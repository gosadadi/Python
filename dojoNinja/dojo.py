from mysqlconnection import connectToMySQL
class Dojo:
    def __init__( self , data ):
        self.name = data['name']
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM Dojos;"
        print(query)
        results = connectToMySQL('dojo_ninja').query_db(query)
        print(results)
        dojos = []
        for dojo in results:
            dojos.append( cls(dojo) )
        return dojos
    @classmethod
    def save(cls, data ):
        query = "INSERT INTO Dojos( name, created_at, updated_at ) VALUES ( %(name)s, NOW() , NOW());"
        print(query)
        return connectToMySQL('dojo_ninja').query_db( query, data )
