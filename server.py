from flask_app import app
from flask_app.controllers import dojos, ninjas
# imports the users and ninjas file content from the controllers folder

if __name__ == "__main__":
    app.run(debug=True)