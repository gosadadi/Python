from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import burger
class Restaurant:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.burgers=[]

    @classmethod
    def save(cls, data):
        query = "INSERT INTO restaurants ( name , created_at , updated_at ) VALUES (%(name)s,NOW(),NOW());"
        return connectToMySQL('burgers').query_db(query, data)

    @classmethod
    def get_restaurant(cls):
        query = "SELECT * FROM restaurants;"
        results = connectToMySQL('burgers').query_db(query)
        restaurants= []
        for restaurant in results:
            restaurants.append( cls(restaurant) )
        return restaurants
    

    @classmethod
    def get_restaurant_with_burgers( cls , data ):
        query = "SELECT * FROM restaurants LEFT JOIN burgers ON burgers.restaurant_id = restaurants.id WHERE restaurants.id = %(id)s;"
        
        results = connectToMySQL('burgers').query_db( query , data )
        print(results)
        restaurant = cls( results[0] )
        for result in results:
            burger_data = {
                "id" : result["burgers.id"],
                "name" :result["burgers.name"],
                "bun" : result["bun"],
                "meat" : result["meat"],
                "calories" : result["calories"],
                "created_at" : result["burgers.created_at"],
                "updated_at" : result["burgers.updated_at"]
            }
        restaurant.burgers.append( burger.Burger( burger_data ) )
        return restaurant

