from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import dojo

class Ninja:
    db = 'dojosandninjas' # make a variable to use in the result variable that uses the database's name instead of typing out 'dojosandninjas' each time

    def __init__(self, data): # constructor method to make the database key info to be accessable by the templates
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.dojos_id = None

    @classmethod
    def save(cls, data): #this is a method to save a new ninja information into our database
        query = "INSERT INTO ninjas (first_name, last_name, age, dojos_id) VALUES (%(first_name)s, %(last_name)s, %(age)s, %(dojos_id)s);" # inserts new key values from the form into our database
        result = connectToMySQL(cls.db).query_db(query, data)
        print(result)
        return result
