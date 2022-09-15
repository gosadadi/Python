from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.recipe import Recipe
from flask_app.models.user import User


@app.route("/recipes")
def home_page():
    if 'user_id' not in session:
        return redirect('/')
    data = {
        "id": session['user_id']
    }

    logged_user = User.get_one(data)

    return render_template("show.html", logged_user=logged_user, all_recipe=Recipe.get_all())


@app.route('/recipes/new')
def recipe_new():

    return render_template("recipe_form.html")


@app.route('/create/recipes', methods=['POST'])
def create_recipes():
    is_valid = Recipe.validate_recipe(request.form)
    if not is_valid:
        flash("please fill out all required form")
        return render_template("recipe_form.html")

    data = {
        "name": request.form['name'],
        "description": request.form['description'],
        "instructions": request.form['instructions'],
        "under_thirty": request.form['under_thirty'],
        "created_at": request.form['created_at'],
        "user_id": session['user_id']
    }

    new_recipe = Recipe.save(data)
    return redirect('/recipes')


@app.route('/recipes/<int:id>')
def view_one(id):

    data = {
        'id': id
    }
    user= {
        "id": session['user_id']
    }

    logged_user = User.get_one(user)

    return render_template("show_one_recipe.html", one_recipe=Recipe.get_one(data), logged_user=User.get_one(user))


@app.route('/edit_recipe/<int:id>')
def edit_page(id):
    data = {
        'id': id
    }
    one_recipe = Recipe.get_one(data)
    return render_template("update_recipe.html", one_recipe=one_recipe)


@app.route('/update/<int:id>', methods=['POST'])
def update(id):
    is_valid = Recipe.validate_recipe(request.form)
    if not is_valid:
        flash("please fill out all required form")
        return render_template("recipe_form.html")

    data = {
        'id': id,
        "name": request.form['name'],
        "description": request.form['description'],
        "instructions": request.form['instructions'],
        "under_thirty": request.form["under_thirty"],
        "user_id": session['user_id']
    }
    Recipe.update(data)
    return redirect("/recipes")


@app.route('/delete/<int:id>')
def delete(id):
    data = {
        'id': id,
    }
    Recipe.destroy(data)
    return redirect('/recipes')
