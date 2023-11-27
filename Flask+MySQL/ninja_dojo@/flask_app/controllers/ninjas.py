from flask_app import app
from flask import render_template,redirect,request
from flask_app.models import ninja,dojo


@app.route('/ninjas')
def ninja_home():
    return render_template('create_ninja.html',all_dojos=dojo.Dojo.get_allDojo())

# create ninja
@app.route('/create/ninja',methods=['post'])
def save_ninja():
    ninja.Ninja.create_ninja(request.form)
    return redirect('/ninjas')