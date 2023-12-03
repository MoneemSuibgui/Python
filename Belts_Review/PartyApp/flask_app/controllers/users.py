from flask_app import app
from flask_app.models.user import User
from flask import request , redirect, session, render_template, flash
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt(app)

# ========================INDEX PAGE=================

@app.route('/')
def index():
    return render_template("index.html")

#  =======================REGISTER===================

@app.route('/users/create', methods=['post'])
def register():
    if User.validate(request.form):
        hashed_password = bcrypt.generate_password_hash(request.form['password'])
        data = {
            **request.form, 'password':hashed_password
        }
        session['user_id'] = User.create_user(data)
        return redirect('/dashboard')
    return redirect('/')




# ===============================LOGIN===================

@app.route('/users/login', methods = ['post'])
def login():
    # Verify the email : if the email exist
    print(request.form, '*'*25)
    user_form_db = User.get_by_email({'email':request.form['email']})
    print(user_form_db.email,"************")
    if user_form_db:
        # YES exist
        # Check the Password
        if not bcrypt.check_password_hash(user_form_db.password, request.form['password']):
            flash("Invalid Email/Password","login")
            return redirect('/')
        else :
            session['user_id'] = user_form_db.id
            return redirect ('/dashboard')
    flash("Invalid Email/Password","login")
    return redirect('/')


# ==========================LOGOUT==============================
@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')