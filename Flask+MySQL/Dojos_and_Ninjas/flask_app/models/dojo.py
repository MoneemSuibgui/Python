from flask_app.config.mysqlconnection import connectToMySQL
from .ninja import Ninja



class Dojo:
    def __init__(self,data):
        self.id=data['id']
        self.name=data['name']
        self.created_at=data['created_at']
        self.updated_at=data['updated_at']
        self.ninja=[]
        

#create dojo
    @classmethod
    def create_dojo(cls,data):
        query=" INSERT INTO dojos (name) VALUES (%(name)s); "
        return connectToMySQL('dojo_ninja').query_db(query,data)
    
#get all dojos
    @classmethod
    def get_allDojo(cls):
        query="SELECT * FROM dojos"
        result=connectToMySQL('dojo_ninja').query_db(query)
        dojo_info=[]
        for one_dojo in result:
            dojo_info.append(cls(one_dojo))
        return dojo_info

#get all ninjas of one dojo
    @classmethod
    def get_ninjas_dojo(cls,data):
        query="SELECT * FROM dojos LEFT JOIN ninjas ON ninjas.dojos_id=dojos.id WHERE dojos.id=%(id)s;"
        result =connectToMySQL('dojo_ninja').query_db(query,data)
        # print(result)
        dojo=cls(result[0])
        for one_row in result:
            if one_row['ninjas.id']==None:
                break
            ninja_data={
                'id':one_row['ninjas.id'],
                'first_name':one_row['first_name'],
                'last_name':one_row['last_name'],
                'age':one_row['age'],
                'created_at':one_row['ninjas.created_at'],
                'updated_at':one_row['updated_at']
            }
            dojo.ninja.append(Ninja(ninja_data))
            # print(dojo)
        return dojo