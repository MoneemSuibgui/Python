from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash




class Pie:
    db="pypies_users_schema"
    def __init__(self,data):
        self.id=data['id']
        self.name=data['name']
        self.filling=data['filling']
        self.crust=data['crust']
        self.user_id=data['user_id']
        self.created_at=data['created_at']
        self.updated_at=data['updated_at']
    

# create Pypies
    @classmethod
    def save_pie(cls,data):
        query="INSERT INTO pypies (name,filling,crust,user_id,created_at) VALUES (%(name)s,%(filling)s,%(crust)s,%(user_id)s,now()) ;"
        return connectToMySQL(cls.db).query_db(query,data)

# get all Pypies
    @classmethod
    def get_pypies_of_user(cls,data):
        query="SELECT * FROM pypies WHERE user_id=%(id)s ;"
        results=connectToMySQL(cls.db).query_db(query,data)
        all_pypies=[]
        for row in results:
            all_pypies.append(cls(row))
            print(all_pypies)
        return all_pypies

# delete pypie
    @classmethod
    def destroy_pypie(cls,data):
        query=" DELETE FROM pypies WHERE id=%(id)s AND user_id=%(user_id)s;"
        return connectToMySQL(cls.db).query_db(query,data)
    
# get one pypie by id
    @classmethod
    def get_pypie_by_id(cls,data):
        query="SELECT * FROM pypies WHERE id=%(id)s ;"
        result=connectToMySQL(cls.db).query_db(query,data)
        return cls(result[0])

# update pypie
    @classmethod
    def update_pypie(cls,data):
        query=" UPDATE pypies SET  name=%(name)s,filling=%(filling)s,crust=%(crust)s,updated_at=NOW() WHERE id=%(id)s;"
        return connectToMySQL(cls.db).query_db(query,data)
    
# get all pypies
    @classmethod
    def get_all_pypies(cls):
        query="""
        SELECT pypies.id, pypies.name,	users.first_name AS user_f_name,users.last_name AS user_l_name
        ,count(votes.id) as nbr_votes FROM pypies
        LEFT JOIN users ON users.id=pypies.user_id
        LEFT JOIN votes on votes.pypie_id=pypies.id GROUP BY pypies.id
        ORDER BY nbr_votes DESC;
        """
        result=connectToMySQL(cls.db).query_db(query)
        all_pypies_info=[]
        for row in result:
            all_pypies_info.append(row)
            # print(all_pypies_info)
        return all_pypies_info
    
            



# validation of pie
    @staticmethod 
    def valid_pie(pie):
        is_valid=True
        if len(pie['name'])<3:
            flash("* Name at least be 3 characters","add_pie")
            is_valid=False
        if len(pie['filling'])<3:
            flash("* Filling at least be 3 characters","add_pie")
            is_valid=False
        if len(pie['crust'])<3:
            flash("* Crust at least be 3 characters","add_pie")
            is_valid=False
        return is_valid

