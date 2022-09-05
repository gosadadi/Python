from flask import Flask, render_template, redirect, request,session
app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe'


@app.route('/')
def counter():
    if 'times' not in session:
        session['times']=0
    session['times']+=1
    return render_template("counter.html", count=session['times'])

@app.route('/users')
def clicked():
    session['times']+=1
    return redirect('/')

@ app.route('/reset')
def reset():
    session['times']=0
    return redirect('/')


if __name__ == "__main__":
    app.run(debug=True)
