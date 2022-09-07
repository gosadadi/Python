from flask import Flask, render_template, redirect, request, session
from dojo import Dojo
app = Flask(__name__)
app.secret_key = 'it is secret'


@app.route("/")
def dojos():
    dojos = Dojo.get_all()
    return render_template("dojos.html",all_dojos=dojos)


@app.route('/new_dojos', methods=["POST"])
def new_dojo():
    
    data = {"name":request.form["name"]}
    Dojo.save(data)
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)
