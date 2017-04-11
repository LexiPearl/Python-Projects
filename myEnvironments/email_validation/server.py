#source py2FlaskEnv/bin/activate

from flask import Flask, request, redirect, render_template, session, flash
import re
from mysqlconnection import MySQLConnector
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
app = Flask(__name__)
mysql = MySQLConnector(app,'emailvalidation')
app.secret_key = "Emailvalidation"


@app.route('/')
def index():
    # users = mysql.query_db("SELECT * FROM users")
    # print users
    # return render_template('index.html')
    # query = "SELECT * FROM users"                           # define your query
    # users = mysql.query_db(query)                           # run query with query_db()
    return render_template('index.html')
# @app.route('/friends/<friend_id>')
# def show(friend_id):
#         # Write query to select specific user by id. At every point where
#         # we want to insert data, we write ":" and variable name.
#     query = "SELECT * FROM friends WHERE id = :specific_id"
#         # Then define a dictionary with key that matches :variable_name in query.
#     data = {'specific_id': friend_id}
#         # Run query with inserted data.
#     users = mysql.query_db(query, data)
#         # users should be a list with a single object,
#         # so we pass the value at [0] to our template under alias one_friend.
#     return render_template('index.html', one_user=users[0])
@app.route('/success', methods=['POST'])
def create():
    # print request.form['first_name']
    # add a friend to the database!
       # Write query as a string. Notice how we have multiple values
    # we want to insert into our query.
    flashMessage = False
    if not EMAIL_REGEX.match(request.form['email_address']):
        flash(" Email is not valid!")
        flashMessage= True
        return redirect("/")
    if flashMessage== False:
        flash("The email address you entered is a valid email address! Thank you!")
        query = "INSERT INTO users (email_address, created_at, updated_at) VALUES (:email_address, NOW(), NOW())"
        # # We'll then create a dictionary of data from the POST data received.
        data = {
        'email_address': request.form['email_address'],
        }
        # # Run query, with dictionary values injected into the query.
        mysql.query_db(query, data)
        query = "SELECT * FROM users"                           # define your query
        users = mysql.query_db(query)
        return render_template('success.html', all_users=users)
# @app.route('/update_friend/<friend_id>', methods=['POST'])
# def update(friend_id):
#     query = "UPDATE friends SET first_name = :first_name, last_name = :last_name, occupation = :occupation WHERE id = :id"
#     data = {
#              'first_name': request.form['first_name'],
#              'last_name':  request.form['last_name'],
#              'occupation': request.form['occupation'],
#              'id': friend_id
#            }
#     mysql.query_db(query, data)
#     return redirect('/')
# @app.route('/remove_friend/<friend_id>', methods=['POST'])
# def delete(friend_id):
#     query = "DELETE FROM friends WHERE id = :id"
#     data = {'id': friend_id}
#     mysql.query_db(query, data)
#     return redirect('/')
app.run(debug=True)
