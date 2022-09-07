from flask import Flask, render_template, redirect, session, request
from user import User
app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe'

@app.route('/user')
def index():
    users = User.get_all()
    return render_template('all_user.html', users=users)

@app.route('/user/new')
def all_user():
    
    return render_template('new_user.html')


@app.route('/new_user', methods=["POST"])
def new_user():
    
    data = {"first_name":request.form["first_name"],
            "last_name": request.form["last_name"],
            "email_address":request.form["email_address"]
            
            }
    print(data)
    User.save(data)
    return redirect('/user')

if __name__ == "__main__":
    app.run(debug=True)
