#source py2FlaskEnv/bin/activate
from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('disappearingninjas.html')
@app.route('/<ninja>')
def green(ninja):
    return render_template('disappearingninjas.html', ninja=ninja)
@app.route('/ninja/<color>')
def individual(color):
    return render_template('disappearingninjas.html', color=color)
app.run(debug=True) # run our server
