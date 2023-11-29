from flask_app.config.mysqlconnection import connectToMySQL
import re
from flask import flash
EMAIL_REGEX= re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')


class User:
    db="user_schema"
    def __init__(self,dt):
        self.id=dt['id']
        self.email=dt['email']
        self.created_at=dt['created_at']
        self.updated_at=dt['updated_at']
        


#add user email
    @classmethod
    def create_email(cls,data):
        query="INSERT INTO users (email,created_at) VALUES (%(email)s,now()) ;"
        return connectToMySQL(cls.db).query_db(query,data)
    
#get all users info
    @classmethod
    def get_users_info(cls):
        query="SELECT * FROM users"
        result=connectToMySQL(cls.db).query_db(query)
        users=[]
        for user in result:
            users.append(cls(user))
            print(users)
        return users

# delete user
    @classmethod
    def destroy_one_user(cls,data):
        query=" DELETE FROM users WHERE id=%(id)s "
        return connectToMySQL(cls.db).query_db(query,data)
    
    
#validation email
    @staticmethod
    def validate_email(user):
        is_valid=True
        query="SELECT * FROM users WHERE email=%(email)s;"
        result=connectToMySQL(User.db).query_db(query,user)
        print(result)
        if len(result)>=1:
            flash("This Email is already taken")
            is_valid=False
        if not EMAIL_REGEX.match(user['email']):
            flash("* Email is not valid")
            is_valid=False
        return is_valid