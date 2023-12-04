from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import db
from flask import flash
from flask_app.models.user_model import User



class Thought:
    def __init__(self,data):
        self.id=data['id']
        self.user_id=data['user_id']
        self.content=data['content']
        self.created_at=data['created_at']
        self.updated_at=data['updated_at']
        self.creator=None





# create thought
    @classmethod
    def save_thought(cls,data):
        query="""
        INSERT INTO thoughts (user_id,content,created_at) 
        VALUES (%(user_id)s,%(content)s,NOW());
        """
        return connectToMySQL(db).query_db(query,data)
    
# thought validation
    @staticmethod
    def valid_thought(thought):
        is_valid=True
        if len(thought['content'])<4:
            flash("* Thought must at least be 5 Characters","thought")
            is_valid=False
        return is_valid


# get all thoughts
    @classmethod
    def get_all_thoughts(cls):
        query = """
            SELECT * FROM thoughts JOIN users ON thoughts.user_id = users.id; 
        """
        results = connectToMySQL(db).query_db(query)
        thoughts = []
        for row in results:
            thought = cls(row)
            poster_data={
                'id':row['users.id'],
                'first_name':row['first_name'],
                'last_name':row['last_name'],
                'email':row['email'],
                'password':'',
                'created_at':row['users.created_at'],
                'updated_at':row['users.updated_at'],
            }
            thought.info=User(poster_data)
            thought.poster = f"{row['first_name']} {row['last_name']}"
            thoughts.append(thought)
        return thoughts
    

# get user thoughts
    @classmethod
    def get_user_thoughts(cls,data):
        query = """
        SELECT * FROM users JOIN thoughts ON thoughts.user_id = users.id
        WHERE users.id=%(id)s; 
        """
        result=connectToMySQL(db).query_db(query,data)
        
        all_thoughts=[]
        for row in result:
            
            thought_data={
                'id':row['thoughts.id'],
                'user_id':row['user_id'],
                'content':row['content'],
                'created_at':row['thoughts.created_at'],
                'updated_at':row['thoughts.updated_at'],
            }
            
            all_thoughts.append(thought_data)
        return all_thoughts


# delete one thought
    @classmethod
    def delete_thought(cls,data):
        query="DELETE FROM thoughts WHERE id=%(id)s"
        return connectToMySQL(db).query_db(query,data)



# get nbrs of likes of all thoughts
    @classmethod
    def get_nbrs_likes_all_thoughts(cls):
        query="""
        SELECT thoughts.id AS thought_id,count(likes.id) AS nbr FROM thoughts 
        LEFT JOIN likes ON likes.thought_id=thoughts.id
        GROUP BY thoughts.id;
        """
        result=connectToMySQL(db).query_db(query)
        nbrs_list_of_likes=[]
        for row in result:
            nbrs_list_of_likes.append(row)
            print(nbrs_list_of_likes)
        return nbrs_list_of_likes
        
        