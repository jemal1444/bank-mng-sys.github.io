from flask import Flask, render_template, request, redirect, url_for, session
from flask_mysqldb import MySQL
import MySQLdb.cursors
import MySQLdb.cursors, re, hashlib
import mysql.connector

mysql=MySQL()
connection=mysql.connector.connect(host='localhost', user='root',password='Test@1234', database='bank_mng_sys')   
cursor=connection.cursor()                       


app = Flask (__name__)
# Config MySQL
'''app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'Test@1234'
app.config['MYSQL_DB'] = 'bank_mng_sys'
mysql.init_app(app)'''

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/', methods=['GET','POST'])
def login():
    ALX=''
    if request.method=='POST':
        username=request.form['username']
        password=request.form['password']
        cursor=MySQL.connection.cursor()
        cursor.execute('SELECT * FROM users WHERE username=%s AND password=%s')
        data=cursor.fetchone()
        if data:
            session['loggedin']=True
            session['username']=data[0] 
            return redirect(url_for('index'))
        else:
            ALX= "Incorrect Username/Password. Try again!"
    return render_template('index.html', ALX=ALX)
if __name__=='__main__':
    app.run(debug=True)
    