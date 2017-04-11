#source py2FlaskEnv/bin/activate
import datetime
from flask import Flask, render_template, request, redirect, session
from datetime import datetime
import random
app = Flask(__name__)
app.secret_key = 'NinjaGold'
@app.route('/', methods=['GET', 'POST'])
def index():
    # session.clear()
    if request.method == 'GET':
        if session.get('gold') == None:
        # if 'gold' not in session:
            session['gold'] = 0
            session['info']=[]
    return render_template("ninjagold.html")
@app.route('/process_money', methods=['POST'])
def process():
    time= datetime.now()
    # pytz
    if request.form['action'] == 'farm':
        randomgold= random.randrange(10,21)
        location='farm'
    if request.form['action'] == 'cave':
        randomgold= random.randrange(5,11)
        location='cave'
    if request.form['action'] == 'house':
        randomgold= random.randrange(2,6)
        location='house'
    if request.form['action'] == 'casino':
        randomgold= random.randrange(-50,51)
        location='casino'
    if randomgold > -1:
        sentence= ("Earned " + str(randomgold) + " from the " + location+"! "+ str(time))
        color= 'green'
        session['info'].insert(0,{'sentence': sentence, 'class': color} )
    if randomgold < 0:
        sentence= ("Entered a casino and lost "+ str(randomgold) + " golds...Ouch. "+ str(time))
        color= 'red'
        session['info'].insert(0,{'sentence': sentence, 'class': color})
    session['gold'] += randomgold
    return redirect("/")
app.run(debug=True)
