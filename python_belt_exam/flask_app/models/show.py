from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app.models.user import User


class Show:
    def __init__(self, data):
        self.id = data['id']
        self.title = data['title']
        self.network = data['network']
        self.release_date = data['release_date']
        self.description = data['description']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user_id = data['user_id']
        self.poster = None

    @classmethod
    def save(cls, data):
        query = "INSERT INTO shows (title,network,release_date,description,created_at,updated_at,user_id) VALUES (%(title)s,%(network)s,%(release_date)s,%(description)s,NOW(),NOW(),%(user_id)s);"
        show_id = connectToMySQL('python_belt').query_db(query, data)
        return show_id

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM python_belt.shows LEFT JOIN python_belt.users ON users.id=shows.user_id;"
        results = connectToMySQL('python_belt').query_db(query)

        shows = []
        for show in results:
            all_shows = cls(show)
            poster_data = {
                'id': show['users.id'],
                'first_name': show['first_name'],
                'last_name': show['last_name'],
                'email': show['email'],
                'password': show['password'],
                'created_at': show['created_at'],
                'updated_at': show['updated_at']
            }
            all_shows.poster = User(poster_data)
            shows.append(all_shows)
        return shows

    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM shows LEFT JOIN users on users.id= shows.user_id WHERE shows.id = %(id)s;"
        results = connectToMySQL('python_belt').query_db(query, data)
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
        query = "UPDATE shows SET title=%(title)s,network=%(network)s,release_date=%(release_date)s, description=%(description)s,user_id=%(user_id)s WHERE shows.id = %(id)s;"
        return connectToMySQL('python_belt').query_db(query, data)

        # query = "UPDATE recipes SET name,description, instructions,under_thirty,update_at,user_id=%(name)s,%(description)s,%(instructions)s,%(under_thirty)s,NOW(),%(user_id)s WHERE recipes.id = %(id)s;"
        # return connectToMySQL('user_recipe').query_db(query, data)

    @classmethod
    def destroy(cls, data):
        query = "DELETE FROM shows WHERE id = %(id)s;"
        return connectToMySQL('python_belt').query_db(query, data)

    @staticmethod
    def validate_show(show):
        is_valid = True
        if len(show['title']) < 3:
            is_valid = False
            flash("name must be at least 3 characters.", "register")
        if len(show['network']) < 3:
            is_valid = False
            flash("network must be at least 3 characters.", "register")   
        if len(show['release_date']) < 6:
            is_valid = False
            flash("Release date must be at least 6 characters.", "register")   
            
        if len(show['description']) < 3:
            is_valid = False
            flash("description must be at least 3 characters.", "register")
        return is_valid
    