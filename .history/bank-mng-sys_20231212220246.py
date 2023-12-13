from flask import Flask, render_template, request, redirect, url_for, session
from flask_mysqldb import MySQL
import MySQLdb.cursors
import re

from sqlalchemy import CursorResult

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
@app.route('/register',methods=['GET','POST'])
def register():
    username = input("Enter username: ")
    password = input("Enter password: ")

    # Check if the username already exists
    check_username_query = "SELECT * FROM users WHERE username = %s"
    CursorResult.execute(check_username_query, (username,))
    if CursorResult.fetchone():
        print("Username already exists.")
        return

    # Insert the new user into the database
    insert_user_query = "INSERT INTO users (username, password) VALUES (%s, %s)"
    cursor.execute(insert_user_query, (username, password))
    db.commit()

    print("Registration successful.")
    
if __name__=='__main__':
    app.run(debug=True)
    