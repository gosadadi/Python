from os import times
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def checkerboard():
    return render_template("checker_board.html",times=4,z=4)

@app.route('/4')
def checkerboard8By4():
    return render_template("checker_board.html",times=4,z=2)
@app.route('/<int:times>/<int:z>/<col1>/<col2>')
def checkerboardChanging(times,z,col1,col2):
    return render_template("checker_board.html",times=times,z=z,col1=col1,col2=col2)
if __name__ == "__main__":
    app.run(debug=True)
