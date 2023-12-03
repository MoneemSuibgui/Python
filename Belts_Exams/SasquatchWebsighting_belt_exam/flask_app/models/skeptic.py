from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.user import User


class Skeptic:
    
    db="mydb_schema"

    def __init__(self,data):
        self.id=data['id']
        self.user_id=data['user_id']
        self.sight_id=data['sight_id']
        self.created_at=data['created_at']
        self.updated_at=data['updated_at']


    
# create user
    @classmethod
    def save_skeptics(cls,data):
        query="INSERT INTO skeptics (user_id,sight_id,created_at) VALUES (%(user_id)s,%(sight_id)s,now()) ;"
        return connectToMySQL(cls.db).query_db(query,data)
    
# get all skeptic for one sight
    @classmethod
    def get_all_skiptics_one_sight(cls,data):
        query = """
            SELECT * FROM skeptics JOIN users
            ON users.id=skeptics.user_id 
            Join sightings on sightings.id=skeptics.sight_id 
            Where sightings.id=%(id)s;"""
        results = connectToMySQL(cls.db).query_db(query,data)
        all_skeptics=[]
        for row in results:
            skeptic_data=User(row)
            all_skeptics.append(skeptic_data) 
        return all_skeptics

    
    @classmethod
    def delete_skeptic(cls,data):
        query="DELETE FROM skeptics WHERE sight_id=%(sight_id)s  AND user_id=%(user_id)s;"
        return connectToMySQL(cls.db).query_db(query,data)
    

    # display number of skiptics
    @classmethod
    def count_skiptics(cls,data):
        query="SELECT count(skeptics.id) AS nbr  FROM skeptics WHERE skeptics.sight_id=%(id)s;"
        result=connectToMySQL(cls.db).query_db(query,data)
        nbr=result[0]['nbr']
        print(result)
        return nbr

    
    
    @classmethod
    def get_lsit_skeptics_one_sight(cls,data):
        query = "SELECT user_id FROM  skeptics WHERE sight_id=%(id)s;"
        result = connectToMySQL(cls.db).query_db(query, data)
        list_ids=[]
        
        for row in result:
            list_ids.append(row['user_id'])
        print(list_ids)
        return list_ids
    

# display number of skiptics into dashboard
    @classmethod
    def count_skipticals_in_dashboard(cls):
        query="""
        select sightings.id,count(skeptics.id) AS nbr_skeptics from sightings
        left join skeptics on skeptics.sight_id=sightings.id
        group by sightings.id;
        """
        result=connectToMySQL(cls.db).query_db(query)
        list_nbrs_skepticals=[]
        for row in result:
            list_nbrs_skepticals.append(row)
            print("-"*30)
            print(list_nbrs_skepticals)
        return list_nbrs_skepticals
        
        