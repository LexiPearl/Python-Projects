#source py2FlaskEnv/bin/activate

from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
from flask.ext.bcrypt import Bcrypt
from datetime import datetime
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
FIRSTNAME_REGEX = re.compile(r'^[a-zA-Z]*$')
LASTNAME_REGEX = re.compile(r'^[a-zA-Z]*$')
app = Flask(__name__)
bcrypt = Bcrypt(app)
mysql = MySQLConnector(app,'the_wall')
app.secret_key = "Thewall"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['POST'])
def register():
    email= request.form['email']
    first_name= request.form['first_name']
    last_name= request.form['last_name']
    password= request.form['password']
    confirm_password= request.form['confirm_password']
    session['message']=[]
    flashMessage = False
    if len(email) < 1:
        flash("Email cannot be empty! ")
        flashMessage=True
    elif not EMAIL_REGEX.match(request.form['email']):
        flash("Invalid Email Address!")
        flashMessage=True
    if len(first_name) < 1:
        flash("First name cannot be empty! ")
        flashMessage=True
    # str.isalpha(str(request.form['last_name']))
    elif not FIRSTNAME_REGEX.match(request.form['first_name']):
        flash("Invalid first name!")
        flashMessage=True
    if len(last_name) < 1:
        flash("Last name cannot be empty! ")
        flashMessage=True
    elif not LASTNAME_REGEX.match(request.form['last_name']):
        flash("Invalid last name!")
        flashMessage=True
    if len(password)<8:
        flash("Password length is invalid")
        flashMessage=True
    if len(confirm_password) < 1:
        flash("Confirm password cannot be empty! ")
        flashMessage=True
    if confirm_password != password:
        flash("Passwords do not match!")
        flashMessage=True
    if flashMessage==True:
        return redirect('/')
    if flashMessage==False:
        pw_hash = bcrypt.generate_password_hash(password)
        insert_query = "INSERT INTO users (first_name, last_name, email, password, created_at, updated_at) VALUES (:first_name, :last_name, :email, :pw_hash, NOW(), NOW())"
        query_data = { 'first_name':first_name, 'last_name':last_name, 'email': email, 'pw_hash': pw_hash }
        mysql.query_db(insert_query, query_data)
        session['first_name']=first_name
        user_query = "SELECT * FROM users where users.email = :email"
        query_data = {'email': email}
        user = mysql.query_db(user_query, query_data)
        query= "SELECT id from users WHERE email=:email"
        session['id']=mysql.query_db(query, query_data)
        session['new_id']=session['id'][0].get('id')
        session['id']=session['new_id']
        return redirect('/wall')

@app.route('/login', methods=['POST'])
def login():
    email = request.form['email']
    password = request.form['password']
    user_query = "SELECT * FROM users where users.email = :email LIMIT 1"
    query_data = {'email': email}
    user = mysql.query_db(user_query, query_data)

    #validate email
    if bcrypt.check_password_hash(user[0]['password'],password):
        query= "SELECT first_name from users WHERE email=:email"
        session['first_name']=mysql.query_db(query, query_data)
        session['new_first_name']=session['first_name'][0].get('first_name')
        session['first_name']=session['new_first_name']
        query= "SELECT id from users WHERE email=:email"
        session['id']=mysql.query_db(query, query_data)
        session['new_id']=session['id'][0].get('id')
        session['id']=session['new_id']
        return redirect("/wall")
    else:
        flash("Password is incorrect!")
        return redirect("/")

@app.route('/wall')
def thewall():
    query= "SELECT concat(users.first_name, ' ', users.last_name) as user_name, users.id, messages.id as message_id, messages.message, messages.created_at from users join messages on messages.user_id=users.id order by messages.created_at desc"
    messages= mysql.query_db(query)
    # query_data={'users.name': users_name, 'messages.message':messages}
    # messages= mysql.query_db(query,query_data)
    # first_name=mysql.query_db(query,query_data)
    # query= "select * from messages"
    # query= SELECT users.first_name, users.last_name, users.id
    # query_data = {'first_name':first_name, 'last_name':last_name, 'id': id}
    # mysql.query_db(query)
    query= "SELECT concat(users.first_name, ' ', users.last_name) as user_name, users.id, comments.comment, comments.created_at, comments.id, comments.message_id as message_id from users join comments on comments.user_id=users.id join messages on messages.id=comments.message_id order by comments.created_at desc"
    comments= mysql.query_db(query)
    return render_template('the_wall.html', all_messages=messages, all_comments=comments)

@app.route('/newmessage', methods=['POST'])
def newmessage():
    message=request.form['message']
    insert_query = "INSERT INTO messages (user_id, message, created_at, updated_at) VALUES (:user_id, :message, NOW(), NOW())"
    query_data = { 'user_id': session['id'], 'message':message }
    mysql.query_db(insert_query, query_data)
    return redirect ('/wall')

@app.route('/newcomment/<message_id>', methods=['POST'])
def newcomment(message_id):
    comment=request.form['comment']
    insert_query = "INSERT INTO comments (user_id, comment, created_at, updated_at, message_id) VALUES (:user_id, :comment, NOW(), NOW(), :message_id)"
    query_data = { 'user_id': session['id'], 'comment':comment, 'message_id':message_id }
    mysql.query_db(insert_query, query_data)
    return redirect('/wall')

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')

app.run(debug=True)

# @app.route('/friends', methods=['POST'])
# def create():
#     flashMessage = False
#     if not EMAIL_REGEX.match(request.form['email_address']):
#         color="red"
#         flash(" Email is not valid!")
#         flashMessage= True
#         return redirect("/")
#     if flashMessage== False:
#         color="green"
#         flash("The email address you entered is a valid email address! Thank you!")
#         query = "INSERT INTO friends (first_name, last_name, email_address, created_at, updated_at) VALUES (:first_name, :last_name, :email_address, NOW(), NOW())"
#         data = {
#         'first_name': request.form['first_name'],
#         'last_name': request.form['last_name'],
#         'email_address': request.form['email_address'],
#         }
#         mysql.query_db(query, data)
#         query = "SELECT * FROM friends"
#         friends = mysql.query_db(query)
#         return render_template('index.html', all_friends=friends, color=color)
#
# @app.route('/friends/<friend_id>/edit', methods=['GET'])
# def show(friend_id):
#     query = "SELECT * FROM friends Where id=:specific_id"
#     data = {'specific_id': friend_id}
#     friends = mysql.query_db(query,data)
#     return render_template('friends.html', one_friend=friends)
#
# @app.route('/friends/<friend_id>', methods=['POST'])
# def update(friend_id):
#     query = "UPDATE friends SET first_name = :first_name, last_name = :last_name, email_address = :email_address WHERE id = :id"
#     data = {
#              'first_name': request.form['first_name'],
#              'last_name':  request.form['last_name'],
#              'email_address': request.form['email_address'],
#              'id': friend_id
#            }
#     mysql.query_db(query, data)
#     return redirect('/')
#
# @app.route('/friends/<friend_id>/delete', methods=['POST'])
# def delete(friend_id):
#     query = "DELETE FROM friends WHERE id = :id"
#     data = {'id': friend_id}
#     mysql.query_db(query, data)
#     return redirect('/')
# app.run(debug=True)
