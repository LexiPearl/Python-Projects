#source py2FlaskEnv/bin/activate
from flask import Flask, render_template, request, redirect, flash, session
# the "re" module will let us perform some regular expression operations
import re
# create a regular expression object that we can use run operations on
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
FIRSTNAME_REGEX = re.compile(r'^[a-zA-Z]*$')
LASTNAME_REGEX = re.compile(r'^[a-zA-Z]*$')
app = Flask(__name__)
app.secret_key = "Registration"

@app.route('/')
def index():
    return render_template('registrationform.html')
@app.route('/process', methods=['POST'])
def process():
    email= request.form['email']
    firstname= request.form['firstname']
    lastname= request.form['lastname']
    # birthdate= request.form['birthdate']
    password= request.form['password']
    confirmpassword= request.form['confirmpassword']
    flashMessage = False
    if len(email) < 1:
        flash("Email cannot be empty! ")
        flashMessage=True
    elif not EMAIL_REGEX.match(request.form['email']):
        flash("Invalid Email Address!")
        flashMessage=True
    if len(firstname) < 1:
        flash("First name cannot be empty! ")
        flashMessage=True
    elif not FIRSTNAME_REGEX.match(request.form['firstname']):
        flash("Invalid first name!")
        flashMessage=True
    if len(lastname) < 1:
        flash("Last name cannot be empty! ")
        flashMessage=True
    elif not LASTNAME_REGEX.match(request.form['lastname']):
        flash("Invalid last name!")
        flashMessage=True
    # if len(birthdate) < 1:
    #     flash("Birth date cannot be empty!")
    #     flashMessage=True
    if len(password) < 1:
        flash("Password cannot be empty! ")
        flashMessage=True
    elif len(password)<8:
        flash("Password length is invalid")
        flashMessage=True
    if len(confirmpassword) < 1:
        flash("Confirm password cannot be empty! ")
        flashMessage=True
    if confirmpassword != password:
        flash("Passwords do not match!")
        flashMessage=True
    if flashMessage==True:
        return redirect("/")

    if flashMessage==False:
        flash("Success!")

        return render_template("registrationform.html")
app.run(debug=True)
