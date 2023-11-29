from flask_app import app
from flask import render_template,redirect,request
from flask_app.models.author import Author


@app.route('/authors')
def authors_page():
    return render_template("authors.html",authors=Author.get_all_authors())


# create author
@app.route('/create/author',methods=['post'])
def save():
    Author.create_author(request.form)
    return redirect('/authors')

# get author by id
# get favorites book of one user
@app.route('/authors/<int:id>')
def get_one_author(id):
    author_data={'id':id}
    data={'id':id}
    author=Author.get_author_by_id(author_data)
    favourite_books=Author.get_author_fav_books(author_data)
    unfavourite_books=Author.get_unfav_books(data)
    
    return render_template("authors_show.html",
                        author=author
                        ,favourite_books=favourite_books,
                        unfavourite_books=unfavourite_books)
    

# create favourite books 
@app.route('/create/favourite/book', methods=['post'])
def create_fav_book():
    data={
        'author_id':request.form['author_id'],
        'book_id':request.form['book_id']
    }
    Author.save_fav(data)
    return redirect(f"/authors/{request.form['author_id']}")




