from flask import Flask,render_template

app = Flask(__name__)

@app.route("/") #base url
def playGround():
    return render_template("play_ground.html")
@app.route("/play/<int:times>") #base url
def playGroundTimes(times):
    return render_template("play_ground.html",times=times)
@app.route("/play/<int:times>/<color>")
def playGroundTimesColor(times,color):
    return render_template("play_ground.html",times=times,color=color)
if __name__=="__main__":
    app.run(debug=True) 