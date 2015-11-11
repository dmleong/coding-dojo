""" Import Oracle's python connector for MySQL """
import mysql.connector
import collections
def _convert(data):
    if isinstance(data, basestring):
        return str(data)
    elif isinstance(data, collections.Mapping):
        return dict(map(_convert, data.iteritems()))
    elif isinstance(data, collections.Iterable):
        return type(data)(map(_convert, data))
    else:
        return data
# Create a class that will give us an object that we can use to connect to a database
class MySQLConnection(object):
    # init method with configurations.
    def __init__(self, db):
        """ BEGIN DATABASE CONFIGURATIONS """
        self.config = {
            'user': 'root',
            'password': 'root', # Change this for windows users
            'database': db,
            'host': 'localhost',
            # comment out the line below for windows
            'unix_socket': '/Applications/MAMP/tmp/mysql/mysql.sock',
        }
        self.conn = mysql.connector.connect(**self.config)
    """ BELOW ARE THE CUSTOM FUNCTIONS WE BUILT FOR YOU TO USE """
    """
    fetch function should be used for queries that return multiple rows
    Rows are returned in a list of tuples with each tuple corresponding to a row
    """
    # Begin fetch
    def fetch(self, query):
        cursor = self.conn.cursor(dictionary=True)
        cursor.execute(query)
        data = list(cursor.fetchall())
        cursor.close()
        return _convert(data)
    """
    run_mysql_query function should be used for INSERT/UPDATE/DELETE queries
    returns the number of rows affected
    """
    # Begin run_mysql_query
    def run_mysql_query(self, query):
        cursor = self.conn.cursor(dictionary=True)
        data = cursor.execute(query)
        self.conn.commit()
        cursor.close()
        return data
# This is the module method to be called by the user in server.py. Make sure to provide the db name!
def MySQLConnector(db):
    return MySQLConnection(db)
