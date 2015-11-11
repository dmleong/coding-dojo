from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
app = Flask(__name__)
mysql = MySQLConnector('friendsdb')

@app.route('/')
def index():
    friends = mysql.fetch("SELECT * FROM friends")
    return render_template('index.html', friends=friends)

@app.route('/friends', methods=['POST'])
def create():
    query = "INSERT INTO friends (first_name, last_name, occupation, created_at, updated_at) VALUES ('{}', '{}', '{}', NOW(), NOW())".format(request.form['first_name'], request.form['last_name'], request.form['occupation'])
    print query
    mysql.run_mysql_query(query)
    return redirect('/')

app.run(debug=True)
