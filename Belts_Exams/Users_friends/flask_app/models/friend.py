from flask_app.config.mysqlconnection import  connectToMySQL
from flask_app.models.user import User


class Friend:
    db="users_freinds_shema"
    def __init__(self,data):
        self.id=data['id']
        self.user_id=data['user_id']
        self.friend_id=data['friend_id']
        self.email=data['email']
        self.created_at=data['created_at']
        self.updated_at=data['updated_at']

# create friend
    @classmethod
    def create_friend(cls,data):
        query="INSERT INTO friends(user_id,friend_id,created_at) VALUES (%(user_id)s,%(friend_id)s,NOW()) ;"
        return connectToMySQL(cls.db).query_db(query,data)
        
        
        
# get all friends of logged_ in_user
    @classmethod
    def get_all_friends(cls,data):
        query="""
        SELECT* FROM friends 
        LEFT JOIN users AS friend ON friend.id=friends.friend_id
        WHERE friends.user_id=%(id)s
        """
        result=connectToMySQL(cls.db).query_db(query,data)
        friends_list=[]
        for row in result:
            
            friend_data={
                'id':row['friend.id'],
                'name':row['name'],
                'alias':row['alias'],
                'email':row['email'],
                'password':'',
                'date_birthday':row['date_birthday'],
                'created_at':row['friend.created_at'],
                'updated_at':row['friend.updated_at'],
            }
            friends_list.append(User(friend_data))
            print(friends_list)
        return friends_list
    
    

# get all friends of logged_ in_user
    @classmethod
    def get_all_unfriends(cls,data):
        query="""
        SELECT * FROM users WHERE users.id NOT IN (SELECT friends.friend_id FROM friends WHERE user_id=%(id)s);
        """
        result=connectToMySQL(cls.db).query_db(query,data)
        users_list=[]
        for row in result:
            
            friend_data={
                'id':row['id'],
                'name':row['name'],
                'alias':row['alias'],
                'email':row['email'],
                'password':'',
                'date_birthday':row['date_birthday'],
                'created_at':row['created_at'],
                'updated_at':row['updated_at'],
            }
            users_list.append(User(friend_data))
            print(users_list)
        return users_list

# delete friend
    @classmethod
    def delete_friend(cls,data):
        query="DELETE FROM friends WHERE user_id=%(user_id)s AND friend_id=%(friend_id)s;"
        return connectToMySQL(cls.db).query_db(query,data)
