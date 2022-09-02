from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.dojo import Dojo # this imports the Ninja class from the Ninjas.py file inside the models folder
from flask_app.models.ninja import Ninja

@app.route('/')
def ninja_main():
    return render_template('dojos.html')

@app.route('/new_ninja')
def new_ninja():
    dojos = Dojo.get_all()
    return render_template('new_ninja.html', dojos=dojos)

@app.route('/ninja/create', methods=['POST']) # route that submits the info from the form on the new_Ninjas.html page
def create_ninja():
    print(request.form)
    Ninja.save(request.form) # saves new Ninja and their info from the form
    return redirect('/')