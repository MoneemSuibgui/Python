from flask_app.models.user import User
from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_bcrypt import Bcrypt
bcrypt=Bcrypt(app)


@app.route('/')
def index():
    return render_template('index.html')


# Register User
@app.route('/register/user', methods=['post'])
def register():
    if  not User.is_valid(request.form):
        return redirect('/')
    
    pass_hash= bcrypt.generate_password_hash(request.form['password'])
    data={
        'first_name':request.form['first_name'],
        'last_name':request.form['last_name'],
        'email':request.form['email'],
        'password':pass_hash
    }
    
    session['user_id']=User.save(data)
    return redirect('/dashboard')


# Login user
@app.route('/login', methods=['post'])
def login():
    
    user_in_db=User.get_by_email({'email':request.form['email']})
    
    if not user_in_db:
        flash("Invalid Email","Login")
        return redirect('/')
    if not bcrypt.check_password_hash(user_in_db.password,request.form['password']):
        flash("Invalid Password","Login")
        return redirect('/')
    
    session['user_id']=user_in_db.id
    return redirect('/dashboard')

# Dashboard : Show user info
@app.route('/dashboard')
def show_info():
    if 'user_id' not in session :
        return redirect('/logout')
    data={
        'id':session['user_id']
    }
    return render_template("dashboard.html",user=User.get_by_id(data))

# Logout
@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')
