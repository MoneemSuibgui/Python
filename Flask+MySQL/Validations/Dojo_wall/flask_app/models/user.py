from flask_app.config.sql_connection import connectToMySQL
from flask import flash
import re
from flask_app import db
EMAIL_REGEX= re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 

class User:
    
    def __init__(self,data):
        self.id=data['id']
        self.first_name=data['first_name']
        self.last_name=data['last_name']
        self.email=data['email']
        self.password=data['password']
        self.created_at=data['created_at']
        self.updated_at=data['updated_at']
    
# get full name
    def full_name(self):
        return f"{self.first_name} {self.last_name}"
        
#create user
    @classmethod
    def create_user(cls,data):
        query="""
        INSERT INTO users (first_name,last_name,email,password) 
        VALUES (%(first_name)s,%(last_name)s,%(email)s,%(password)s)
        """
        return connectToMySQL(db).query_db(query,data)

#get user by id
    @classmethod
    def get_by_id(cls,data):
        query="SELECT * FROM users WHERE id=%(id)s ;"
        result= connectToMySQL(db).query_db(query,data)
        return cls(result[0])

# get user by email
    @classmethod
    def get_by_email(cls,data):
        query="SELECT * FROM users WHERE email=%(email)s;"
        result=connectToMySQL(db).query_db(query,data)
        if len(result)<1:
            return False
        return cls(result[0])

# get all users
    @classmethod
    def get_all_users(cls,data):
        query="""
        SELECT * FROM users ;
        """
        results=connectToMySQL(db).query_db(query,data)
        if len(results)<1:
            return False
        return results





# User validation
    @staticmethod
    def validate_user(user):
        is_valid=True
        query="SELECT * FROM users WHERE email=(%(email)s);"
        result=connectToMySQL(db).query_db(query,user)
        if len(result)>=1:
            flash("* Email adresse used","register")
            is_valid=False
        if not EMAIL_REGEX.match(user['email']):
            flash("* Invalid email adresse ","register")
            is_valid=False
        if len(user['first_name'])<3:
            flash("* First name at least be 4 characters","register")
            is_valid=False
        if len(user['last_name'])<3:
            flash("* Last name at least be 4 characters","register")
            is_valid=False
        if len(user['email'])<8:
            flash("* Email at least be 8 characters","register")
            is_valid=False
        if len(user['password'])<8:
            flash("* Password at least be 8 characters","register")
            is_valid=False
        if (user['password'])!=(user['confirm']):
            flash("* Password and Confirm Password doesn't match","register")
            is_valid=False
        return is_valid