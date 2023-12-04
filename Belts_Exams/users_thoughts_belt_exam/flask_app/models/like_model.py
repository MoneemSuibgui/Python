from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import db

class Like:
    
    def __init__(self,data):
        self.id:data['id']
        self.user_id:data['user_id']
        self.thought_id:data['thought_id']
        self.created_at:data['created_at']
        self.updated_at:data['updated_at']


# create like
    @classmethod
    def save_like(cls,data):
        query="INSERT INTO likes (user_id,thought_id,created_at) VALUES (%(user_id)s,%(thought_id)s,NOW());"
        return connectToMySQL(db).query_db(query,data)

# delete like
    @classmethod
    def delete_like(cls,data):
        query="DELETE FROM likes WHERE user_id=%(user_id)s AND thought_id=%(thought_id)s;"
        return connectToMySQL(db).query_db(query,data)

# get all thought id's likes by logged in user
    @classmethod
    def like_list(cls,data):
        query="""
        SELECT thoughts.id FROM thoughts
        JOIN likes on thoughts.id=likes.thought_id
        WHERE likes.user_id=%(id)s;
        """
        result=connectToMySQL(db).query_db(query,data)
        likes=[]
        for row in result:
            likes.append(row['id'])
            # print(likes)
        return likes




