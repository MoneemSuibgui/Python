from flask_app import app
from flask_app.models.user import User
from flask import render_template,redirect,request


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/create/user',methods=['post'])
def save():
    
    if not(User.validate_email(request.form)):
        return redirect('/')
    else:
        User.create_email(request.form)
    
    return redirect('/success')

@app.route('/success')
def show_emails():
    return render_template("success.html",all_users=User.get_users_info())
    

@app.route('/destroy/<int:id>')
def destroy(id):
    data={
        'id':id
    }
    
    User.destroy_one_user(data)
    return redirect('/success')