from flask import Flask,render_template

app = Flask(__name__)

@app.route("/") #base url
def index():
    return render_template("play_ground.html",)
@app.route("/play/<int:times>/<color>")
def playGround(times,color):
    return render_template("play_ground.html",times=times,color=color)
if __name__=="__main__":
    app.run(debug=True) 