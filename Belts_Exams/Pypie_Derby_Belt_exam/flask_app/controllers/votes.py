from flask_app import app
from flask import redirect,session
from flask_app.models.vote import Vote

# create vote
@app.route('/create/vote/<pypie_id>')
def save_vote(pypie_id):
    
    vote_date={
        'pypie_id':pypie_id,
        'user_id':session['user_id']
    }
    Vote.create_vote(vote_date)
    return redirect(f"/vote/{pypie_id}")


# delete vote
@app.route('/delete/vote/<pypie_id>')
def destroy_vote(pypie_id):
    
    vote_date={
        'pypie_id':pypie_id,
        'user_id':session['user_id']
    }
    Vote.delete_vote(vote_date)
    return redirect(f"/vote/{pypie_id}")