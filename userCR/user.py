from mysqlconnection import connectToMySQL
import re
from flask import flash

class User:
    def __init__( self , data ):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email_address = data['email_address']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM userCR.users;"
        results = connectToMySQL('userCR').query_db(query)
        users = []
        for user in results:
            users.append( cls(user))
        return users
    
    @classmethod
    def save(cls, data ):
        query = "INSERT INTO users( first_name,last_name,email_address, created_at, updated_at ) VALUES ( %(first_name)s,%(last_name)s,%(email_address)s, NOW() , NOW());"
        results=connectToMySQL('userCR').query_db( query, data )
        return results
    
    @staticmethod
    def validate_user( user ):
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        is_valid = True
        if not EMAIL_REGEX.match(user['email']): 
            flash("Invalid email address!")
            is_valid = False
        return is_valid



    