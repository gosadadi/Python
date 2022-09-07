from mysqlconnection import connectToMySQL
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
        query = "INSERT INTO users( first_name,last_name,email_addresss, created_at, updated_at ) VALUES ( %(first_name)s,%(last_name)s,%(email_addresss)s) NOW() , NOW());"
        print(query)
        return connectToMySQL('userCR').query_db( query, data )
