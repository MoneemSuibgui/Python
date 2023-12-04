from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.models.visit import Visit


# delete visitor
@app.route('/delete/visitor/<int:tree_id>')
def destroy_visitor(tree_id):
    if 'user_id' not in session:
        return redirect('/logout')
    visitor_data={
        'user_id':session['user_id'],
        'tree_id':tree_id
    }
    Visit.delete_visitor(visitor_data)
    return redirect(f"/show/{tree_id}")


# create visitor
@app.route('/create/visitor/<int:tree_id>')
def create_visistor(tree_id):
    if 'user_id' not in session:
        return redirect('/logout')
    visitor_data={
        'user_id':session['user_id'],
        'tree_id':tree_id
    }
    Visit.save_visitor(visitor_data)
    return redirect(f"/show/{tree_id}")