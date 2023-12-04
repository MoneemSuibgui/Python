from flask_app.config.mysqlconnection import connectToMySQL
import re
from flask import flash
EMAIL_REGEX=re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 




class User:
    db="users_plants_db"
    def __init__(self,data):
        self.id=data['id']
        self.first_name=data['first_name']
        self.last_name=data['last_name']
        self.email=data['email']
        self.password=data['password']
        self.created_at=data['created_at']
        self.updated_at=data['updated_at']
        
    def full_name(self):
        return f"{self.first_name} {self.last_name}"
    
# create user
    @classmethod
    def save_user(cls,data):
        query="INSERT INTO users (first_name,last_name,email,password,created_at) VALUES (%(first_name)s,%(last_name)s,%(email)s,%(password)s,now()) ;"
        return connectToMySQL(cls.db).query_db(query,data)

# get user by id
    @classmethod
    def get_user_by_id(cls,data):
        query="SELECT * FROM users WHERE id=%(id)s;"
        result=connectToMySQL(cls.db).query_db(query,data)
        return cls(result[0])

# get user by email
    @classmethod
    def get_user_by_email(cls,data):
        query="SELECT * FROM users WHERE email=%(email)s;"
        result=connectToMySQL(cls.db).query_db(query,data)
        if len(result)<1:
            return False
        return cls(result[0])



# validation
    @staticmethod 
    def valid(user):
        is_valid=True
        query="SELECT * FROM users WHERE email=%(email)s;"
        result=connectToMySQL(User.db).query_db(query,user)
        if len(result)>=1:
            flash("* Email already taken")
            is_valid=False
        if len(user['email'])<8:
            flash("* Email at least be 8 characters","register")
            is_valid=False
        if not EMAIL_REGEX.match(user['email']):
            flash("* Invalid email","register")
            is_valid=False
        if len(user['first_name'])<3:
            flash("* First name at least be 3 characters","register")
            is_valid=False
        if len(user['last_name'])<3:
            flash("* last name at least be 3 characters","register")
            is_valid=False
        if len(user['password'])<8:
            flash("* Password at least be 8 characters","register")
            is_valid=False
        if user['password']!=user['confirm']:
            flash("Confirm password doesn't match with password","register")
            is_valid=False
        return is_valid

# validation login
    @staticmethod
    def valid_login(user):
        is_valid=True
        if user['email']=="":
            flash('* Enter your email adresse',"login")
            is_valid=False
        if user['password']=="":
            flash('* Enter your email adresse',"login")
            is_valid=False
        return is_valid