from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.show import Show
from flask_app.models.user import User

@app.route("/shows")
def home_page():
    if 'user_id' not in session:
        return redirect('/')
    data = {
        "id": session['user_id']
    }

    logged_user = User.get_one(data)

    return render_template("show.html", logged_user=logged_user, all_show=Show.get_all())


@app.route('/shows/new')
def recipe_new():

    return render_template("show_form.html")


@app.route('/create/shows', methods=['POST'])
def create_shows():
    is_valid = Show.validate_show(request.form)
    if not is_valid:
        flash("please fill out all required form")
        return render_template("show_form.html")

    data = {
        "title": request.form['title'],
        "network": request.form['network'],
        "release_date": request.form['release_date'],
        "description": request.form['description'],
        "user_id": session['user_id']
    }

    new_show = Show.save(data)
    return redirect('/shows')


@app.route('/shows/<int:id>')
def view_one(id):

    data = {
        'id': id
    }
    user= {
        "id": session['user_id']
    }

    logged_user = User.get_one(user)

    return render_template("show_one_show.html", one_show=Show.get_one(data), logged_user=User.get_one(user))


@app.route('/edit_show/<int:id>')
def edit_page(id):
    if 'user_id' not in session:
        return redirect('/')
    data = {
        'id': id
    }
    one_show = Show.get_one(data)
    return render_template("update_show.html", one_show=one_show)


@app.route('/update/<int:id>', methods=['POST'])
def update(id):
    is_valid = Show.validate_show(request.form)
    if not is_valid:
        flash("please fill out all required form")
        return render_template("show_form.html")

    data = {
        'id': id,
        "title": request.form['title'],
        "network": request.form['network'],
        "release_date": request.form['release_date'],
        "description": request.form["description"],
        "user_id": session['user_id']
    }
    Show.update(data)
    return redirect("/shows")

@app.route('/delete/<int:id>')
def delete(id):
    data = {
        'id': id,
    }
    Show.destroy(data)
    return redirect('/shows')
