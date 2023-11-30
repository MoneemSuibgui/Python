from flask_app.config.mysql_connection import connectToMySQL
from flask import flash
import re
EMAIL_REGEX= re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 



class User:
    db='login_registration'
    def __init__(self,data):
        self.id=data['id']
        self.first_name=data['first_name']
        self.last_name=data['last_name']
        self.email=data['email']
        self.password=data['password']
        self.created_at=data['created_at']
        self.updated_at=data['updated_at']
        
# instance method to get full name of user
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

# create user
    @classmethod
    def save(cls,data):
        query="""
        INSERT INTO users (first_name,last_name,email,password
        ,created_at,updated_at) VALUES (%(first_name)s,%(last_name)s,
        %(email)s,%(password)s,now(),now())
        """
        return connectToMySQL(cls.db).query_db(query,data)
    

# get user by email(checked to login)
    @classmethod
    def get_by_email(cls,data):
        query="SELECT * FROM users WHERE email=(%(email)s);"
        result=connectToMySQL(cls.db).query_db(query,data)
        if len(result) < 1 :
            return False
        return cls(result[0])
    

# get user by id
    @classmethod
    def get_by_id(cls,data):
        query="SELECT * FROM users WHERE id=(%(id)s);"
        result=connectToMySQL(cls.db).query_db(query,data)
        if len(result)<1:
            return False
        return cls(result[0])


#validation 
    @staticmethod
    def is_valid(user):
        is_valid=True
        query="SELECT * FROM users WHERE email= %(email)s;"
        result=connectToMySQL(User.db).query_db(query,user)
        print(result)
        if len(result)>=1:
            flash("* email adress is already token","Register")
            is_valid=False
        if not EMAIL_REGEX.match(user['email']):
            flash("* Invalid email adress","Register")
            is_valid=False
        if len(user['first_name'])<3:
            flash("first name at least be 3 characters","Register")
            is_valid=False
        if len(user['last_name'])<3:
            flash("last name at least be 3 characters","Register")
            is_valid=False
        if len(user['email'])<8:
            flash("email at least be 8 characters","Register")
            is_valid=False
        if len(user['password'])<8:
            flash("password at least be 8 characters","Register")
            is_valid=False
        if (user['password'])!=(user['confirm_password']):
            flash("confirm password doesn't much with password","Register")
            is_valid=False
        return is_valid