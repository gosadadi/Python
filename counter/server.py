from flask import Flask,render_template, redirect,request,session
app=Flask(__name__)
@app.route ('/')
def counter():
    return render_template ("counter.html")


if __name__== "__main__":
    app.run(debug=True)
