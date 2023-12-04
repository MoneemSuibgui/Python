from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.models.user import User
from flask_app.models.tree import Tree
from flask_app.models.visit import Visit




# dashboard
@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        return redirect('/logout')
    logged_in_user_data={'id':session['user_id']}
    return render_template("dashboard.html",
                        user=User.get_user_by_id(logged_in_user_data)
                        ,all_trees=Tree.get_all_trees())
    
    
# new tree
@app.route('/new/tree')
def new_tree():
    logged_in_user_data={'id':session['user_id']}
    return render_template("plan_tree.html",user=User.get_user_by_id(logged_in_user_data))


# create_new tree
@app.route('/plant/tree',methods=['post'])
def plant_tree():
    if 'user_id' not in session:
        return redirect('/logout')
    if not Tree.valid_plant(request.form):
        return redirect('/new/tree')
    data_tree={
        **request.form,'user_id':session['user_id']
    }
    Tree.save_tree(data_tree)
    return redirect('/dashboard')

# show tree info
@app.route('/show/<int:tree_id>')
def show_info(tree_id):
    if 'user_id' not in session:
        return redirect('/logout')
    one_tree=Tree.get_tree_by_id({'id':tree_id})
    user=User.get_user_by_id({'id':session['user_id']})
    visitors=Visit.get_visitors_one_tree({'id':tree_id})
    visitor_data={
        'user_id':session['user_id'],
        'tree_id':tree_id
    }
    id_visitor=Visit.get_id_visitor_one_tree(visitor_data)
    return render_template("show_info_tree.html",one_tree=one_tree,user=user,visitors=visitors,id_visitor=id_visitor)


# get my trees
@app.route('/user/account')
def show_my_trees():
    if 'user_id' not in session:
        return redirect('/logout')
    user=User.get_user_by_id({'id':session['user_id']})
    user_data={
        'id':session['user_id']
        }
    all_my_trees=Tree.get_my_trees(user_data)
    return render_template("my_trees.html",user=user,all_my_trees=all_my_trees)


# delete tree
@app.route('/delete/<int:tree_id>')
def destroy_tree(tree_id):
    if 'user_id' not in session:
        return redirect('/logout')
    tree_data={
        'user_id':session['user_id'],
        'id':tree_id
    }
    Tree.delete_tree(tree_data)
    return redirect('/user/account')


# edit tree
@app.route('/edit/<int:tree_id>')
def edit_tree(tree_id):
    if 'user_id' not in session:
        return redirect('/logout')
    tree=Tree.get_tree_by_id({'id':tree_id})
    user=User.get_user_by_id({'id':session['user_id']})
    return render_template("edit_tree.html",tree=tree,user=user)


# create_new tree
@app.route('/update/tree',methods=['post'])
def update():
    if 'user_id' not in session:
        return redirect('/logout')
    if not Tree.valid_plant(request.form):
        return redirect(f"/edit/{request.form['id']}")
    data_tree={
        **request.form,'id':request.form['id']
    }
    Tree.update_tree(data_tree)
    return redirect('/user/account')
