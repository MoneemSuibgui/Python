from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.models.user import User
from flask_bcrypt import Bcrypt
bcrypt=Bcrypt(app)


# register & login page
@app.route('/')
def index():
    return render_template('login_register.html')

# register
@app.route('/create/user', methods=['post'])
def register():
    
    if not User.valid(request.form):
        return redirect('/')
    data={
        'first_name':request.form['first_name'],
        'last_name':request.form['last_name'],
        'email':request.form['email'],
        'password':bcrypt.generate_password_hash(request.form['password'])
    }
    session['user_id']=User.save_user(data)
    return redirect('/dashboard')


# login
@app.route('/login',methods=["post"])
def login():
    user_in_db=User.get_user_by_email({'email':request.form['email']})
    
    if not User.valid_login(request.form):
        return redirect('/')
    if not user_in_db:
        flash("* Invalid Email Adresse","login")
        return redirect('/')
    
    if not bcrypt.check_password_hash(user_in_db.password,request.form['password']):
        flash("* Invalid Password","login")
        return redirect('/')
    else:
        session['user_id']=user_in_db.id
        return redirect('/dashboard')




# logout 
@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')