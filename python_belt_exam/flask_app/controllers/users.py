from flask import render_template, request, redirect, flash, session
from flask_app import app
import re
from flask_app.models.user import User
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
    print(this_user.id)
    
    return redirect('/recipes')


@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')
