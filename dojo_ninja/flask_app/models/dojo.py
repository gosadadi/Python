from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.ninja import Ninja
class Dojo:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.ninjas=None

    @classmethod
    def save(cls, data):
        query = "INSERT INTO dojos (dojo_id, name , created_at , updated_at ) VALUES (%(name)s,NOW(),NOW());"
        return connectToMySQL('dojo_ninja').query_db(query,data)


    @classmethod
    def get_all(cls):
        query = "SELECT * FROM dojos;"
        results = connectToMySQL('dojo_ninja').query_db(query)
        dojos= []
        for dojo in results:
            dojos.append( cls(dojo) )
        return dojos

    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM dojos LEFT JOIN ninjas ON dojos.id=ninjas.dojo_id WHERE dojos.id = %(id)s;"
        results = connectToMySQL('dojo_ninja').query_db(query, data)
        single_dojo = cls(results[0])
        for result in results:
            ninja_data = {
                "id" : result["ninjas.id"],
                "dojo_id" : result["dojo_id"],
                "first_name" : result["first_name"],
                "last_name" : result["last_name"],
                "age" : result["age"],
                "created_at" : result["ninjas.created_at"],
                "updated_at" : result["ninjas.updated_at"]
            } 
        single_dojo.ninjas=Ninja(ninja_data)
        return single_dojo












#     @classmethod
#     def get_restaurant_with_burgers( cls , data ):
#         query = "SELECT * FROM restaurants LEFT JOIN burgers ON burgers.restaurant_id = restaurants.id WHERE restaurants.id = %(id)s;"
        
#         results = connectToMySQL('burgers').query_db( query , data )
#         print(results)
#         restaurant = cls( results[0] )
#         for result in results:
#             burger_data = {
#                 "id" : result["burgers.id"],
#                 "name" :result["burgers.name"],
#                 "bun" : result["bun"],
#                 "meat" : result["meat"],
#                 "calories" : result["calories"],
#                 "created_at" : result["burgers.created_at"],
#                 "updated_at" : result["burgers.updated_at"]
#             }
#         restaurant.burgers.append( burger.Burger( burger_data ) )
#         return restaurant


