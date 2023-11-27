from user import User
from flask import Flask, render_template, request, redirect
app = Flask(__name__)




@app.route('/')
def go_index():
    return redirect('/users')


#Read all users
@app.route("/users")
def index():
    users = User.get_all()
    return render_template("index.html", users=users)

# new user form
@app.route('/users/new')
def new_user():
    return render_template('user.html')

# create New User
@app.route('/users/create', methods=['POST'])
def create_user():
    User.create_user(request.form)
    return redirect ('/users')




if __name__ == "__main__":
    app.run(debug=True,port=5070)