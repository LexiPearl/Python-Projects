#source py2FlaskEnv/bin/activate

from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'ThisIsSecret'
# our index route will handle rendering our form
@app.route('/')
def index():
    return render_template("index.html")
# this route will handle our form submission
# notice how we defined which HTTP methods are allowed by this route


@app.route('/users', methods=['POST'])
def create_user():
    print "Got Post Info"
        # recall the name attributes we added to our form inputs
        # to access the data that the user input into the fields we use request.form['name_of_input']
    session['name'] = request.form['name']
    session['email'] = request.form['email']
    # return render_template('users.html', name=name, email=email)
    return redirect('/show')


@app.route('/show')
def show_user():
    return render_template('users.html')
    # redirects back to the '/' route
    # return redirect('users.html')
app.run(debug=True) # run our server



    #accessing data
# request.form['name_of_input']

    #storing the data
# my_data = request.form['name_of_input']

    #redirecting
# return redirect('/route_goes_here')
