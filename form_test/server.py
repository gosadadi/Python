from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe' # set a secret key for security purposes


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/users', methods=['POST'])
def create_user():
    print("Got Post Info")
    session['name']= request.form['name']
    session['email'] = request.form['email']
    session['userinf']= request.form
    print(request.form)
    return redirect('/show')


@app.route("/show")
def show_user():
    print("Showing the User Info From the Form")
    print(session)
    return render_template("show.html")


if __name__ == "__main__":
    app.run(debug=True)
