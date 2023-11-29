from flask_app.config.mysqlconnection import connectToMySQL
from .book import Book


class Author:
    db="books_schema"
    def __init__(self,data):
        self.id=data['id']
        self.name=data['name']
        self.created_at=data['created_at']
        self.updated_at=data['updated_at']


# create author
    @classmethod
    def create_author(cls,data):
        query="INSERT INTO authors (name,created_at,updated_at) VALUES (%(name)s,now(),now()) ;"
        return connectToMySQL(cls.db).query_db(query,data)
    
# get all author
    @classmethod
    def get_all_authors(cls):
        query="SELECT * FROM authors"
        result=connectToMySQL(cls.db).query_db(query)
        # print(result)
        authors=[]
        for one_author in result:
            authors.append(cls(one_author))
        return authors

# get author by id
    @classmethod
    def get_author_by_id(cls,data):
        query="SELECT* FROM authors WHERE authors.id=%(id)s ;"
        result=connectToMySQL(cls.db).query_db(query,data)
        return cls(result[0])


# get favorites book of one user
    @classmethod
    def get_author_fav_books(cls,data):
        query="""
        SELECT * FROM books LEFT JOIN favourites 
        ON favourites.book_id=books.id
        where author_id=%(id)s ;
        """
        fav_books=[] 
        result=connectToMySQL(cls.db).query_db(query,data)
        for fav_book_db in result:
            if fav_book_db['id']==None:
                break
            data={
                'id':fav_book_db['id'],
                'title':fav_book_db['title'],
                'num_of_page':fav_book_db['num_of_page'],
                'created_at':fav_book_db['created_at'],
                'updated_at':fav_book_db['updated_at']
                }
            
            fav_books.append(Book(data))
        return fav_books
            


# unfavorites book
    @classmethod
    def get_unfav_books(cls,data):
        query="""
        SELECT * FROM books WHERE books.id NOT IN
        (SELECT book_id FROM favourites WHERE author_id=%(id)s );
        """
        result=connectToMySQL(cls.db).query_db(query,data)
        unfav_books=[]
        for books in result:
            unfav_books.append(Book(books))
        print(unfav_books)
        return unfav_books
        
        
# create favourite 
    @classmethod
    def save_fav(cls,data):
        query="INSERT INTO favourites (author_id,book_id) VALUES (%(author_id)s,%(book_id)s);"
        return connectToMySQL(cls.db).query_db(query,data)