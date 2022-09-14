from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.user import User
from flask import flash

class Recipe:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.description = data['description']
        self.instructions = data['instructions']
        self.under_thirty = data['under_thirty']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user_id = data['user_id']
        self.users = []

    @staticmethod
    def validate_recipe(recipe):
        is_valid = True
        if len(recipe['name']) < 2:
            is_valid = False
            flash("name must be at least 2 characters.", "register")
        if len(recipe['description']) < 2:
            is_valid = False
            flash("description must be at least 2 characters.", "register")
        if len(recipe['instructions']) < 2:
            is_valid = False
            flash("instructions must be at least 2 characters.", "register")
        return is_valid



    @classmethod
    def save(cls, data):
        query = "INSERT INTO recipes (name,description,instructions,under_thirty,created_at,updated_at,user_id) VALUES (%(name)s,%(description)s,%(instructions)s,%(under_thirty)s,%(created_at)s,NOW(),%(user_id)s);"
        recipe_id= connectToMySQL('user_recipe').query_db(query, data)
        return recipe_id

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM recipes;"
        results = connectToMySQL('user_recipe').query_db(query)

        recipes = []
        for recipe in results:
            recipes.append(cls(recipe))

        return recipes
















