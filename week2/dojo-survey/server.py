from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'ThisIsSecret'

@app.route('/')
def index():
    option_list = ['San Jose', 'New York', 'Seattle']
    language_list = ['Python', 'PHP', 'Javascript']
    return render_template('index.html', option_list=option_list, language_list=language_list)

@app.route('/create', methods=['POST'])
def create_user():
    session['name'] = request.form['name']
    session['location'] = request.form['location']
    session['language'] = request.form['language']
    session['comment'] = request.form['comment']
    return redirect('/process')

@app.route('/process')
def show_user():
    return render_template('results.html')

app.run(debug=True)
