from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app.models.user import User

class Sight:
    
    db="mydb_schema"
    def __init__(self,data):
        self.id=data['id']
        self.user_id=data['user_id']
        self.location=data['location']
        self.content=data['content']
        self.date_sight=data['date_sight']
        self.number_s=data['number_s']
        self.created_at=data['created_at']
        self.updated_at=data['updated_at']
        self.poster=None
    


# create sight
    @classmethod
    def save_sight(cls,data):
        query="""
        INSERT INTO sightings 
        (user_id,location,content,date_sight,number_s,created_at)
        VALUES (%(user_id)s,%(location)s,%(content)s,%(date_sight)s,%(number_s)s,NOW())
        """
        return connectToMySQL(cls.db).query_db(query,data)
    
# get all sightings
    @classmethod
    def get_all_sightings(cls):
        query = """
            SELECT * FROM sightings JOIN users ON sightings.user_id = users.id; 
        """
        results = connectToMySQL(cls.db).query_db(query)
        sightings = []
        for row in results:
            sight = cls(row)
            poster_data={
                'id':row['users.id'],
                'first_name':row['first_name'],
                'last_name':row['last_name'],
                'email':row['email'],
                'password':'',
                'created_at':row['users.created_at'],
                'updated_at':row['users.updated_at'],
            }
            sight.info=User(poster_data)
            sight.poster = f"{row['first_name']} {row['last_name']}"
            sightings.append(sight)
        return sightings
    

# delete sight
    @classmethod
    def delete_sight(cls,data):
        query="DELETE FROM sightings WHERE id=%(id)s ;"
        return connectToMySQL(cls.db).query_db(query,data)


# get sight by id
    @classmethod
    def get_sight_by_id(cls,data):
        query="SELECT * FROM sightings WHERE id=%(id)s;"
        result=connectToMySQL(cls.db).query_db(query,data)
        return cls(result[0])


# update sight
    @classmethod
    def update_sight(cls,data):
        query="UPDATE sightings SET location=%(location)s,content=%(content)s,date_sight=%(date_sight)s,number_s=%(number_s)s,updated_at=NOW() WHERE id=%(id)s;"
        return connectToMySQL(cls.db).query_db(query,data)


# get all one sight
    @classmethod
    def get_one_sight(cls,data):
        query = """
            SELECT * FROM sightings JOIN users ON sightings.user_id = users.id WHERE sightings.id=%(id)s; 
        """
        results = connectToMySQL(cls.db).query_db(query,data)
        sighting = cls(results[0])
        sighting.poster=f"{results[0]['first_name']} {results[0]['last_name']}"

        return sighting
    
    @classmethod
    def get_nbr_skiptics(cls,data):
        query="SELECT * FROM sight Where sight.id=%(id)s"
        result=connectToMySQL(cls,data).query_db(query,data)
        nbr=cls(result['nbr_skeptical'])
        return nbr
    
    
#validation of Sight
    @staticmethod
    def valid_sight(sight):
        is_valid=True
        if len(sight['location'])<3:
            flash("* Location must at least be 8 Characters","sight")
            is_valid=False
        if len(sight['content'])<8:
            flash("* content must at least be 8 Characters","sight")
            is_valid=False
        if len(sight['number_s'])==0:
            flash("* Number Sasquatch must more than 0 ","sight")
            is_valid=False
        if (sight['date_sight'])=="":
            flash("* date_sight mustn't be empty","sight")
            is_valid=False
        return is_valid
    
    
