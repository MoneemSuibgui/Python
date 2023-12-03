from flask_app.config.mysqlconnection import connectToMySQL
import re
from flask import flash
EMAIL_REGEX=re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 
from flask_app import db
from datetime import datetime




class User:
    def __init__(self,data):
        
        
        self.id=data['id']
        self.name=data['name']
        self.alias=data['alias']
        self.email=data['email']
        self.password=data['password']
        self.date_birthday=data['date_birthday']
        self.created_at=data['created_at']
        self.updated_at=data['updated_at']


# create user
    @classmethod
    def save_user(cls,data):
        query="INSERT INTO users (name,alias,email,password,date_birthday,created_at) VALUES (%(name)s,%(alias)s,%(email)s,%(password)s,%(date_birthday)s,now()) ;"
        return connectToMySQL(db).query_db(query,data)

# get user by id
    @classmethod
    def get_user_by_id(cls,data):
        query="SELECT * FROM users WHERE id=%(id)s;"
        result=connectToMySQL(db).query_db(query,data)
        return cls(result[0])

# get user by email
    @classmethod
    def get_user_by_email(cls,data):
        query="SELECT * FROM users WHERE email=%(email)s;"
        result=connectToMySQL(db).query_db(query,data)
        if len(result)<1:
            return False
        return cls(result[0])
    

# Register validation
    @staticmethod 
    def valid(user):
        is_valid=True
        query="SELECT * FROM users WHERE email=%(email)s;"
        result=connectToMySQL(db).query_db(query,user)
        if len(result)>=1:
            flash("* Email already taken","register")
            is_valid=False
        if len(user['email'])<8:
            flash("* Email at least be 8 characters","register")
            is_valid=False
        if not EMAIL_REGEX.match(user['email']):
            flash("* Invalid email","register")
            is_valid=False
        if len(user['name'])<3:
            flash("* Name at least be 3 characters","register")
            is_valid=False
        if len(user['alias'])<3:
            flash("* Alias at least be 3 characters","register")
            is_valid=False
        if user['date_birthday'] == "":
            is_valid = False
            flash("* Date birthday is required", "register")
        else:
            
            input_date = datetime.strptime(user['date_birthday'], '%Y-%m-%d').date()
            current_date = datetime.now().date()
                
            if input_date >= current_date:
                is_valid = False
                flash("Input date is in the future", "register")
        if len(user['password'])<8:
            flash("* Password at least be 8 characters","register")
            is_valid=False
        if user['password']!=user['confirm']:
            flash("* Confirm password doesn't match with password","register")
            is_valid=False
        return is_valid

# Login validation 
    @staticmethod
    def valid_login(user):
        is_valid=True
        if user['email']=="":
            flash('* Enter your email adresse','login')
            is_valid=False
        if user['password']=="":
            flash('* Enter your email adresse','login')
            is_valid=False
        return is_valid