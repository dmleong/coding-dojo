from flask import Flask, flash, render_template, request, redirect, session
import random

app = Flask(__name__)
app.secret_key = 'ThisIsSecret'

def setSession():
    session['num'] = random.randint(1,100)

@app.route('/')
def index():
    if session['num'] == None:
        setSession()
    else:
        pass
    print session['num']
    return render_template('index.html')

@app.route('/guess', methods=['POST'])
def checkNumber():
    error = None
    success = None
    guess = request.form['guess']
    if request.method == 'POST':
        if guess.isdigit():
            numguess = int(guess)
            if numguess == session['num']:
                flash('Correct', 'success')
                return redirect('/')
            elif numguess > session['num']:
                flash('Too high', 'error')
            else:
                flash('Too low', 'error')
        else:
            flash('Not a valid guess', 'error')
    elif isinstance(guess, str):
        flash('Not a valid guess', 'error')
    else:
        flash('Not a valid guess', 'error')

    return redirect('/')

@app.route('/reset', methods=['GET', 'POST'])
def reset():
    setSession()
    return redirect('/')

app.run(debug=True)
