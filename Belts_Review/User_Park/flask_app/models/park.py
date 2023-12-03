from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from .user  import  User


class Park:
    db="park_schema"
    
    def __init__(self,data):
        self.id=data['id']
        self.park_name=data['park_name']
        self.city=data['city']
        self.has_playground=data['has_playground']
        self.description=data['description']
        self.description=data['description']
        self.user_id=data['user_id']
        self.created_at=data['created_at']
        self.updated_at=data['updated_at']
        
        
# create a park
    @classmethod
    def save_park(cls,data):
        query="INSERT INTO parks (park_name,city,has_playground,description,user_id) VALUES (%(park_name)s,%(city)s,%(has_playground)s,%(description)s,%(user_id)s);"
        return connectToMySQL(cls.db).query_db(query,data)
    

# update a park
    @classmethod
    def update_one_park(cls,data):
        query=" UPDATE parks SET park_name=%(park_name)s,city=%(city)s,has_playground=%(has_playground)s,description=%(description)s WHERE parks.id=%(id)s;"
        return connectToMySQL(cls.db).query_db(query,data)

    
# delete a park
    @classmethod
    def delete_park(cls,data):
        query="DELETE FROM parks WHERE id=%(id)s;"
        return connectToMySQL(cls.db).query_db(query,data)

#get park_info by id
    @classmethod
    def get_park_info_by_id(cls,data):
        query="SELECT * FROM parks LEFT JOIN users ON users.id=parks.user_id WHERE parks.id=%(id)s ; "
        result= connectToMySQL(cls.db).query_db(query,data)
        parks_info=cls(result[0])
        parks_info.owner={
                'first_name':result[0]['first_name'],
                'last_name':result[0]['last_name'],
                'email':result[0]['email']
                }
        return parks_info

# get park by id
    @classmethod
    def get_park_by_id(cls,data):
        query="SELECT * FROM parks WHERE id=%(id)s ;"
        result= connectToMySQL(cls.db).query_db(query,data)
        return cls(result[0])

# get all parks
    @classmethod
    def ge_all_parks(cls):
        query="SELECT * FROM parks LEFT JOIN users ON users.id=parks.user_id"
        result=connectToMySQL(cls.db).query_db(query)
        parks=[]
        for row in result:
            park=cls(row)
            user_info={
                'first_name':row['first_name'],
                'last_name':row['last_name'],
            }
            park.poster=user_info
            parks.append(park)
        return parks

# validate park form
    @staticmethod
    def validate_park(park):
        is_valid=True
        if len(park['park_name'])<3:
            flash("* Park name at least be 3 characters","create_park")
            is_valid=False
        if len(park['city'])<3:
            flash("* City at least be 3 characters","create_park")
            is_valid=False
        if len(park['description'])<8:
            flash("* Description at least be 8 characters","create_park")
            is_valid=False
        # if park['has_playground']== :
        #     flash("* Has Playground must be checked ","create_park")
        #     return False
        return is_valid