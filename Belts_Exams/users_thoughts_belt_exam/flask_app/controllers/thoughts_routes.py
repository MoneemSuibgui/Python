from flask_app import app
from flask import render_template,redirect,request,session
from flask_app.models.thought_model import Thought
from flask_app.models.user_model import User
from flask_app.models.like_model import Like





# dashboard
@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        return redirect('/logout')
    logged_in_user=User.get_user_by_id({'id':session['user_id']}) 
    return render_template("dashboard.html"
                        ,logged_in_user=logged_in_user
                        ,all_thoughts=Thought.get_all_thoughts()
                        ,likes=Like.like_list({'id':session['user_id']})
                        ,nbrs_likes=Thought.get_nbrs_likes_all_thoughts())





# create a thought
@app.route('/create/thought' ,methods=['post'])
def create_thought():
    if 'user_id' not in session:
        return redirect('/logout')
    if not Thought.valid_thought(request.form):
        return redirect('/dashboard')
    thought_data={
        'user_id':session['user_id'],
        'content':request.form['content']
    }
    session['thought_id']=Thought.save_thought(thought_data)
    return redirect('/dashboard')

# delete one thought
@app.route('/delete/thought/<int:thought_id>')
def destroy_thought(thought_id):
    if 'user_id' not in session:
        return redirect('/logout')
    thought_data={'id':thought_id}
    Thought.delete_thought(thought_data)
    return redirect("/dashboard" )


# get one user by id
@app.route('/users/<int:user_id>')
def get_one_user_by_id(user_id):
    if 'user_id' not in session:
        return redirect('/logout')
    logged_in_user_data={'id':session['user_id']}
    user_data={'id':user_id}
    return render_template("show_info.html",
                        user=User.get_user_by_id(logged_in_user_data)
                        ,thoughts=Thought.get_user_thoughts(user_data)
                        ,creator_thoughts=User.get_user_by_id(user_data))


