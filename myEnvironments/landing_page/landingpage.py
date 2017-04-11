#source py2FlaskEnv/bin/activate

from flask import Flask, render_template
app = Flask(__name__)
@app.route('/')
def landingpage():
    return render_template("landingpage.html", phrase="Hello")

@app.route('/ninjas')
def ninjas():
    return render_template("ninjas.html")

@app.route('/dojos/new')
def dojos():
    return render_template("dojos.html")

app.run(debug=True)
