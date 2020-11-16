#!C:/Users/lx615/AppData/Local/Programs/Python/Python38-32/python

#Import Flask Library
from flask import Flask, render_template, request, session, url_for, redirect, flash
import mysql.connector

#Initialize the app from Flask
app = Flask(__name__)

#Configure MySQL
conn = mysql.connector.connect(host='localhost',
                       user='root', port=8889,
                       password='root',
                       database='air_ticket')

'''
#Define a route to hello function
@app.route('/')
def hello():
    return render_template('index.html')

#Define route for login
@app.route('/login')
def login():
    return render_template('login.html')

#Define route for register
@app.route('/register')
def register():
    return render_template('register.html')

#Authenticates the login
@app.route('/loginAuth', methods=['GET', 'POST'])
def loginAuth():
    #grabs information from the forms
    username = request.form['username']
    password = request.form['password']

    #cursor used to send queries
    cursor = conn.cursor()
    #executes query
    query = "SELECT * FROM user WHERE username = \'{}\' and password = \'{}\'"
    cursor.execute(query.format(username, password))
    #stores the results in a variable
    data = cursor.fetchone()
    #use fetchall() if you are expecting more than 1 data row
    cursor.close()
    error = None
    if(data):
        #creates a session for the the user
        #session is a built in
        session['username'] = username
        return redirect(url_for('home'))
    else:
        #returns an error message to the html page
        error = 'Invalid login or username'
        return render_template('login.html', error=error)

#Authenticates the register
@app.route('/registerAuth', methods=['GET', 'POST'])
def registerAuth():
    #grabs information from the forms
    username = request.form['username']
    password = request.form['password']

    #cursor used to send queries
    cursor = conn.cursor()
    #executes query
    query = "SELECT * FROM user WHERE username = \'{}\'"
    cursor.execute(query.format(username))
    #stores the results in a variable
    data = cursor.fetchone()
    #use fetchall() if you are expecting more than 1 data row
    error = None
    if(data):
        #If the previous query returns data, then user exists
        error = "This user already exists"
        return render_template('register.html', error = error)
    else:
        ins = "INSERT INTO user VALUES(\'{}\', \'{}\')"
        cursor.execute(ins.format(username, password))
        conn.commit()
        cursor.close()
        flash("You are logged in")
        return render_template('index.html')

@app.route('/home')
def home():
    
    username = session['username']
    cursor = conn.cursor();
    query = "SELECT ts, blog_post FROM blog WHERE username = \'{}\' ORDER BY ts DESC"
    cursor.execute(query.format(username))
    data1 = cursor.fetchall() 
    cursor.close()
    return render_template('home.html', username=username, posts=data1)

        
@app.route('/post', methods=['GET', 'POST'])
def post():
    username = session['username']
    cursor = conn.cursor();
    blog = request.form['blog']
    query = "INSERT INTO blog (blog_post, username) VALUES(\'{}\', \'{}\')"
    cursor.execute(query.format(blog, username))
    conn.commit()
    cursor.close()
    return redirect(url_for('home'))

@app.route('/logout')
def logout():
    session.pop('username')
    return redirect('/')
'''
#Define a route to hello function
@app.route('/')
def hello():
    return render_template('index.html')

#Define route for login
@app.route('/login')
def login():
    return render_template('login.html')

#Define route for register
@app.route('/register')
def register():
    return render_template('register.html')

#Define route for customer register
@app.route('/customerRegister')
def customerRegister():
    return render_template('customer_register.html')

#Authenticates the register
@app.route('/customerRegisterAuth', methods=['GET', 'POST'])
def customerRegisterAuth():
    email = request.form['username']
    password = request.form['password']
    building_num = request.form['building number']
    street = request.form['street']
    city = request.form['city']
    state = request.form['state']
    name = request.form['name']
    phone = request.form['phone']
    birthday = request.form['birthday']
    pp_num = request.form['passport num']
    pp_expir_date = request.form['passport expir']
    pp_country = request.form['passport country']

    cursor = conn.cursor()
    query = "SELECT * FROM customer WHERE email = \'{}\'"
    cursor.execute(query.format(email))
    data = cursor.fetchone()
    error = None
    if(data):
        error = "This user already exists"
        return render_template('customer_register.html', error = error)
    else:
        ins = "INSERT INTO customer VALUES(\'{}\', \'{}\', \'{}\', \'{}\', \'{}\', \'{}\', \'{}\', \'{}\', \'{}\', \'{}\', \'{}\', \'{}\' )"      
        cursor.execute(ins.format(email, name, password, building_num, street, city,
                state, phone, pp_num, pp_expir_date, pp_country, birthday))
        conn.commit()
        cursor.close()
        flash("registered!")
        return render_template('index.html')
    
