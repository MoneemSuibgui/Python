from flask_app import app
from flask import render_template,redirect,request,session
from flask_app.models.dojo import Dojo

@app.route('/')
def index():
    return render_template("index.html")



#create dojo
@app.route('/create/dojo',methods=['post'])
def save_dojo():
    
    if not Dojo.validate_dojo(request.form):
        return redirect('/')
    else:
        Dojo.create_dojo(request.form)
        session['dojo_name']=request.form['name']
        session['dojo_location']=request.form['location']
        session['dojo_fav_language']=request.form['favorite_language']
        session['dojo_comment']=request.form['comment']
        
    return redirect('/results')


@app.route('/results')
def get_dojo_info():
    return render_template("result.html",name=session['dojo_name'],location=session['dojo_location'],language=session['dojo_fav_language'],comment=session['dojo_comment'])


