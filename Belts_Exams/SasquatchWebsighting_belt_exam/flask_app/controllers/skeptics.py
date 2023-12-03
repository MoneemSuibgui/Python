from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.models.skeptic import Skeptic
from flask_app.models.sight import Sight






@app.route('/skeptic/<int:one_sight_id>/create')
def skeptik_save(one_sight_id):
    if  'user_id' not in session:
        return redirect('/')
    data = {
            'user_id' : session['user_id'],
            'sight_id' : one_sight_id
        }
    
    Skeptic.save_skeptics(data)
    return redirect(f"/sight/{one_sight_id}")
    



@app.route('/skeptic/<int:one_sight_id>/delete')
def delete_skeptics(one_sight_id):
    skeptic_data={
        'user_id':session['user_id'],
        'sight_id':one_sight_id
    }
    Skeptic.delete_skeptic(skeptic_data)
    return redirect(f"/sight/{one_sight_id}")