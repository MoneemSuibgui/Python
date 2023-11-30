from flask_app import app
from flask_app.models.message import Message
from flask_app.models.user import User
from flask import session,render_template,redirect,request,flash


# the wall page
@app.route('/wall')
def wall():
    if 'user_id' not in session:
        return redirect('/logout')
    user_data={'id':session['user_id']}
    logged_in_user=User.get_by_id(user_data)
    all_users=User.get_all_users(user_data)
    nbr_mg_logged_in_user=Message.get_nbr_of_msg_reciver(user_data)
    nbr_of_massages=Message.get_nbr_of_msg(user_data)
    
    return render_template("wall.html",
                        logged_in_user=logged_in_user
                        ,users=all_users
                        ,nbr_of_massages=nbr_of_massages,
                        nbr_msg_logged_user=nbr_mg_logged_in_user
                        ,all_messages=Message.get_all_messages(user_data))

# create message
@app.route('/create/message', methods=['post'])
def send_message():
    if 'user_id' not in session:
        return redirect('/logout')
    if not Message.validate_msg(request.form):
        return redirect('/wall')
    else:
        message_data={
        'sender_id':session['user_id'],
        'reciver_id':request.form['reciver_id'],
        'content':request.form['content']
        }
        Message.create_msg(message_data)
        return redirect('/wall')


# delete message
@app.route('/delete/message/<int:msg_id>')
def destry_message(msg_id):
    if 'user_id' not in session:
        return redirect('/logout')
    msg_data={
        'id':msg_id
        }
    Message.delete_message(msg_data)
    return redirect('/wall')
    





