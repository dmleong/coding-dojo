from flask import Flask, render_template, request, redirect, session, flash, url_for
from mysqlconnection import MySQLConnector
from flask.ext.bcrypt import Bcrypt
import re
import pprint
from itertools import groupby

app = Flask(__name__)
bcrypt = Bcrypt(app)
mysql = MySQLConnector('loginregistration')
app.secret_key = 'ThisIsSecret'

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
        session['first_name'] = str(request.form['first_name'])


    #Check last name
    if request.form['last_name'] == '':
        flash('Name cannot be blank', 'last_nameError')
        errors += 1
        pass
    elif any(char.isdigit() for char in request.form['last_name']) == True:
        flash('Name cannot have numbers', 'last_nameError')
        errors += 1
        pass
    else:
        session['last_name'] = str(request.form['last_name'])

    #Check email
    if str(request.form['email']) == '':
        flash('Email cannot be blank', 'emailError')
        errors += 1
        pass
    elif not emailRegex.match(request.form['email']):
        flash('Invalid email address', 'emailError')
        errors += 1
        pass
    else:
        session['email'] = str(request.form['email'])

    #Check password
    if str(request.form['password']) == '':
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
        session['password'] = str(request.form['password'])

    #Check confirmation password
    if str(request.form['confirm_password']) == '':
        flash('Please confirm password', 'confirm_passwordError')
        errors += 1
        pass
    elif str(request.form['confirm_password']) != str(request.form['password']):
        flash('Passwords do not match', 'confirm_passwordError')
        errors += 1
    else:
        session['confirm_password'] = str(request.form['confirm_password'])

    #See if there are any errors
    if errors > 0:
        session['password'] = ''
        session['confirm_password'] = ''
        return False
    else:
        return True

def validateLogin():
    errors = 0
     #Check email
    if str(request.form['email']) == '':
        flash('Email cannot be blank', 'loginEmailError')
        errors += 1
        pass
    elif not emailRegex.match(request.form['email']):
        flash('Invalid email address', 'loginEmailError')
        errors += 1
        pass
    else:
        session['email'] = str(request.form['email'])

    #Check password
    if request.form['password'] == '':
        flash('Password cannot be blank', 'loginPasswordError')
        errors += 1
        pass
    else:
        session['password'] = str(request.form['password'])

        #See if there are any errors
    if errors > 0:
        session['password'] = ''
        return False
    else:
        return True

def setUserId():
    getUserId = "SELECT idusers FROM users WHERE email = '{}'".format(session['email'])
    id = mysql.fetch(getUserId)
    session['userid'] = id[0]['idusers']
    return True

def checkIfEmailExists():
    getEmails = "SELECT email FROM users WHERE email = '{}'".format(session['email'])
    emailList = mysql.fetch(getEmails)
    if emailList == None:
        return False
    else:
        return True

def getPostsWithUsers():
    getPosts = "SELECT posts.idposts, posts.post_text, posts.created_at, users.idusers, users.idusers, users.first_name, users.last_name FROM posts LEFT JOIN users ON posts.user_id = users.idusers ORDER BY posts.created_at DESC"
    posts = mysql.fetch(getPosts)
    return posts

def getComments():
    getComments = "SELECT comments.post_id, comments.comment_text, comments.created_at, users.first_name, users.last_name FROM comments LEFT JOIN posts ON comments.post_id = posts.idposts LEFT JOIN users ON comments.user_id = users.idusers"
    comments = mysql.fetch(getComments)
    return comments

