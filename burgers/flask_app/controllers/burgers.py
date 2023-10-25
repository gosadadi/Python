from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.burger import Burger
from flask_app.models.restaurant import Restaurant


@app.route('/')
def index():
    # display form here
    restaurants = Restaurant.get_restaurant()
    return render_template("index.html", all_restaurant=restaurants)


@app.route('/create', methods=['POST'])
def create():
    if not Burger.validate_burger(request.form):
        return redirect('/')
    
    data = {
        "name": request.form['name'],
        "bun": request.form['bun'],
        "meat": request.form['meat'],
        "calories": request.form['calories'],
        'restaurant_id': request.form['restaurant_id']
    }
    
    # Burger.save(request.form)
    # return redirect("/burgers")
    Burger.save(data)
    return redirect('/burgers')

    

@app.route('/burgers')
def burgers():
    return render_template("results.html", all_burgers=Burger.get_all())


@app.route('/show/<int:burger_id>')
def detail_page(burger_id):

    data = {
        'id': burger_id
    }

    return render_template("details_page.html", burger=Burger.get_one(data))


@app.route('/edit_page/<int:burger_id>')
def edit_page(burger_id):
    data = {
        'id': burger_id
    }
    return render_template("edit_page.html", burger=Burger.get_one(data))


@app.route('/update/<int:burger_id>', methods=['POST'])
def update(burger_id):
    data = {
        'id': burger_id,
        "name": request.form['name'],
        "bun": request.form['bun'],
        "meat": request.form['meat'],
        "calories": request.form['calories']
    }
    Burger.update(data)
    return redirect(f"/show/{burger_id}")


@app.route('/delete/<int:burger_id>')
def delete(burger_id):
    data = {
        'id': burger_id,
    }
    Burger.destroy(data)
    return redirect('/burgers')


@app.route('/restaurant')
def restaurant():
    return render_template("create_restaurant.html")


@app.route('/create/restaurant', methods=['POST'])
def create_restaurant():
    data = {
        "name": request.form['name'],

    }
    Restaurant.save(data)
    return redirect('/restaurant')


@app.route('/restaurant/burger')
def all_restaurant():
    all_restaurant = Restaurant.get_restaurant()
    return render_template("all_restaurant.html", all_restaurant=all_restaurant)
