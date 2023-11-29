
from flask_app import app 
from flask import render_template,redirect,request
from flask_app.models.user import User




# redirect to main page
@app.route('/')
def go_home():
    return redirect('/users')

# render our main page (read.html)
@app.route('/users')
def home():
    return render_template("read.html",user=User.get_all_users())

# create new user
@app.route('/create/user',methods=['post'])
def register():
    User.save(request.form)
    return redirect('/users/new')

# user form
@app.route('/users/new')
def index():
    return render_template("create.html")


# delete one user
@app.route('/users/destroy/<int:id>')
def destroy_user(id):
    data={
        "id":id
    }
    User.destroy(data)
    return redirect('/users')

# edit one user
@app.route('/users/edit/<int:id>')
def edit_user(id):
    data={
        "id":id
    }
    return render_template("edit.html",one_user=User.get_by_id(data))


# update one user
@app.route('/update/user',methods=['post'])
def update_user():
    User.update_user(request.form)
    return redirect('/users')

# show one user
@app.route('/user/<int:id>')
def show_user_info(id):
    user_data={'id':id}
    return render_template("read_one.html",one_user=User.get_by_id(user_data))