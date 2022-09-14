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
    
    return render_template("show.html", logged_user= logged_user, all_recipe=Recipe.get_all())


@app.route('/recipes/new')
def recipes_new():

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


@app.route('/recipes/<int:recipe_id>')
def view_one(recipe_id):

    data = {
        'id': recipe_id
    }

    return render_template("show_one_recipe.html", one_recipe=Recipe.get_one(data))


@app.route('/update/recipe')
def update_recipe():
    
    
    return render_template("update_recipe_form.html") 


@app.route('/update/<int:recipe_id>', methods=['POST'])
def update(recipe_id):
    is_valid = Recipe.validate_recipe(request.form)
    if not is_valid:
        flash("please fill out all required form")
        return render_template("recipe_form.html")
    
    
    data = {
        'id': recipe_id,
        "name": request.form['name'],
        "description": request.form['description'],
        "instructions": request.form['instructions'],
        "under_thirty":request.form["under_thirty"],
        "user_id": session['user_id']
    }
    Recipe.update(data)
    return redirect(f"/recipes/{recipe_id}")

