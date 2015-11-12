from flask import Flask, render_template, request, redirect, session, flash, url_for
import re
from flask.ext.bcrypt import Bcrypt
from mysqlconnection import MySQLConnector

app = Flask(__name__)
app.secret_key = 'ThisIsSecret'
mysql = MySQLConnector('loginregistration')
bcrypt = Bcrypt(app)

emailRegex = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
passwordRegex = re.compile(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d).+$')


def validate():
    errors = 0
    #Check first name
    if request.form['first_name'] == '':
        flash('Name cannot be blank', 'first_nameError')
        errors += 1
        pass
    elif any(char.isdigit() for char in request.form['first_name']) == True:
        flash('Name cannot have numbers', 'first_nameError')
        errors += 1
        pass
    else:
        session['first_name'] = request.form['first_name']

    #Check last name
    if request.form['lastName'] == '':
        flash('Name cannot be blank', 'lastNameError')
        errors += 1
        pass
    elif any(char.isdigit() for char in request.form['lastName']) == True:
        flash('Name cannot have numbers', 'lastNameError')
        errors += 1
        pass
    else:
        session['lastName'] = request.form['lastName']

    #Check email
    if request.form['email'] == '':
        flash('Email cannot be blank', 'emailError')
        errors += 1
        pass
    elif not emailRegex.match(request.form['email']):
        flash('Invalid email address', 'emailError')
        errors += 1
        pass
    else:
        session['email'] = request.form['email']

    #Check password
    if request.form['password'] == '':
        flash('Password cannot be blank', 'passwordError')
        errors += 1
        pass
    elif len(request.form['password']) < 8:
        flash('Password must be greater than 8 characters', 'passwordError')
        errors += 1
        pass
    elif not passwordRegex.match(request.form['password']):
        flash('Password must contain at least one lowercase letter, one uppercase letter, and one digit', 'passwordError')
        errors += 1
        pass
    else:
        session['password'] = request.form['password']

    #Check confirmation password
    if request.form['confirmPassword'] == '':
        flash('Please confirm password', 'confirmPasswordError')
        errors += 1
        pass
    elif request.form['confirmPassword'] != request.form['password']:
        flash('Passwords do not match', 'confirmPasswordError')
        errors += 1
    else:
        session['confirmPassword'] = request.form['confirmPassword']

    #See if there are any errors
    if errors > 0:
        session['password'] = ''
        session['confirmPassword'] = ''
        return False
    else:
        return True

def validateLogin():
    errors = 0
     #Check email
    if request.form['email'] == '':
        flash('Email cannot be blank', 'emailError')
        errors += 1
        pass
    elif not emailRegex.match(request.form['email']):
        flash('Invalid email address', 'emailError')
        errors += 1
        pass
    else:
        session['email'] = request.form['email']

    #Check password
    if request.form['password'] == '':
        flash('Password cannot be blank', 'passwordError')
        errors += 1
        pass
    elif len(request.form['password']) < 8:
        flash('Password must be greater than 8 characters', 'passwordError')
        errors += 1
        pass
    elif not passwordRegex.match(request.form['password']):
        flash('Password must contain at least one lowercase letter, one uppercase letter, and one digit', 'passwordError')
        errors += 1
        pass
    else:
        session['password'] = request.form['password']

        #See if there are any errors
    if errors > 0:
        session['password'] = ''
        session['confirmPassword'] = ''
        return False
    else:
        return True


@app.route('/')
def index():
    if session['first_name'] == None:
        session['first_name'] = ''
    if session['lastName'] == None:
        session['lastName'] = ''
    if session['email'] == None:
        session['email'] = ''
    if session['password'] == None:
        session['password'] = ''
    if session['confirmPassword'] == None:
        session['confirmPassword'] = ''
    if session['userid'] == None:
        session['userid'] = ''

    return render_template('index.html')

@app.route('/create', methods=['POST'])
def create():
    if validate() == False:
        return redirect('/')
    else:
        encryptedPassword = bcrypt.generate_password_hash(request.form['password'])
        query = "INSERT INTO users (first_name, last_name, email, password, created_at, updated_at) VALUES ('{}', '{}', '{}','{}', NOW(), NOW())".format(session['first_name'], request.form['lastName'], session['email'], encryptedPassword)
        mysql.run_mysql_query(query)
        session['password'] = ''
        session['confirmPassword'] = ''
    return redirect('/dashboard')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/validate', methods=['POST'])
def validateLoginInfo():
    if validateLogin() == False:
        return redirect('/login')
    else:
        userInfo = mysql.fetch("SELECT * FROM users WHERE email = '{}'".format(session['email']))
        inputPassword = request.form['password']
        inputPasswordEncrypted = bcrypt.generate_password_hash(request.form['password'])

        if inputPasswordEncrypted == userInfo[0]['password']:
            return redirect('/dashboard')
        else:
            flash('Incorrect password', 'passwordError')
    return redirect('/login')

@app.route('/dashboard')
def returnDashboard():
    if session['email']:
        return render_template('dashboard.html')
    else:
        return redirect('/')

@app.route('/logout', methods=['POST'])
def clear():
    session['firstName'] = ''
    session['lastName'] = ''
    session['email'] = ''
    session['password'] = ''
    session['confirmPassword'] = ''
    session['userid'] = ''

    return redirect('/')

app.run(debug=True)
