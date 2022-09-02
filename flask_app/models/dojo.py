from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import ninja

class Dojo:
    db = 'dojosandninjas' # make a variable to use in the result variable that uses the database's name instead of typing out 'dojosandninjas' each time

    def __init__(self, data): # constructor method to make the database key info to be accessable by the templates
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.ninjas = []

    @classmethod
    def save(cls, data): #this is a method to save a new dojo information into our database
        query = "INSERT INTO dojos (name) VALUES (%(name)s);" # inserts new key values from the form into our database
        result = connectToMySQL(cls.db).query_db(query, data)
        return result

    @classmethod
    def get_all(cls): # this is a method to get all of the information from each table about a dojo
        query = "SELECT * FROM dojos;"
        results = connectToMySQL(cls.db).query_db(query)
        dojos = []
        for i in results:
            dojos.append(cls(i)) # this combines all the table info into one list
        return dojos

    @classmethod
    def get_one_with_ninjas(cls, data):
        query = "SELECT * FROM dojos LEFT JOIN ninjas ON dojos.id = ninjas.dojos_id WHERE dojos.id = %(id)s;"
        results = connectToMySQL(cls.db).query_db(query, data)
        one_dojo = cls(results[0])
        for one_ninja in results:
            if  one_ninja['ninjas.id'] == None:
                break
            data = {
                'id': one_ninja['ninjas.id'],
                'first_name': one_ninja['first_name'],
                'last_name': one_ninja['last_name'],
                'age': one_ninja['age'],
                'created_at': one_ninja['created_at'],
                'updated_at': one_ninja['updated_at']
            }
            ninja_obj = ninja.Ninja(data)
            one_dojo.ninjas.append(ninja_obj)
        return one_dojo