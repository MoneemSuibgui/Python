from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.models import user ,sight,skeptic




@app.route('/dashboard')
def dashbaord():
    if 'user_id' not in session:
        return redirect('/logout')
    return render_template("dashboard.html"
                        ,logged_in_user=user.User.get_user_by_id({'id':session['user_id']})
                        ,all_sightings=sight.Sight.get_all_sightings()
                        ,nbrs_skepticals=skeptic.Skeptic.count_skipticals_in_dashboard())


# create sight
@app.route('/new/sight')
def new_sight():
    if 'user_id' not in session:
        return redirect('/logout')
    return render_template("create_sight.html",logged_in_user=user.User.get_user_by_id({'id':session['user_id']}))

# save sight
@app.route('/create/sight',methods=['post'])
def create_new_sight():
    if 'user_id' not in session:
        return redirect('/logout')
    if not sight.Sight.valid_sight(request.form):
        return redirect('/new/sight')
    data={
        'location':request.form['location'],
        'content':request.form['content'],
        'date_sight':request.form['date_sight'],
        'number_s':request.form['number_s'],
        'user_id':session['user_id']
    }
    sight.Sight.save_sight(data)
    return redirect('/dashboard')



# delete sight
@app.route('/delete/<int:sight_id>')
def delete_like(sight_id):
    if 'user_id' not in session:
        return redirect('/logout')
    sight_data={
        'id':sight_id
    }
    sight.Sight.delete_sight(sight_data)
    return redirect('/dashboard')


# edit show
@app.route('/edit/<int:sight_id>')
def edit_sight(sight_id):
    if 'user_id' not in session:
        return redirect('/logout')
    sight_data={'id':sight_id}
    return render_template("edit_sighting.html",edit_sight=sight.Sight.get_sight_by_id(sight_data)
                        ,logged_in_user=user.User.get_user_by_id({'id':session['user_id']}))

# update show
@app.route('/update/sight',methods=['post'])
def update_one_show():
    if 'user_id' not in session:
        return redirect('/logout')
    if not sight.Sight.valid_sight(request.form):
        return redirect(f"/edit/{request.form['id']}")
    sight_data={
        **request.form,'id':request.form['id']
    }
    sight.Sight.update_sight(sight_data)
    return redirect('/dashboard')

# view
@app.route('/sight/<int:sight_id>')
def show_sight(sight_id):
    if 'user_id' not in session:
        return redirect('/logout')
    sight_data={
        'id':sight_id
    }
    user_data={'id':session['user_id']}
    one_sight=sight.Sight.get_one_sight(sight_data)
    skiptics=skeptic.Skeptic.get_all_skiptics_one_sight(sight_data)
    return render_template("show_sight_info.html"
                        ,one_sight=one_sight,skiptics=skiptics
                        ,list_ids_skeptics=skeptic.Skeptic.get_lsit_skeptics_one_sight(sight_data)
                        ,logged_in_user=user.User.get_user_by_id(user_data)
                        ,nbrs_skepticals=skeptic.Skeptic.count_skiptics(sight_data))