def getPostsWithComments():
    comments = getComments()
    posts = getPostsWithUsers()
    commentList = {}
    postsWithCommentContainer = []

    for comment in comments:
        info = {
                "post_id": comment['post_id'],
                "created_at": comment['created_at'].strftime("%B %d, %Y %-I:%M %p" ),
                "first_name": comment['first_name'],
                "last_name": comment['last_name'],
                "comment_text": comment['comment_text']
            }
        if comment['post_id'] in commentList:
            commentList[comment['post_id']].append(info)
        else:
            commentList[comment['post_id']] = [info]

    for post in posts:
        postData = {
            "created_at": post['created_at'].strftime("%B %d, %Y %-I:%M %p" ),
            "post_id": post['idposts'],
            "first_name": post['first_name'],
            "last_name": post['last_name'],
            "post_text": post['post_text'],
            "new_id": post['created_at'].strftime("%B%d%Y%-I%M%s" )
        }

        if post['idposts'] in commentList:
            postData['comments'] = commentList[post['idposts']]
        postsWithCommentContainer.append(postData)

    return postsWithCommentContainer

@app.route('/')
def index():
    if session['first_name'] == None:
        session['first_name'] = ''
    if session['last_name'] == None:
        session['last_name'] = ''
    if session['email'] == None:
        session['email'] = ''
    if session['password'] == None:
        session['password'] = ''
    if session['confirm_password'] == None:
        session['confirm_password'] = ''
    if session['userid'] == None:
        session['userid'] = ''
    if session['loggedin'] == None:
        session['loggedin'] = False

    return render_template('index.html')

@app.route('/create', methods=['POST'])
def create():
    if validate() == False:
        session['loggedin'] = False
        return redirect('/')
    else:
        if checkIfEmailExists() == True:
            encryptedPassword = bcrypt.generate_password_hash(request.form['password'])
            query = "INSERT INTO users (first_name, last_name, email, password, created_at, updated_at) VALUES ('{}', '{}', '{}','{}', NOW(), NOW())".format(session['first_name'], session['last_name'], session['email'], encryptedPassword)
            mysql.run_mysql_query(query)
            session['password'] = ''
            session['confirm_password'] = ''
            session['loggedin'] = True
            return redirect('/dashboard')
        else:
            flash('Account with email already exists. Please use another email', 'emailError')
    return redirect('/')

@app.route('/validate', methods=['POST'])
def validateLoginInfo():
    if validateLogin() == False:
        session['loggedin'] = False
        return redirect('/login')
    else:
        userInfo = mysql.fetch("SELECT * FROM users WHERE email = '{}'".format(session['email']))
        if userInfo:
            inputPassword = request.form['password']
            if bcrypt.check_password_hash(userInfo[0]['password'], inputPassword):
                session['loggedin'] = True
                session['userid'] = userInfo[0]['idusers']
                session['first_name'] = userInfo[0]['first_name']
                return redirect('/dashboard')
            else:
                flash('Incorrect password', 'loginPasswordError')
        else:
            flash('No user with that email exists. Please create new user', 'loginEmailError')
            return redirect('/')
    return redirect('/dashboard')

@app.route('/dashboard')
def returnDashboard():
    if session['loggedin'] == True:
        setUserId()
        postData = getPostsWithComments()
        return render_template('dashboard.html', posts=postData)
    else:
        return redirect('/')

@app.route('/post', methods=['POST'])
def postData():
    if session['loggedin'] == True:
        postMessage = str(request.form['post'])
        query = "INSERT INTO posts (post_text, created_at, updated_at, user_id) VALUES ('{}', NOW(), NOW(), '{}')".format(postMessage, session['userid'])
        mysql.run_mysql_query(query)
        return redirect('/dashboard')
    else:
        return redirect('/')

@app.route('/post/<post_id>/comment', methods=['POST'])
def postComment(post_id):
    if session['loggedin'] == True:
        commentMessage = str(request.form['comment'])
        query = "INSERT INTO comments (post_id, user_id, comment_text, created_at, updated_at) VALUES ('{}', '{}', '{}', NOW(), NOW())".format(post_id, session['userid'], commentMessage)
        mysql.run_mysql_query(query)
        return redirect('/dashboard')
    else:
        return redirect('/')

@app.route('/logout')
def clear():
    session['first_name'] = ''
    session['last_name'] = ''
    session['email'] = ''
    session['password'] = ''
    session['confirm_password'] = ''
    session['userid'] = ''
    session['loggedin'] = False

    return redirect('/')

app.run(debug=True)
