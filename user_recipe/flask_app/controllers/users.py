from flask import render_template, request, redirect, flash, session
from flask_app import app
import re
from flask_app.models.user import User
from flask_app.models.recipe import Recipe
from flask_bcrypt import Bcrypt


bcrypt = Bcrypt(app)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/register', methods=['POST'])
def register():
    is_valid = User.validate_user(request.form)
    if not is_valid:
        return redirect("/")
    user_data = {
        "first_name": request.form["first_name"],
        "last_name": request.form["last_name"],
        "email_address": request.form["email"],
        "password": bcrypt.generate_password_hash(request.form["password"]),
    }
    id = User.save(user_data)
    if not id:
        flash("Email already taken.", "register")
        return redirect('/')
    session['user_id'] = id
    return redirect('/recipes')


@app.route("/login", methods=['POST'])
def login():
    data = {
        "email": request.form['email']
    }
    this_user = User.get_by_email(data)
    if not this_user:
        flash("Invalid Email/Password", "login")
        return redirect("/")
    if not bcrypt.check_password_hash(this_user.password, request.form['password']):
        flash("Invalid Email/Password", "login")
        return redirect("/")
    session['user_id'] = this_user.id
    return redirect('/recipes')


@app.route("/recipes")
def dashboard():
    if 'user_id' not in session:
        return redirect('/')
    data = {
        "id": session['user_id']
    }
    logged_user = User.get_one(data)
    all_recipes=Recipe.get_all()
    print(all_recipes)
    
    return render_template("show.html", logged_user= logged_user,all_recipes=Recipe.get_all())


@app.route('/recipes/new')
def recipes_new():

    return render_template("recipe_form.html")


@app.route('/create/recipes', methods=['POST'])
def create_recipes():
    is_valid = (Recipe).validate_recipe(request.form)
    if not is_valid:
        return redirect("/recipes")

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






@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')
