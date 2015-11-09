from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ninjas')
def ninja():
    return render_template('ninja.html')

@app.route('/dojos/new')
def dojo():
    return render_template('dojo.html', name='Danielle')

@app.route('/create', methods=['POST'])
def create_user():
    print "Got post info"
    name = request.form['name']
    email = request.form['email']
    return redirect('/success')

@app.route('/success')
def success():
    return render_template('success.html')

app.run(debug=True)
