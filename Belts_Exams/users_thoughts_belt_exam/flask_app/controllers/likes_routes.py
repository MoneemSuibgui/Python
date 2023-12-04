from flask_app import app
from flask import render_template,redirect,request,session
from flask_app.models.thought_model import Thought
from flask_app.models.like_model import Like


@app.route('/create/like/<int:thought_id>')
def create_like(thought_id):
    if 'user_id' not in session:
        return redirect('logout')
    likes_data={
        'user_id':session['user_id'],
        'thought_id':thought_id
        
    }
    Like.save_like(likes_data)
    return redirect('/dashboard')


@app.route('/delete/like/<int:thought_id>')
def destroy_like(thought_id):
    if 'user_id' not in session:
        return redirect('logout')
    likes_data={
        'user_id':session['user_id'],
        'thought_id':thought_id
    }
    Like.delete_like(likes_data)
    return redirect('/dashboard')
    