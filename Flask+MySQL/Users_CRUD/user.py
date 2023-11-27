from mysqlconnection import connectToMySQL

class User:
    def __init__(self,data):
        self.id=data['id']
        self.first_name=data['first_name']
        self.last_name=data['last_name']
        self.email=data['email']
        self.created_at=data['created_at']
        self.updated_at=data['updated_at']
        
        
        
#create user
    @classmethod
    def create_user(cls,data):
        query="""
        INSERT INTO users(first_name,last_name,email,created_at,updated_at)
        VALUES (%(first_name)s,%(last_name)s,%(email)s,now(),now())
        """
        return  connectToMySQL('user').query_db(query,data)
    

# get all users
    @classmethod
    def get_allUsers(cls):
        query="SELECT * FROM users ;"
        result=connectToMySQL('user').query_db(query)
        all_users=[]
        for user in result:
            all_users.append(cls(user))
        return all_users
    

# get user by id
    @classmethod
    def get_user(cls,data):
        query="SELECT * FROM users WHERE (id=%(id)s) ;"
        result=connectToMySQL('user').query_db(query,data)
        return (cls(result[0]))
    
# delete user 
    @classmethod
    def destroy_user(cls,data):
        query="DELETE  FROM users WHERE (id=%(id)s) ;"
        return connectToMySQL('user').query_db(query,data)
    
    
# update user
    @classmethod
    def update_user(cls,data):
        query="UPDATE users SET first_name=%(first_name)s,last_name=%(last_name)s,email=%(email)s,created_at=now(),updated_at=now() WHERE id=%(id)s ;"
        return connectToMySQL('user').query_db(query,data)
    