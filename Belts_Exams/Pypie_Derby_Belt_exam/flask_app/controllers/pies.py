from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.models.pie import Pie
from flask_app.models.user import User
from flask_app.models.vote import Vote


@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        return redirect('/logout')
    logged_in_user_data={'id':session['user_id']}
    return render_template("dashboard.html",
                        user=User.get_user_by_id(logged_in_user_data)
                        ,all_pypies=Pie.get_pypies_of_user(logged_in_user_data))


@app.route('/create/pie' ,methods=['post'])
def create_pie():
    if 'user_id' not in session:
        return redirect('/logout')
    if not Pie.valid_pie(request.form):
        return redirect('/dashboard')
    pie_data={
        **request.form,'user_id':session['user_id']
    }
    Pie.save_pie(pie_data)
    return redirect('/dashboard')


@app.route('/delete/<pypie_id>')
def delete_pypie(pypie_id):
    if 'user_id' not in session:
        return redirect('/logout')
    pypie_data={
        'id':pypie_id,
        'user_id':session['user_id']
    }
    Pie.destroy_pypie(pypie_data)
    return redirect('/dashboard')


@app.route('/edit/<pypie_id>')
def edit_pypie(pypie_id):
    if 'user_id' not in session:
        return redirect('/logout')
    edit_pypie=Pie.get_pypie_by_id({'id':pypie_id})
    return render_template("edit_pie.html",edit_pypie=edit_pypie)


@app.route('/update/pypie' ,methods=['post'])
def update_one():
    if 'user_id' not in session:
        return redirect('/logout')
    if not Pie.valid_pie(request.form):
        return redirect(f"/edit/{request.form['id']}")
    pypie_data={
        **request.form,'id':request.form['id']
    }
    Pie.update_pypie(pypie_data)
    return redirect('/dashboard')

@app.route('/pie_derby')
def get_all_info():
    if 'user_id' not in session:
        return redirect('/logout')
    all_pypies=Pie.get_all_pypies()
    return render_template('pies_info.html',all_pypies=all_pypies)

@app.route('/vote/<int:pypie_id>')
def vote_page(pypie_id):
    if 'user_id' not in session:
        return redirect('/logout')
    one_pypie=Pie.get_pypie_by_id({'id':pypie_id})
    vote_data={
        'pypie_id':pypie_id,
        'user_id':session['user_id']
        }
    return render_template("vote.html",one_pypie=one_pypie
                        ,vote=Vote.get_votes_list_one_pypie(vote_data))
    