#Define route for booking agent register
@app.route('/agentRegister')
def agentRegister():
    return render_template('agent_register.html')

#Authenticates the register
@app.route('/agentRegisterAuth', methods=['GET', 'POST'])
def agentRegisterAuth():
    email = request.form['username']
    password = request.form['password']
    agent_id = request.form['agent id']

    cursor = conn.cursor()
    query = "SELECT * FROM booking_agent WHERE email = \'{}\'"
    cursor.execute(query.format(email))
    data = cursor.fetchone()
    error = None
    if(data):
        error = "This user already exists"
        return render_template('agent_register.html', error = error)
    else:
        ins = "INSERT INTO booking_agent VALUES(\'{}\', \'{}\', \'{}\')"      
        cursor.execute(ins.format(email, password, agent_id))
        conn.commit()
        cursor.close()
        flash("registered!")
        return render_template('index.html')
    
#Define route for airline staff register
@app.route('/staffRegister')
def staffRegister():
    cursor = conn.cursor()
    query = "SELECT DISTINCT * FROM airline"
    cursor.execute(query)
    data = cursor.fetchall()
    
    return render_template('staff_register.html', airline_list=data)

#Authenticates the register
@app.route('/staffRegisterAuth', methods=['GET', 'POST'])
def staffRegisterAuth():
    email = request.form['username']
    password = request.form['password']
    first_name = request.form['first name']
    last_name = request.form['last name']
    birthday = request.form['birthday']
    airline = request.form['airline']

    cursor = conn.cursor()
    query = "SELECT * FROM airline_staff WHERE username = \'{}\'"
    cursor.execute(query.format(email))
    data = cursor.fetchone()
    error = None
    if(data):
        error = "This user already exists"
        return render_template('staff_register.html', error = error)
    else:
        ins = "INSERT INTO airline_staff VALUES(\'{}\', \'{}\', \'{}\', \'{}\', \'{}\', \'{}\')"      
        cursor.execute(ins.format(email, password, first_name, last_name, birthday, airline))
        conn.commit()
        cursor.close()
        flash("registered!")
        return render_template('index.html')

#Authenticates the login
@app.route('/loginAuth', methods=['GET', 'POST'])
def loginAuth():
    role = request.form['identity']
    username = request.form['username']
    password = request.form['password']

    cursor = conn.cursor()
    if role == 'customer':
        query = "SELECT * FROM customer WHERE email = \'{}\' and password = \'{}\'"
    elif role == 'booking_agent':
        query = "SELECT * FROM booking_agent WHERE email = \'{}\' and password = \'{}\'"
    else:
        query = "SELECT * FROM airline_staff WHERE username = \'{}\' and password = \'{}\'"
        
    cursor.execute(query.format(username, password))
    data = cursor.fetchone()
    cursor.close()
    error = None
    if(data):
        #creates a session for the the user
        session['username'] = username
        session['identity'] = role      #################
        return redirect(url_for('home'))
    else:
        error = 'Invalid login or username'
        return render_template('login.html', error=error)

#User homepage
@app.route('/home')
def home():
    username = session['username']
    identity = session['identity']
    
    if identity == 'customer':
        cursor = conn.cursor()
        query = "SELECT airline_name, flight_num, departure_airport, departure_time, arrival_airport, arrival_time, status FROM purchases NATURAL JOIN (ticket NATURAL JOIN flight) WHERE customer_email = \'{}\'"
        cursor.execute(query.format(username))
        data1 = cursor.fetchall()
        return render_template('home.html', username=username, identity=identity, upcoming=data1)



        
app.secret_key = 'some key that you will never guess'
#Run the app on localhost port 5000
#debug = True -> you don't have to restart flask
#for changes to go through, TURN OFF FOR PRODUCTION
if __name__ == "__main__":
    app.run('127.0.0.1', 5000, debug = True)
