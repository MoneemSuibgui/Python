from flask_app.config.mysqlconnection import connectToMySQL





class Visit:
    db="users_plants_db"
    def __init__(self,data):
        self.id=data['id']
        self.tree_id=data['tree_id']
        self.user_id=data['user_id']
        self.created_at=data['created_at']
        self.updated_at=data['updated_at']
        
        
    
# create visitor
    @classmethod
    def save_visitor(cls,data):
        query="INSERT INTO visits (tree_id,user_id,created_at) VALUES (%(tree_id)s,%(user_id)s,now()) ;"
        return connectToMySQL(cls.db).query_db(query,data)

# delete visitors
    @classmethod
    def delete_visitor(cls,data):
        query="DELETE FROM visits WHERE tree_id=%(tree_id)s AND user_id=%(user_id)s ;"
        return connectToMySQL(cls.db).query_db(query,data)
    
# get id's of visits of one tree
    @classmethod
    def get_id_visitor_one_tree(cls,data):
        query="SELECT tree_id FROM visits WHERE tree_id=%(tree_id)s AND user_id=%(user_id)s;"
        result=connectToMySQL(cls.db).query_db(query,data)
        if len(result)<1:
            return False
        return result[0]
    
    

# get all visitors of one tree
    @classmethod
    def get_visitors_one_tree(cls,data):
        query="""
        SELECT users.first_name as user_f_name,users.last_name as user_l_name
        FROM users_plants_db.visits
        LEFT JOIN users ON visits.user_id=users.id
        WHERE visits.tree_id=%(id)s;
        """
        result=connectToMySQL(cls.db).query_db(query,data)
        visitors=[]
        for row in result:
            visitors.append(row)
        return visitors
        