from flask_app import app
from flask import render_template,redirect,request
from flask_app.models.book import Book
from flask_app.models.author import Author




@app.route('/')
def index():
    return redirect('/books')

@app.route('/books')
def book_page():
    return render_template("books.html",all_books=Book.get_all_books())

#create a new book
@app.route('/create/book',methods=['post'])
def save_book():
    Book.create_book(request.form)
    return redirect('/books')

# get book by id
@app.route('/books/<int:id>')
def get_book(id):
    book_data={'id':id}

    return render_template("book_show.html",
                        book=Book.get_book_by_id(book_data),
                        fav_authors=Book.get_fav_authors(book_data),
                        unfavourites_authors=Book.get_unfav_authors(book_data))


# create favourite author 
@app.route('/create/fav/author',methods=['post'])
def create_fav_author():
    data={
        'author_id':request.form['author_id'],
        'book_id':request.form['book_id']
    }
    Author.save_fav(data)
    return redirect(f"/books/{request.form['book_id']}")









