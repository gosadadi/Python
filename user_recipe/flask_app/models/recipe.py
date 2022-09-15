from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app.models.user import User


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
        self.poster = None

    @classmethod
    def save(cls, data):
        query = "INSERT INTO recipes (name,description,instructions,under_thirty,created_at,updated_at,user_id) VALUES (%(name)s,%(description)s,%(instructions)s,%(under_thirty)s,%(created_at)s,NOW(),%(user_id)s);"
        recipe_id = connectToMySQL('user_recipe').query_db(query, data)
        return recipe_id

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM user_recipe.recipes LEFT JOIN user_recipe.users ON users.id=recipes.user_id;"
        results = connectToMySQL('user_recipe').query_db(query)

        recipes = []
        for recipe in results:
            all_recipes = cls(recipe)
            poster_data = {
                'id': recipe['users.id'],
                'first_name': recipe['first_name'],
                'last_name': recipe['last_name'],
                'email': recipe['email'],
                'password': recipe['password'],
                'created_at': recipe['created_at'],
                'updated_at': recipe['updated_at']
            }
            all_recipes.poster = User(poster_data)
            recipes.append(all_recipes)
        return recipes

    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM recipes LEFT JOIN users on users.id= recipes.user_id WHERE recipes.id = %(id)s;"
        results = connectToMySQL('user_recipe').query_db(query, data)
        if len(results) < 1:
            return False
        one_instance = cls(results[0])
        one_data = {
            'id': results[0]['users.id'],
            'first_name': results[0]['first_name'],
            'last_name': results[0]['last_name'],
            'email': results[0]['email'],
            'password': results[0]['password'],
            'created_at': results[0]['created_at'],
            'updated_at': results[0]['updated_at']
        }
        one_instance.poster = User(one_data)

        return one_instance

    @classmethod
    def update(cls, data):
        query = "UPDATE recipes SET name=%(name)s,description=%(description)s,instructions=%(instructions)s, under_thirty=%(under_thirty)s,updated_at = NOW(),user_id=%(user_id)s WHERE id = %(id)s;"
        return connectToMySQL('user_recipe').query_db(query, data)

        # query = "UPDATE recipes SET name,description, instructions,under_thirty,update_at,user_id=%(name)s,%(description)s,%(instructions)s,%(under_thirty)s,NOW(),%(user_id)s WHERE recipes.id = %(id)s;"
        # return connectToMySQL('user_recipe').query_db(query, data)

    @classmethod
    def destroy(cls, data):
        query = "DELETE FROM recipes WHERE id = %(id)s;"
        return connectToMySQL('user_recipe').query_db(query, data)

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
