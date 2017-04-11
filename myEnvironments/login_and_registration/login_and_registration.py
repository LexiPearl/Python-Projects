#source py2FlaskEnv/bin/activate

from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
from flask.ext.bcrypt import Bcrypt
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
FIRSTNAME_REGEX = re.compile(r'^[a-zA-Z]*$')
LASTNAME_REGEX = re.compile(r'^[a-zA-Z]*$')
app = Flask(__name__)
bcrypt = Bcrypt(app)
mysql = MySQLConnector(app,'login_and_reg')
app.secret_key = "LoginAndReg"


@app.route('/')
def index():
    return render_template('login_and_registration.html')
@app.route('/process', methods=['POST'])
def process():
    email_address = request.form['email_address']
    password=request.form['password']
    last_name=request.form['last_name']
    first_name= request.form['first_name']
    password_confirmation=request.form['password_confirmation']
    flashMessage = False
    if len(email_address) < 1:
        flash("Email cannot be empty! ")
        flashMessage=True
    elif not EMAIL_REGEX.match(request.form['email_address']):
        flash("Invalid Email Address!")
        flashMessage=True
    if len(first_name) < 2:
        flash("First name cannot be empty! ")
        flashMessage=True
    elif not FIRSTNAME_REGEX.match(request.form['first_name']):
        flash("Invalid first name!")
        flashMessage=True
    if len(last_name) < 2:
        flash("Last name cannot be empty! ")
        flashMessage=True
    elif not LASTNAME_REGEX.match(request.form['last_name']):
        flash("Invalid last name!")
        flashMessage=True
    if len(password)<8:
        flash("Password length is invalid")
        flashMessage=True
    if len(password_confirmation) < 1:
        flash("Confirm password cannot be empty! ")
        flashMessage=True
    if password_confirmation != password:
        flash("Passwords do not match!")
        flashMessage=True
    if flashMessage==True:
        return redirect("/")
    if flashMessage==False:
        flash("Success!")
        pw_hash = bcrypt.generate_password_hash(password)
        insert_query = "INSERT INTO users (first_name, last_name, email_address, password, created_at, updated_at) VALUES (:first_name, :last_name, :email_address, :pw_hash, NOW(), NOW())"
        query_data = { 'first_name':first_name, 'last_name':last_name, 'email_address': email_address, 'pw_hash': pw_hash }
        mysql.query_db(insert_query, query_data)
        return render_template('login.html')
@app.route('/login', methods=['POST'])
def login():
    email_address = request.form['email_address']
    password = request.form['password']
    user_query = "SELECT * FROM users where users.email_address = :email_address"
    query_data = {'email_address': email_address}
    user = mysql.query_db(user_query, query_data)
    if bcrypt.check_password_hash(user[0]['password'],password):
        return render_template("yaloggedon.html")
    else:
        flash("Password is incorrect!")
        return redirect("/login")
        # return render_template('login.html')

app.run(debug=True)
