
import hashlib
from flask import Flask, render_template, request, redirect, url_for, session
from flask_mysqldb import MySQL
import MySQLdb.cursors
import re
import mysql.connector
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Test@1234",
    database="bank_mng_sys"
)

mysql=MySQL()
app = Flask (__name__)
# Config MySQL
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'Test@1234'
app.config['MYSQL_DB'] = 'bank_mng_sys'
mysql.init_app(app)

app.secret_key = 'alx'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/', methods=['GET','POST'])
def login():
        username=request.form['username']
        password=request.form['password']
        cursor=mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM users WHERE username=%s AND password=%s', (username,password))
        
        data=cursor.fetchone()
        if data is None:
            return "<h1>Password or Username is Wrong!</h1>"
        else:
            return render_template('home.html')
#=====================================================       
# User Registration
@app.route('/register', methods=['GET','POST'])
def register():
    # Output message if something goes wrong...
    msg = ''
    # Check if "username", "password" and "email" POST requests exist (user submitted form)
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form and 'email' in request.form:
        # Create variables for easy access
        username = request.form['username']
        password = request.form['password']
        email = request.form['email'] 
        # Check if user account exists using MySQL
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM users WHERE username = %s', (username,))
        user = cursor.fetchone()
        # If account exists show error and validation checks
        if user:
            msg = 'User account already exists!'
        elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
            msg = 'Invalid email address!'
        elif not re.match(r'[A-Za-z0-9]+', username):
            msg = 'Username must contain only characters and numbers!'
        elif not username or not password or not email:
            msg = 'Please fill out the form!'
        else:
            # Hash the password
            hash = password + app.secret_key
            hash = hashlib.sha1(hash.encode())
            password = hash.hexdigest()
            # Account doesn't exist, and the form data is valid, so insert the new account into the accounts table
            cursor.execute('INSERT INTO users VALUES (NULL, %s, %s, %s)', (username, password, email,))
            mysql.connection.commit()
            msg = 'You have successfully registered!'
        
    elif request.method == 'POST':
        # Form is empty... (no POST data)
        msg = 'Please fill out the form!'
    # Show registration form with message (if any)
    return render_template('register.html', msg=msg)

@app.route('/user_management',methods=['GET','POST'])
def user_management():
    return render_template('user_management.html')
#===============================================
#Function to create a new bank account# Establish database connection
# Establish database connection
@app.route('/create_bank_account', methods=['GET','POST'])    

def create_bank_account(account_number, account_holder, balance):
    cursor = db.cursor()
    # SQL query to insert a new bank account record
    sql = "INSERT INTO accounts (account_number, account_holder, balance) VALUES (%s, %s, %s)"
    values = (account_number, account_holder, balance)

    try:
        cursor.execute(sql, values)
        db.commit()
        print("Bank account created successfully!")
    except Exception as e:
        db.rollback()
        print("Error creating bank account:", str(e))
    finally:
        cursor.close()
        db.close()

#=============================
# A list to store the created bank accounts
accounts = []
# Define a route for the bank account creation page
@app.route('/create_account', methods=['GET', 'POST'])
def create_account():
    if request.method == 'POST':
        account_number = request.form['account_number']
        account_name = request.form['account_name']

        # Create a dictionary to store the account details
        account = {
            'account_number': account_number,
            'account_name': account_name
        }



        # Add the account to the accounts list
        accounts.append(account)

        # Redirect to the account list page after successful account creation
        return redirect('/account_list')

    # Render the bank account creation form
    return render_template('create_account.html')

# Define a route for the account list page
@app.route('/account_list')
def account_list():
    # Pass the accounts list to the template
    return render_template('account_list.html', accounts=accounts)

#Transaction code
@app.route('/transaction', methods=['GET','POST'])
def transaction():
    account_number = request.form.get('account_number')
    amount = request.form.get('amount')
    transaction_type = request.form.get('transaction_type')

    if amount is None:
        return "Invalid amount."

    try:
        amount = float(amount)
    except ValueError:
        return "Invalid amount. Please enter a valid number."

    # Create a new transaction object
    transaction = Transaction(account_number=account_number, amount=amount, transaction_type=transaction_type)

    # Save the transaction to the database
    mysql.session.add(transaction)
    mysql.session.commit()

    # Perform transaction logic here
    if transaction_type == 'deposit':
        # Logic for deposit
        result = f"Successfully deposited ${amount} to account number {account_number}."
    elif transaction_type == 'withdraw':
        # Logic for withdrawal
        result = f"Successfully withdrew ${amount} from account number {account_number}."
    else:
        result = "Invalid transaction type."

    return result

@app.route('/logout')
def logout():
    # Remove session data, this will log the user out
    session.pop('loggedin', None)
    session.pop('id', None)
    session.pop('username', None)
    # Redirect to login page
    return redirect(url_for('/'))


if __name__=='__main__':
    app.run(debug=True)