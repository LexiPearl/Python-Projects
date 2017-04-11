#source py2FlaskEnv/bin/activate

from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'CounterKey'

@app.route('/', methods=['GET', 'POST'])
def index():
    if session.get('number') == None:
    #if 'counter' in session==False
        session['number'] = 0
    session['number'] += 1
    if request.method == 'POST':
        if request.form['action'] == 'plustwo':
            session['number'] += 1
        if request.form['action'] == 'clear':
            session['number'] = 1
    return render_template("counter.html")

app.run(debug=True)
