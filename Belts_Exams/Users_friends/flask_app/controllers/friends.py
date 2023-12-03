from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.models.user import User
from flask_app.models.friend import Friend

# friends page
@app.route('/friends')
def dashboard():
    user_data={'id':session['user_id']}
    return render_template('friends.html'
                        ,logged_in_user=User.get_user_by_id(user_data)
                        ,all_friends=Friend.get_all_friends(user_data)
                        ,unfriends_list=Friend.get_all_unfriends(user_data))
    

# create friends
@app.route('/create/friend/<int:user_id>')
def save_friend(user_id):
    if 'user_id' not in session:
        return redirect('/logout')
    user_data={
        'user_id':session['user_id'],
        'friend_id':user_id
    }
    Friend.create_friend(user_data)
    return redirect('/friends')

# delete friends
@app.route('/delete/friend/<friend_id>')
def destroy_friend(friend_id):
    if 'user_id' not in session:
        return redirect('/logout')
    friend_data={
        'user_id':session['user_id'],
        'friend_id':friend_id
    }
    Friend.delete_friend(friend_data)
    return redirect('/friends')


# show info friend
@app.route('/user/<int:user_id>')
def show_info_friend(user_id):
    user_info=User.get_user_by_id({'id':user_id})
    return render_template("show_user.html",user_info=user_info)
    
