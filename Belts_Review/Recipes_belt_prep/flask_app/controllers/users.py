from flask_app import app
from flask_app.models.user import User
from flask_app.models.recipe import Recipe
from flask import session,render_template,redirect,request,flash
from flask_bcrypt import Bcrypt
bcrypt=Bcrypt(app)

@app.route('/')
def index():
    return render_template("index.html")

# register
@app.route('/create/user',methods=['post'])
def register():
    
    if not User.validate_user(request.form):
        return redirect('/')
    
    data={
        'first_name':request.form['first_name'],
        'last_name':request.form['last_name'],
        'email':request.form['email'],
        'password':bcrypt.generate_password_hash(request.form['password'])
        }
    session['user_id']=User.create_user(data)
    return redirect('/dashboard')

# Login
@app.route('/login',methods=['post'])
def login():
    user_in_db=User.get_by_email(request.form)
    if not user_in_db:
        flash("* Invalid email adresse","login")
        return redirect('/')
    if not bcrypt.check_password_hash(user_in_db.password,request.form['password']):
        flash("* Invalid password","login")
        return redirect('/')
    session['user_id']=user_in_db.id
    return redirect('/dashboard')

# dasboard
@app.route('/dashboard')
def show_info():
    if 'user_id' not in session:
        return redirect('/logout')
    
    return render_template("dashboard.html",user=User.get_by_id({'id':session['user_id']}),recipes=Recipe.get_all_recipes())

# logout
@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')