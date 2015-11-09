from flask import Flask, render_template, session
import random

app = Flask(__name__)
app.secret_key = 'ThisIsSecret'

num = random.randrange(0, 101)

@app.route('/')
def index():
    return render_template('index.html')

app.run(debug=True)
