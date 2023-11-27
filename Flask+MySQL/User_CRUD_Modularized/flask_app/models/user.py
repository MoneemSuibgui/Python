from flask_app.config.mysqlconnection import connectToMySQL


class User:
    def __init__(self,data):
        self.id=data['id']
        self.first_name=data['first_name']
        self.last_name=data['last_name']
        self.email=data['email']
        self.created_at=data['created_at']
        self.updated_at=data['updated_at']


    def full_name(self):
        return f" {self.first_name} {self.last_name}"

#***********get all users*******
    @classmethod
    def get_all_users(cls):
        query="SELECT * FROM users"
        result=connectToMySQL('user_schema').query_db(query)
        users_list=[]
        for one_user in result:
            users_list.append(cls(one_user))
        return users_list
    
#**********create user***********
    @classmethod
    def save(cls,data):
        query="""
        INSERT INTO users (first_name,last_name,email,created_at)
        VALUES (%(first_name)s,%(last_name)s,%(email)s,now())
        """
        return connectToMySQL('user_schema').query_db(query,data)
    


#**********delete users**********
    @classmethod
    def destroy(cls,data):
        query="DELETE  FROM users WHERE id=%(id)s "
        return connectToMySQL('user_schema').query_db(query,data)


#**********get one_user by id**********
    @classmethod
    def get_by_id(cls,data):
        query=" SELECT * FROM users WHERE id=%(id)s"
        result=connectToMySQL('user_schema').query_db(query,data)
        return cls(result[0])
    
#**********update user*******
    @classmethod
    def update_user(cls,data):
        query="""
        UPDATE users SET first_name=%(first_name)s
        ,last_name=%(last_name)s,email=%(email)s,
        created_at=now() WHERE id=%(id)s;
        """
        return connectToMySQL('user_schema').query_db(query,data)
    

