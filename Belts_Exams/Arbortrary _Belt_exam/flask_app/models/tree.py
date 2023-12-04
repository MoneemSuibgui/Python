from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash





class Tree:
    db="users_plants_db"
    def __init__(self,data):
        self.id=data['id']
        self.user_id=data['user_id']
        self.spicies=data['spicies']
        self.location=data['location']
        self.reason=data['reason']
        self.date_planted=data['date_planted']
        self.created_at=data['created_at']
        self.updated_at=data['updated_at']
        
        
        
# create user
    @classmethod
    def save_tree(cls,data):
        query="INSERT INTO trees (user_id,spicies,location,reason,date_planted,created_at) VALUES (%(user_id)s,%(spicies)s,%(location)s,%(reason)s,now(),now()) ;"
        return connectToMySQL(cls.db).query_db(query,data)

# get all trees
    @classmethod
    def get_all_trees(cls):
        query="""
        SELECT trees.id,trees.spicies,users.first_name AS user_f_name,
        users.last_name AS user_l_name, count(visits.id) as nbr_visitors FROM trees 
        LEFT JOIN users ON users.id=trees.user_id
        LEFT JOIN visits ON visits.tree_id=trees.id
        GROUP BY trees.id ORDER BY nbr_visitors desc
        """
        result=connectToMySQL(cls.db).query_db(query)
        all_trees=[]
        for row in result:
            all_trees.append(row)
        return all_trees

# get tree by id
    @classmethod
    def get_tree_by_id(cls,data):
        query="SELECT * FROM trees WHERE id=%(id)s;"
        result=connectToMySQL(cls.db).query_db(query,data)
        return cls(result[0])
    
# get my trees
    @classmethod
    def get_my_trees(cls,data):
        query="SELECT * FROM trees WHERE user_id=%(id)s;"
        results=connectToMySQL(cls.db).query_db(query,data)
        my_trees=[]
        for row in results:
            my_trees.append(row)
        return my_trees


# delete tree
    @classmethod
    def delete_tree(cls,data):
        query="DELETE FROM trees WHERE id=%(id)s AND user_id=%(user_id)s ;"
        return connectToMySQL(cls.db).query_db(query,data)


# update show
    @classmethod
    def update_tree(cls,data):
        query="UPDATE trees SET spicies=%(spicies)s,location=%(location)s,reason=%(reason)s,date_planted=%(date_planted)s,updated_at=NOW() WHERE id=%(id)s;"
        return connectToMySQL(cls.db).query_db(query,data)

# get tree info
    @classmethod
    def get_tree_by_id(cls,data):
        query="""
        SELECT users.first_name,users.last_name,
        trees.spicies,trees.location,trees.date_planted
        ,trees.id,trees.reason
        FROM users_plants_db.trees LEFT JOIN users 
        ON users.id=trees.user_id
        WHERE trees.id=%(id)s;
        """
        result=connectToMySQL(cls.db).query_db(query,data)
        return (result[0])


# validations

    @staticmethod 
    def valid_plant(tree):
        is_valid=True
        if len(tree['spicies'])<3:
            flash("* Spicies at least be 3 characters","tree")
            is_valid=False
        if len(tree['location'])<3:
            flash("* Location at least be 3 characters","tree")
            is_valid=False
        if len(tree['reason'])<3:
            flash("* Reason at least be 3 characters","tree")
            is_valid=False
        if tree['date_planted']=="":
            flash("* Enter the date planted ","tree")
            is_valid=False
        return is_valid