from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash


class Dojo:
    def __init__(self,data):
        self.name=data['name']
        self.location=data['location']
        self.favorite_language=data['favorite_language']
        self.comment=data['comment']
        self.created_at=data['created_at']
        self.updated_at=data['updated_at']
        
        
        
        
#create dojo
    @classmethod
    def create_dojo(cls,data):
        query="""INSERT INTO dojos (name,location,favorite_language,comment,created_at,updated_at)
        VALUES (%(name)s,%(location)s,%(favorite_language)s,%(comment)s,now(),now());
        """
        return connectToMySQL('dojo_survey_schema').query_db(query,data)




# validation form
    @staticmethod
    def validate_dojo(dojo):
        is_valid=True
        if len(dojo['name'])<3:
            flash("* Name must be at least 3 caracter")
            is_valid=False
        if len(dojo['location'])<3:
            flash("* location must be at least 3 caracter")
            is_valid=False
        if len(dojo['favorite_language'])<3:
            flash("* favorite_language' must be at least 3 caracter")
            is_valid=False
        if len(dojo['comment'])<3:
            flash("* Comments must be at least 3 caracter")
            is_valid=False
        return is_valid
