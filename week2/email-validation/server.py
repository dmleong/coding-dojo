from flask import Flask, session, flash, render_template, request, redirect
import re
from mysqlconnection import MySQLConnector

emailRegex = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
app = Flask(__name__)
app.secret_key = 'ThisIsSecret'
mysql = MySQLConnector('emailsdb')


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/create', methods=['POST'])
def create():
    if request.form['email'] == '':
        flash('Email cannot be blank', 'emailError')
        pass
    elif not emailRegex.match(request.form['email']):
        flash('Invalid email address', 'emailError')
        pass
    else:
        email = request.form['email']
        session['email'] = email
        query = "INSERT INTO emails (email_addresses, created_at, updated_at) VALUES ('{}', NOW(), NOW())".format(session['email'])
        print query
        mysql.run_mysql_query(query)

    return redirect('/results')

@app.route('/results')
def show():
    query = "SELECT * FROM emails"
    emailList = mysql.fetch(query)
    return render_template('results.html', email=session['email'], list=emailList)

@app.route('/delete', methods=['POST'])
def delete():
    id = int(request.form['hidden'])
    query = "DELETE FROM emails WHERE idemails = '{}'".format(id)
    print query
    mysql.run_mysql_query(query)
    return redirect('/results')

app.run(debug=True)
