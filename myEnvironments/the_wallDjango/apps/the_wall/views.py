from django.shortcuts import render, redirect, HttpResponse
from .models import User, Message, Comment
import datetime
# import Bcrypt
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
FIRSTNAME_REGEX = re.compile(r'^[a-zA-Z]*$')
LASTNAME_REGEX = re.compile(r'^[a-zA-Z]*$')
# bcrypt = Bcrypt(app)

def index(request):
    return render (request, 'the_wall/index.html')

def register(request):
    if request.method == "POST":
        email= request.POST['email']
        first_name= request.POST['first_name']
        last_name= request.POST['last_name']
        password= request.POST['password']
        confirm_password= request.POST['confirm_password']
        request.session['message']=[]
        time= datetime.datetime.now()
        flashMessage = False
        if len(email) < 1:
            flash("Email cannot be empty! ")
            flashMessage=True
        elif not EMAIL_REGEX.match(request.form['email']):
            flash("Invalid Email Address!")
            flashMessage=True
        if len(first_name) < 1:
            flash("First name cannot be empty!")
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
            People.objects.create(first_name=first_name, last_name=last_name, email=email, password=password, created_at=time, updated_at=time)
            people = People.objects.all()
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

def login(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']
        user_query = "SELECT * FROM users where users.email = :email LIMIT 1"
        query_data = {'email': email}
        user = mysql.query_db(user_query, query_data)
    #validate email
    if bcrypt.check_password_hash(user[0]['password'],password):
        query= "SELECT first_name from users WHERE email=:email"
        request.session['first_name']=mysql.query_db(query, query_data)
        request.session['new_first_name']=session['first_name'][0].get('first_name')
        request.session['first_name']=session['new_first_name']
        query= "SELECT id from users WHERE email=:email"
        request.session['id']=mysql.query_db(query, query_data)
        request.session['new_id']=request.ession['id'][0].get('id')
        request.session['id']=request.session['new_id']
        return redirect("/wall")
    else:
        flash("Password is incorrect!")
        return redirect("/")

def thewall(request):
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

def newmessage(request):
    if request.method == "POST":
        message = request.POST['message']
        insert_query = "INSERT INTO messages (user_id, message, created_at, updated_at) VALUES (:user_id, :message, NOW(), NOW())"
        query_data = { 'user_id': request.session['id'], 'message':message }
        mysql.query_db(insert_query, query_data)
        return redirect ('/wall')

def newcomment(request,message_id):
    if request.method == "POST":
        comment=request.POST['comment']
        insert_query = "INSERT INTO comments (user_id, comment, created_at, updated_at, message_id) VALUES (:user_id, :comment, NOW(), NOW(), :message_id)"
        query_data = { 'user_id': session['id'], 'comment':comment, 'message_id':message_id }
        mysql.query_db(insert_query, query_data)
        return redirect('/wall')

def logout(request):
    if request.method == "GET":
        request.session.flush()
    return redirect("/")
