#source py2FlaskEnv/bin/activate

from flask import Flask, request, redirect, render_template, session, flash
import re
from mysqlconnection import MySQLConnector
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
app = Flask(__name__)
mysql = MySQLConnector(app,'full_friends')
app.secret_key = "Fullfriends"


@app.route('/')
def index():
    query = "SELECT * FROM friends"
    friends = mysql.query_db(query)
    return render_template('index.html', all_friends=friends)
@app.route('/friends', methods=['POST'])
def create():
    flashMessage = False
    if not EMAIL_REGEX.match(request.form['email_address']):
        color="red"
        flash(" Email is not valid!")
        flashMessage= True
        return redirect("/")
    if flashMessage== False:
        color="green"
        flash("The email address you entered is a valid email address! Thank you!")
        query = "INSERT INTO friends (first_name, last_name, email_address, created_at, updated_at) VALUES (:first_name, :last_name, :email_address, NOW(), NOW())"
        data = {
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'email_address': request.form['email_address'],
        }
        mysql.query_db(query, data)
        query = "SELECT * FROM friends"
        friends = mysql.query_db(query)
        return render_template('index.html', all_friends=friends, color=color)

@app.route('/friends/<friend_id>/edit', methods=['GET'])
def show(friend_id):
    query = "SELECT * FROM friends Where id=:specific_id"
    data = {'specific_id': friend_id}
    friends = mysql.query_db(query,data)
    return render_template('friends.html', one_friend=friends)

@app.route('/friends/<friend_id>', methods=['POST'])
def update(friend_id):
    query = "UPDATE friends SET first_name = :first_name, last_name = :last_name, email_address = :email_address WHERE id = :id"
    data = {
             'first_name': request.form['first_name'],
             'last_name':  request.form['last_name'],
             'email_address': request.form['email_address'],
             'id': friend_id
           }
    mysql.query_db(query, data)
    return redirect('/')

@app.route('/friends/<friend_id>/delete', methods=['POST'])
def delete(friend_id):
    query = "DELETE FROM friends WHERE id = :id"
    data = {'id': friend_id}
    mysql.query_db(query, data)
    return redirect('/')
app.run(debug=True)
