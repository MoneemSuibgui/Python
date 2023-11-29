from flask_app import app
from flask_app.models.dojo import Dojo
from flask import render_template,redirect,request


# display all dojos
@app.route('/dojos')
def dojo_home():
    return render_template("create_dojo.html",dojos=Dojo.get_allDojo())

@app.route('/')
def index():
    return redirect('/dojos')

#create dojo
@app.route('/create/dojo',methods=['post'])
def save_dojo():
    Dojo.create_dojo(request.form)
    return redirect('/')



# show all ninjas of one dojo
@app.route('/dojos/<int:id>')
def display_ninjas_dojo(id):
    data={
        'id':id
    }
    return render_template("dojo_show.html",dojo=Dojo.get_ninjas_dojo(data))








