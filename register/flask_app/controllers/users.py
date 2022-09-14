from flask import render_template,request, redirect,flash,session
from flask_app import app
import re
from flask_app.models.user import User
from flask_bcrypt import Bcrypt


bcrypt = Bcrypt(app)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/register',methods=['POST'])
def register():
    is_valid = User.validate_user(request.form)
    if not is_valid:
        return redirect("/")
    user_data = {
        "first_name": request.form["first_name"],
        "last_name": request.form["last_name"],
        "email_address": request.form["email_address"],
        "password": bcrypt.generate_password_hash(request.form["password"]),
    }
    id = User.save(user_data)
    if not id:
        flash("Email already taken.","register")
        return redirect('/')
    session['user_id'] = id
    return redirect('/dashboard')


    
@app.route("/login",methods=['POST'])
def login():
    data = {
        "email_address": request.form['email_address']
    }
    user = User.get_by_email(data)
    if not user:
        flash("Invalid Email/Password","login")
        return redirect("/")
    if not bcrypt.check_password_hash(user.password,request.form['password']):
        flash("Invalid Email/Password","login")
        return redirect("/")
    session['user_id'] = user.id
    return redirect('/dashboard')


    
@app.route("/dashboard")
def dashboard():
    if 'user_id' not in session:
        return redirect('/')
    data = {
        "id": session['user_id']
    }
    user = User.get_one(data)
    return render_template("show.html",user=user)



@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')












    

