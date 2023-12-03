from flask_app import app
from flask_app.models.user import User
from flask_app.models.party import Party
from flask import request , redirect, session, render_template, flash


# ===========================DASHBOARD==================
@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        return redirect('/')
    all_parties = Party.get_all_parties()
    logged_user = User.get_by_id({'id':session['user_id']})
    return render_template("dashboard.html", all_parties = all_parties, user = logged_user)

# =============================NEW PARTY===============
@app.route('/parties/new')
def new_party():
    if 'user_id' not in session:
        return redirect('/')
    return render_template("add_party.html")

# =============================CREATE PARTY============
@app.route('/parties/create', methods=['post'])
def create_party():
    if not Party.validate(request.form):
        return redirect('/parties/new')
    print(request.form,"*"*25)
    data = {
        **request.form, 'user_id':session['user_id']
    }
    print(data,"*"*25)
    Party.create_party(data)
    return redirect('/dashboard')

# =============================EDIT=================
@app.route('/parties/<int:party_id>/edit')
def edit_party(party_id):
    if 'user_id' not in session:
        return redirect('/')
    party = Party.get_by_id({'id':party_id})
    return render_template("edit_party.html",party = party)

# =========================UPDATE====================
@app.route('/parties/update',methods=['post'])
def update_party():
    Party.update_party(request.form)
    return redirect('/dashboard')

# =======================MY PARTIES===========
@app.route('/my_parties')
def my_parties():
    user_parties = Party.get_user_parties({'user_id':session['user_id']})
    logged_user = User.get_by_id({'id':session['user_id']})
    return render_template("my_parties.html", parties = user_parties, user = logged_user)