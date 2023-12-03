from flask_app.config.mysqlconnection import connectToMySQL



class Vote:
    db="pypies_users_schema"
    def __init__(self,data):
        self.id=data['id']
        self.pypie_id=data['pypie_id']
        self.user_id=data['user_id']
        self.created_at=data['created_at']
        self.updated_at=data['updated_at']


# create vote
    @classmethod
    def create_vote(cls,data):
        query="INSERT INTO votes (pypie_id,user_id,created_at) VALUES (%(pypie_id)s,%(user_id)s,NOW());"
        return connectToMySQL(cls.db).query_db(query,data)

# delete vote
    @classmethod
    def delete_vote(cls,data):
        query="DELETE FROM votes WHERE user_id=%(user_id)s AND pypie_id=%(pypie_id)s ;"
        return connectToMySQL(cls.db).query_db(query,data)
    
    
# get id's of votes of one pypies
    @classmethod
    def get_votes_list_one_pypie(cls,data):
        query="SELECT pypie_id FROM votes WHERE pypie_id=%(pypie_id)s AND user_id=%(user_id)s;"
        result=connectToMySQL(cls.db).query_db(query,data)
        if len(result)<1:
            return False
        return result[0]