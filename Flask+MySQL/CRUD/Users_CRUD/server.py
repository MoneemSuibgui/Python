
from flask import  Flask ,render_template, request, redirect
app=Flask(__name__)
from user import User


# get all users
@app.route('/users')
def display_users():
    return render_template('all_users.html',users=User.get_allUsers())

# "/" route redirect to "/users" route (main page)
@app.route('/')
def index():
    return redirect('/users')

#create user
@app.route('/create/user',methods=['post'])
def save_user():
    User.create_user(request.form)
    return redirect('/users/new')

# user form 
@app.route('/users/new')
def all_users():
    return render_template("create_user.html")

# get user info
@app.route('/show/user/<int:id>')
def get_info_user(id):
    data={
        'id':id
    }
    return render_template("show_user.html",user_info=User.get_user(data))

# delete user
@app.route('/destroy/user/<int:id>')
def destroy(id):
    data={
        'id':id
    }
    User.destroy_user(data)
    return redirect('/')

# edit user
@app.route('/edit/user/<int:id>')
def edit_user(id):
    data={
        'id':id
    }
    return render_template("edit_user.html",one_info=User.get_user(data))

# update user
@app.route('/update/user',methods=['post'])
def set_info_user():
    User.update_user(request.form)
    return redirect('/')

if __name__=="__main__":
    app.run(debug=True,port=5009)