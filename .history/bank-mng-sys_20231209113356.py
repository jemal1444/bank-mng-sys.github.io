from flask import Flask, render_template, request, redirect, url_for, session,Cursor
from flask_mysqldb import MySQL
import MySQLdb.cursors
import MySQLdb.cursors, re, hashlib
import MySQLdb.cursors
import mysql.connector
from contextlib import closing


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

@app.route('/', methods=['GET','POST'])
def login():
        username=request.form['username']
        password=request.form['password']
        cur=MySQL.connection.Cursor()
        cur.execute('SELECT * FROM users WHERE username=%s AND password=%s')
        data=cur.fetchone()
        if data is None:
            return "Password or Username is Wrong!"
        else:
            return "Loggedin Successfully"
if __name__=='__main__':
    app.run(debug=True)
    