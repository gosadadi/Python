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
        "email": request.form["email"],
        "password": bcrypt.generate_password_hash(request.form["password"]),
    }
    user_id= User.save(user_data)
    if not user_id:
        flash("Email already taken.", "register")
        return redirect('/')
    session['user_id'] = user_id
    return redirect('/shows')


@app.route("/login", methods=['POST'])
def login():
    data = {
        "email": request.form['email']
    }
    print("this is trying to get the user")
    this_user = User.get_by_email(data)
    if not this_user:
        flash("Invalid Email/Password", "login")
        return redirect("/")
    if not bcrypt.check_password_hash(this_user.password, request.form['password']):
        print("wrong password")
        flash("Invalid Email/Password", "login")
        return redirect("/")
    session['user_id'] = this_user.id
    return redirect('/shows')


@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')
