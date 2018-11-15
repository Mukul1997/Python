from flask import Flask, render_template, url_for, request, session, redirect, flash
from flask_pymongo import PyMongo
import json
import qrgen as q
# import bcrypt

app = Flask(__name__)

# mongodb configs
app.config["MONGO_URI"] = "mongodb://localhost:27017/mukul"
mongo = PyMongo(app)

# routes
@app.route('/')
def index():
    if 'username' in session:
        flash('You are logged in as '+ session['username'],'info')
    return render_template('home.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/loginVerify',methods=['POST'])
def loginVerify():
    users = mongo.db.users
    log =  users.find_one({'name' : request.form['username']})

    if log:
        # if bcrypt.hashpw(request.form['password'].encode('utf-8'), log['password'].encode('utf-8')) == log['password'].encode('utf-8'):
        if request.form['password'] == log['password']:
            session['username'] = request.form['username']
            return redirect(url_for('dashboard'))
    flash("Login Failed","danger")
    return redirect(url_for('login'))

@app.route('/register',methods=['POST','GET'])
def register():
    if request.method == 'POST':
        users = mongo.db.users
        exist =  users.find_one({'name' : request.form['username']})

        if exist is None:
            # hashpass = bcrypt.hashpw(request.form['pass'].encode('utf-8'),bcrypt.gensalt())
            users.insert({'name' : request.form['username'], 'password' : request.form['password']})
            session['username'] = request.form['username']
            d = request.form['username'] + "\n" + request.form['password']
            q.genImage(d,session['username'])
            flash('Registration Successful',"success")
            return redirect(url_for('dashboard'))
        flash('Username Exists !',"warning")
    return render_template('register.html')

@app.route('/dashboard')
def dashboard():
    if 'username' in session:
        users = mongo.db.users
        data =  users.find_one({'name' : session['username']})
        flash("Successfully Logged In","success")
        return render_template('dashboard.html',data = data)
    return render_template('noFile.html')

@app.route('/update',methods=['POST'])
def update():
    users = mongo.db.users
    f_name = request.form['fname']
    b_ranch = request.form['branch']
    p_hone = request.form['phone']
    e_mail = request.form['email']
    f_semester = request.form['semester']
    s_ection = request.form['section']
    users.update({'name' : session['username']},{ '$set' : {'fname' : f_name,'branch' : b_ranch, 'phone' : p_hone, 'sem' : f_semester, 'section' : s_ection, 'email' : e_mail} })
    flash("Successfully Updated !",'success')
    data =  users.find_one({'name' : session['username']})
    d = data['name'] + "\n" + data['password']
    q.genImage(d,session['username'])
    return render_template('dashboard.html',data=data)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/404FNF')
def fileNotFound():
    return render_template('noFile.html')

@app.route('/logout')
def logout():
    session.clear()
    flash("Successfully Logged Out","success")
    return render_template('home.html')

# run server
if __name__ == '__main__':
    app.secret_key = 'wakanda'
    app.run(port=1947,debug=True)
