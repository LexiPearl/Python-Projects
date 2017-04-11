#source py2FlaskEnv/bin/activate
from flask import Flask, render_template, request, redirect, session
import random
app = Flask(__name__)
app.secret_key = 'GreatNumberGame'
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        if session.get('number') == None:
            session['number'] = random.randrange(0,101)
    elif request.method == 'POST':
        if request.form['action'] == 'playagain':
            session['number'] = random.randrange(0,101)
            session.pop('guess')
        else:
            session['guess'] = int(request.form['hypothesis'])
            print session['guess']
    return render_template("greatnumbergame.html")
app.run(debug=True)
