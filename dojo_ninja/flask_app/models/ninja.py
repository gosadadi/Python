from flask_app.config.mysqlconnection import connectToMySQL
# from flask_app.models.dojo import Dojo


class Ninja:
    def __init__(self, data):
        self.id = data['id']
        self.dojo_id = data['dojo_id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.dojos =[]
        
        
    @classmethod
    def save(cls, data):
        query = "INSERT INTO ninjas (dojo_id,first_name,last_name,age, created_at,updated_at) VALUES (%(dojo_id)s, %(first_name)s,%(last_name)s,%(age)s, NOW(),NOW());"
        return connectToMySQL('dojo_ninja').query_db(query, data)
    
    
    
    
    
    
    
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM ninjas;"
        results = connectToMySQL('dojo_ninja').query_db(query)
        dojos= []
        for dojo in results:
            dojos.append( cls(dojo) )
        return dojos

        
        
        
        
        
        
        
        # self.bun = data['bun']
        # self.meat = data['meat']
        # self.calories = data['calories']
        # self.restaurant_id = data['restaurant_id']
        # self.created_at = data['created_at']
        # self.updated_at = data['updated_at']
        # self.restaurant = None

#     @classmethod
#     def save(cls, data):
#         query = "INSERT INTO burgers (name,bun,meat,calories,restaurant_id, created_at,updated_at) VALUES (%(name)s,%(bun)s,%(meat)s,%(calories)s,%(restaurant_id)s, NOW(),NOW());"
#         return connectToMySQL('burgers').query_db(query, data)

#     @classmethod
#     def get_all(cls):
#         query = "SELECT * FROM burgers;"
#         results = connectToMySQL('burgers').query_db(query)
#         burgers = []
#         for burger in results:
#             burgers.append(cls(burger))
#         return burgers

#     @classmethod
#     def get_one(cls, data):
#         query = "SELECT * FROM burgers JOIN restaurants ON burgers.restaurant_id=restaurants.id WHERE burgers.id = %(id)s;"
#         results = connectToMySQL('burgers').query_db(query, data)
#         single_burger = cls(results[0])
#         print("this burger")
#         print(single_burger)
#         return single_burger

#     @classmethod
#     def update(cls, data):
#         query = "UPDATE burgers SET name=%(name)s, bun=%(bun)s, meat=%(meat)s, calories=%(calories)s,updated_at = NOW() WHERE id = %(id)s;"
#         return connectToMySQL('burgers').query_db(query, data)

#     @classmethod
#     def destroy(cls, data):
#         query = "DELETE FROM burgers WHERE id = %(id)s;"
#         return connectToMySQL('burgers').query_db(query, data)

