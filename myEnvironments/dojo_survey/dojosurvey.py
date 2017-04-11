#source py2FlaskEnv/bin/activate

from flask import Flask, render_template, request, redirect, flash, session
app = Flask(__name__)
app.secret_key = 'DojoSurvey'

@app.route('/')
def dojosurvey():
    # session.clear()
    if 'name' not in session:
        session['name']= ''
    return render_template("dojosurvey.html")

@app.route('/dojosurveypart2', methods=['POST'])
def dojosurveypart2():
    session['location']= request.form['location']
    session['language'] = request.form['language']
    name= request.form['name']
    comment= request.form['comment']
    flashMessage = ''
    if len(name)< 1:
        session['comment']=comment
        flashMessage += "Name cannot be empty! "
    if len(comment) > 121:
        session['name']=name
        flashMessage += "Comment cannot be longer than 120 characters! "
    if len(comment) < 1:
        session['name']=name
        flashMessage+= "Comment cannot be empty! "
    # recall the name attributes we added to our form inputs
    # to access the data that the user input into the fields we use request.form['name_of_input']
    if len(flashMessage) > 0:
        flash(flashMessage)
        return redirect("/")
    # redirects back to the '/' route
    session['name']=name
    session['comment']=comment
    return render_template('dojosurveypart2.html')
app.run(debug=True) # run our server

    #accessing data
# request.form['name_of_input']

    #storing the data
# my_data = request.form['name_of_input']

    #redirecting
# return redirect('/route_goes_here')
