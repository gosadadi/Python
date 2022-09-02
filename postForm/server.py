import re
from flask import Flask, render_template, redirect, request, session
app = Flask(__name__)
app.secret_key = 'keep it secret,keep it safe'


@app.route('/')
def index():
    return render_template("index.html")


@app.route("/sundaes/post", methods=['post'])
def sundaypost():
    print(request.form['name'])
    print(request.form['sauce'])
    print(request.form['whipped'])
    return redirect("/sucess")
if "whipped" in request.form:
    whipped=True
else:
    whipped=False


@app.route("/sucess")
def success():
    return "HELLO"


if __name__ == "__main__":
    app.run(debug=True)
