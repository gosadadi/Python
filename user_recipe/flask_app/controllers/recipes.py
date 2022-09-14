from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.recipe import Recipe
from flask_app.models.user import User
from flask_app.controllers import users


@app.route("/recipes")
def recipes():
    if 'user_id' not in session:
        return redirect('/')
    data = {
        "id": session['user_id']
    }
    
    logged_user= (user.User).get_one_by_id(data)
    # all_recipe= (recipe.Recipe).get_all()
    
    
    return render_template("show.html",logged_user=logged_user)


@app.route('/recipes/new')
def recipes_new():

    if 'user_id' not in session:
        return redirect('/')
    data = {
        "id": session['user_id']
    }
    users = (user.User).get_one(data)
    return render_template("recipe_form.html", users=users)


@app.route('/create/recipes', methods=['POST'])
def create_recipes():
    is_valid = (recipe.Recipe).validate_recipe(request.form)
    if not is_valid:
        return redirect("/")

    recipe_data = {
        "name": request.form['name'],
        "description": request.form['description'],
        "instructions": request.form['instructions'],
        "under_thirty": request.form['under_thirty'],
        "created_at": request.form['created_at'],
        "user_id": session['user_id']
    }

    new_recipe = Recipe.save(recipe_data)
    print(new_recipe)
    return redirect('/recipes')
