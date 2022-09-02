from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.dojo import Dojo # this imports the dojo class from the dojos.py file inside the models folder

@app.route('/') # default route
def index():
    return redirect('/dojos')

@app.route('/dojos') # main page
def dojos_main_page():
    dojos = Dojo.get_all()
    return render_template("dojos.html", dojos=dojos) # dojos variable has access to all the table data on the dojos

@app.route('/dojo/create', methods=['POST']) # route that submits the info from the form on the dojos.html page
def create_dojo():
    print(request.form)
    data ={
        'name': request.form['dojo_name']
    }
    Dojo.save(data) # saves new dojo with the data from the form
    return redirect('/dojos')

@app.route('/dojos/<int:id>') # route to show dojos info
def show_dojo(id):
    data = {
        "id": id
    } # this "data" dict makes it possible to use the dojo id key on the html page and on the route address
    a_dojo = Dojo.get_one_with_ninjas(data)
    return render_template("one_dojo.html", one_dojo=a_dojo) # dojo variable allows html page to use the keys based on one dojos id