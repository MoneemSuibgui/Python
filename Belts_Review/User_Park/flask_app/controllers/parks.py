from flask_app.models.park import Park
from flask_app.models.user import User
from flask_app import app
from flask import session,render_template,redirect,request,flash


# New park
@app.route('/new/parks')
def new_park():
    return render_template("new_park.html")


# create a park
@app.route('/create/park',methods=['post'])
def create_park():
    if 'user_id' not in session:
        return redirect('/logout')
    if not Park.validate_park(request.form):
        return redirect('/new/parks')
    park_data={
        **request.form,'user_id':session['user_id']
    }
    Park.save_park(park_data)
    return redirect('/parks')

# delete a park
@app.route('/parks/<int:park_id>/delete')
def destroy_park(park_id):
    if 'user_id' not in session:
        return redirect('/logout')
    park_data={'id':park_id}
    Park.delete_park(park_data)
    return redirect('/parks')

# get a park by id
@app.route('/parks/<int:id>')
def show_park_info(id):
    park_data={'id':id}
    return render_template("show_park.html",park=Park.get_park_info_by_id(park_data))
    

# edit a park
@app.route('/parks/<int:park_id>/edit')
def edit_park(park_id):
    if 'user_id' not in session:
        return redirect('/logout')
    logged_user={'id':session['user_id']}
    park_data={'id':park_id}
    return render_template("edit_park.html",edit_park=Park.get_park_by_id(park_data),user=User.get_by_id(logged_user))
    

# update a park
@app.route('/update/park' ,methods=['post'])
def update_park():
    if 'user_id' not in session:
        return redirect('/logout')
    
    if not Park.validate_park(request.form):
        return redirect ("/new/parks")
    Park.update_one_park(request.form)
    return redirect('/parks')

# get all parks of one user
@app.route('/my_parks')
def my_parks():
    if 'user_id' not in session:
        return redirect('/logout')
    logged_user={'id':session['user_id']}
    parks=User.get_all_park_for_owner(logged_user)
    return render_template("my_parks.html",parks=parks,user=User.get_by_id({'id':session['user_id']}))
