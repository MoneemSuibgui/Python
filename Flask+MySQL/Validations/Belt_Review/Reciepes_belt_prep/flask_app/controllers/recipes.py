from flask_app import app
from flask_app.models.recipe import Recipe
from flask_app.models.user import User
from flask import render_template,redirect,request,session

@app.route('/recipes/new')
def add_recipe():
    if 'user_id' not in session:
        return redirect('/logout')
    else:
        return render_template("create_recipes.html",user=User.get_by_id({'id':session['user_id']}))

# Create recipe
@app.route('/create/recipe',methods=['post'])
def create_recipe():
    
    if not Recipe.validate_recipe(request.form):
        return redirect('/recipes/new')
    if 'user_id' not in session:
        return redirect('/logout')
    
    data={
        'name':request.form['name'],
        'description':request.form['description'],
        'instruction':request.form['instruction'],
        'date_made':request.form['date_made'],
        'under_30':int(request.form['under_30']),
        'user_id':session['user_id']
    }
    Recipe.save_recipe(data)
    return redirect ('/dashboard')

# show one recipe
@app.route('/recipes/<int:id>')
def show_recipes(id):
    if not 'user_id' in session:
        return redirect('/logout')
    data={'id':id}
    user_data={'id': session['user_id']}
    return render_template("show_recipes.html",user=User.get_by_id(user_data),one_recipe=Recipe.get_one_recipe(data))

# edit one recipe
@app.route('/recipes/edit/<int:id>')
def edit_recipe(id):
    if not 'user_id' in session:
        return redirect('/logout')
    data={'id':id}
    user_data={'id':session['user_id']}
    return render_template("edit_recipes.html",edit_recipe=Recipe.get_one_recipe(data),user=User.get_by_id(user_data))


# update one recipe
@app.route('/update/recipe/', methods=['post'])
def update_recipe():
    if not 'user_id' in session :
        return redirect('/logout')
    if not Recipe.validate_recipe(request.form):
        return redirect(f"/recipes/edit/{request.form['id']}")
    data={
        'id':request.form['id'],
        'name':request.form['name'],
        'description':request.form['description'],
        'instruction':request.form['instruction'],
        'date_made':request.form['date_made'],
        'under_30':int(request.form['under_30'])
    }
    Recipe.update_one_recipe(data)
    return redirect('/dashboard')

# delete show 
@app.route('/destroy/<int:id>')
def destroy_recipe(id):
    Recipe.destroy_one({'id':id})
    return redirect('/dashboard')