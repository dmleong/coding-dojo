from flask import Flask
# import the Connector function
from mysqlconnection import MySQLConnector
app = Flask(__name__)
# connect and store the connection in "mysql" note that you pass the database name to the function
mysql = MySQLConnector('mydb')
# an example of running a query
print mysql.fetch("Select * From users")
app.run(debug=True)
