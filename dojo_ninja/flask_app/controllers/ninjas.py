from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.dojo import Dojo
from flask_app.models.ninja import Ninja


@app.route('/')
def index():
    return redirect("/dojos")

@app.route('/dojos')
def dojo_form():
    return render_template("dojo_form.html")


@app.route('/create/dojo', methods=['POST'])
def create_dojo():
    data = {
        "name": request.form["name"]
        
    }
    Dojo.save(data)
    return redirect('/all/dojo')


@app.route('/all/dojo' )
def all_dojos():
    return render_template("dojo_form.html", all_dojos =Dojo.get_all())


@app.route('/show/<int:id>')
def detail_page(id):
    data = {
        'id':id
    }
    return render_template("details_page.html", dojo=Dojo.get_one(data))




# ninja below

@app.route('/ninjas')
def ninja_form():
    
    return render_template("ninja_form.html",all_dojos =Dojo.get_all())


@app.route('/create/ninja', methods=['POST'])
def create_ninja():
    data = {
        "dojo_id":request.form['dojo_id'],
        "first_name": request.form['first_name'],
        "last_name": request.form['last_name'],
        "age": request.form['age'],
        
    }
    Ninja.save(data)
    return redirect('/dojos')











# @app.route('/all/ninjas' )
# def all_ninjas():
    
#     return render_template("details_page.html", all_dojos =Dojo.get_all())




# @app.route('/edit_page/<int:burger_id>')
# def edit_page(burger_id):
#     data = {
#         'id': burger_id
#     }
#     return render_template("edit_page.html", burger=Burger.get_one(data))


# @app.route('/update/<int:burger_id>', methods=['POST'])
# def update(burger_id):
#     data = {
#         'id': burger_id,
#         "name": request.form['name'],
#         "bun": request.form['bun'],
#         "meat": request.form['meat'],
#         "calories": request.form['calories']
#     }
#     Burger.update(data)
#     return redirect(f"/show/{burger_id}")


# @app.route('/delete/<int:burger_id>')
# def delete(burger_id):
#     data = {
#         'id': burger_id,
#     }
#     Burger.destroy(data)
#     return redirect('/burgers')


# @app.route('/restaurant')
# def restaurant():
#     return render_template("create_restaurant.html")


# @app.route('/create/restaurant', methods=['POST'])
# def create_restaurant():
#     data = {
#         "name": request.form['name'],

#     }
#     Restaurant.save(data)
#     return redirect('/restaurant')
# @app.route('/restaurant/burger')
# def all_restaurant():
#     all_restaurant=Restaurant.get_restaurant()
#     return render_template("all_restaurant.html",all_restaurant=all_restaurant)