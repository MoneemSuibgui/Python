from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

class Recipe:
    
    db="recipes_schema"

    def __init__(self,data):
        self.id=data['id']
        self.name=data['name']
        self.description=data['description']
        self.instruction=data['instruction']
        self.date_made=data['date_made']
        self.user_id=data['user_id']
        self.under_30=data['under_30']
        self.created_at=data['created_at']
        self.updated_at=data['updated_at']

#create recipe
    @classmethod
    def save_recipe(cls,data):
        query="INSERT INTO recipes (name,description,instruction,user_id,date_made,under_30) VALUES (%(name)s,%(description)s,%(instruction)s,%(user_id)s,%(date_made)s,%(under_30)s);"
        return connectToMySQL(cls.db).query_db(query,data)
    
    
# get all recepies
    @classmethod
    def get_all_recipes(cls):
        query="SELECT* FROM recipes"
        result=connectToMySQL(cls.db).query_db(query)
        recipes=[]
        for recipe in result:
            recipes.append(cls(recipe))
            print(recipe['name'])
            print(recipes)
        return recipes

# get one recipes by id
    @classmethod
    def get_one_recipe(cls,data):
        query="SELECT * FROM recipes WHERE id=(%(id)s);"
        result=connectToMySQL(cls.db).query_db(query,data)
        return cls(result[0])

# update one recipe
    @classmethod
    def update_one_recipe(cls,data):
        query=" UPDATE  recipes SET name=%(name)s,description=%(description)s,instruction=%(instruction)s,date_made=%(date_made)s,under_30=%(under_30)s,updated_at=now() WHERE id=%(id)s ;"
        return connectToMySQL(cls.db).query_db(query,data)

# delete one recipe
    @classmethod
    def destroy_one(cls,data):
        query="DELETE FROM recipes WHERE id=%(id)s;"
        return connectToMySQL(cls.db).query_db(query,data)
    
    
# validation recipe
    @staticmethod
    def validate_recipe(recipe):
        is_valid=True
        if len(recipe['name'])<3:
            flash("* Name a least be 4 characters","create_recipes")
            flash("* Name a least be 4 characters","edit")
            is_valid=False
        if len(recipe['description'])<8:
            flash("* Description at  least be 9 charcters","create_recipes")
            flash("* Description at  least be 9 charcters","edit")
            is_valid=False
        if len(recipe['instruction'])<8:
            flash("* Instruction at  least be 9 charcters","create_recipes")
            flash("* Instruction at  least be 9 charcters","edit")
            is_valid=False
        if recipe['date_made']=="":
            flash("* You must choose the date","create_recipes")
            flash("* You must choose the date","edit")
            is_valid=False
        # if recipe['under_30']=="":
        #     flash("* You must select under 30 minutes Yes or No?","create_recipes")
        #     is_valid=False
        return is_valid