import dbm
from sqlite3 import Cursor
from MySQLdb import DBAPISet
from flask import Flask, render_template, request, redirect, url_for, session
from flask_mysqldb import MySQL
import MySQLdb.cursors
import re


mysql=MySQL()
app = Flask (__name__)
# Config MySQL
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'Test@1234'
app.config['MYSQL_DB'] = 'bank_mng_sys'
mysql.init_app(app)



@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET','POST'])
def login():
        username=request.form['username']
        password=request.form['password']
        cursor=mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM users WHERE username=%s AND password=%s', (username,password))
        
        data=cursor.fetchone()
        if data is None:
            return "Password or Username is Wrong!"
        else:
            return render_template('home.html')
        
# User Registration
@app.route('/register', methods=['GET','POST'])
def register():
    name = input("Enter your name: ")
    email = input("Enter your email: ")
    password = input("Enter your password: ")
    cursor=mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    # Check if the email already exists
    check_email_query = "SELECT * FROM customers WHERE email = %s"
    cursor.execute(check_email_query, (email,))
    if cursor.fetchone():
        print("Email already exists.")
        return

    # Insert the new customer into the database
    insert_customer_query = "INSERT INTO customers (name, email, password) VALUES (%s, %s, %s)"
    cursor.execute(insert_customer_query, (name, email, password))
    return render_template('register.html')
    print("Registration successful.")
@app.route('/logout', methods=['GET','POST'])
def logout():
    4session.pop('user_id',None)
    print("You have been loggedout successfully!")
    return render_template()
    
if __name__=='__main__':
    app.run(debug=True)
    