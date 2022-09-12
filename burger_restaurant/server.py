# from flask_app.controllers import burgers
# from flask_app import app
from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('restaurant.html')


if __name__ == "__main__":
    app.run(debug=True)
