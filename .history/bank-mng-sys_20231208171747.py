from flask import Flask, render_template, request, redirect, url_for, session
from flask_mysqldb import MySQL
import MySQLdb.cursors
import MySQLdb.cursors, re, hashlib

mysql=MySQL()

app = Flask (__name__)
# Config MySQL
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '1234'
app.config['MYSQL_DB'] = 'bank_mng_sys'
mysql.init_app(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/', methods=['GET','POST'])
def login():
    username=request.form['username']
    password=request.form['password']
    cursor=MySQL.connection.cursor()
    cursor.execute('SELECT * FROM users WHERE username=%s AND password=%s')
    data=cursor.fetchone()
    if data:
        session['loggedin']=True
        session['username']=data[1]
        return redirect(url_for('index'))
        return "Username or Password wrong"
    else:
        ALX= "Incorrect Username/Password. Try again!"
    return render_template('index.html')
if __name__=='__main__':
    app.run(debug=True)
    