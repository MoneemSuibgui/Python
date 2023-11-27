from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import author



class Book:
    
    db="books_schema"
    
    def __init__(self,data):
        self.id=data['id']
        self.title=data['title']
        self.num_of_page=data['num_of_page']
        self.created_at=data['created_at']
        self.updated_at=data['updated_at']



#create a new book
    @classmethod
    def create_book(cls,data):
        query="INSERT INTO books (title,num_of_page,created_at,updated_at) VALUES(%(title)s,%(num_pages)s,now(),now()) ;"
        return connectToMySQL('books_schema').query_db(query,data)
    
# get all books
    @classmethod
    def get_all_books(cls):
        query="SELECT * FROM books ;"
        result= connectToMySQL('books_schema').query_db(query)
        books=[]
        for one_book in result:
            books.append(cls(one_book))
        return books
        

# get author by id
    @classmethod
    def get_book_by_id(cls,data):
        query="SELECT * FROM books WHERE id=%(id)s;"
        result=connectToMySQL(cls.db).query_db(query,data)
        return cls(result[0])
    
# get favourites book
    @classmethod
    def get_fav_authors(cls,data):
        query="""
        SELECT * FROM books 
        LEFT JOIN favourites ON favourites.book_id=books.id
        LEFT JOIN authors ON favourites.author_id=authors.id
        WHERE books.id=%(id)s;
        """
        favourites_authors=[]
        result=connectToMySQL(cls.db).query_db(query,data)
        for row in result:
            if row['authors.id']==None:
                break
            author_data={
                'id':row['authors.id'],
                'name':row['name'],
                'created_at':row['authors.created_at'],
                'updated_at':row['authors.updated_at']
            }
            favourites_authors.append(author.Author(author_data))
        return favourites_authors
    

# get unfavourite authors
    @classmethod
    def get_unfav_authors(cls,data):
        query="SELECT * FROM authors WHERE authors.id NOT IN (SELECT author_id FROM favourites  WHERE book_id=%(id)s);"
        result=connectToMySQL(cls.db).query_db(query,data)
        unfav_authors=[]
        for authors_data in result:
            
            unfav_authors.append(author.Author(authors_data))
            print(unfav_authors)
        return unfav_authors
