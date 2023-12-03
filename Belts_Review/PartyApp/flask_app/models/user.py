from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app import DATABASE
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 

class User:
    def __init__(self,data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']

    # =======================Queries=======================

    # - CREATE
    @classmethod
    def create_user(cls, data):
        query = """
            INSERT INTO users (first_name,last_name,password,email)
            VALUES (%(first_name)s,%(last_name)s,%(password)s,%(email)s);
        """
        return connectToMySQL(DATABASE).query_db(query,data)
    
    # - GET ONE BY EMAIL
    @classmethod
    def get_by_email(cls,data):
        query = """
            SELECT * FROM users WHERE email = %(email)s; 
        """
        results = connectToMySQL(DATABASE).query_db(query,data)
        print(results,"-++-"*25)
        if len(results)<1:
            return False
        return cls(results[0])

    # - GET ONE BY ID
    @classmethod
    def get_by_id(cls,data):
        query = """
            SELECT * FROM users WHERE id = %(id)s; 
        """
        results = connectToMySQL(DATABASE).query_db(query,data)
        if len(results)<1:
            return False
        return cls(results[0])
    
    # ! VALIDATIONS
    @staticmethod
    def validate(data):
        is_valid = True
        if len(data['first_name'])<2:
            is_valid = False
            flash("First Name must be at least 2","register")
        if len(data['last_name'])<2:
            is_valid = False
            flash("Last Name must be at least 2","register")
        if not EMAIL_REGEX.match(data['email']): 
            is_valid = False
            flash("Email not valid","register")
        elif User.get_by_email({'email':data['email']}):
            is_valid = False
            flash("Email Already Exist","register")
        if len(data['password'])<6:
            is_valid = False
            flash("Password greater than 6","register")
        elif data['password']!= data['confirm_password']:
            is_valid = False
            flash("Password and Confirm password must match","register")
        return is_valid