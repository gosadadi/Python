from flask import Flask, render_template,redirect, request, session
app = Flask(__name__) 
app.secret_key = 'keep it secret, keep it safe'

@app.route('/')          
def index():
    return render_template('index.html')

@app.route('/create', methods=['POST']) 
def create():
    session['name'] = request.form['name']
    session['location'] = request.form['location']
    session['language'] = request.form['language']
    session['comments'] = request.form['comments']
    return redirect('/show')

@app.route('/show')
def show():
    return render_template('show.html')



if __name__=="__main__":    
    app.run(debug=True)   

