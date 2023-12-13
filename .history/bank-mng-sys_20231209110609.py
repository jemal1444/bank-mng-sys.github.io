from flask import Flask, render_template, request, flash, redirect, url_for
from flask_mysqldb import MySQL
from passlib.hash import sha256_crypt

app = Flask(__name__)

# MySQL configurations
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'password'
app.config['MYSQL_DB'] = 'mydatabase'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

# Initialize MySQL
mysql = MySQL(app)

# Initialize passlib
hash = sha256_crypt


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/', methods=['GET','POST'])
def login():
        username=request.form['username']
        password=request.form['password']
        cur=None
        cur=MySQL.connection.cursor()
        cur.execute('SELECT * FROM users WHERE username=%s AND password=%s')
        data=cur.fetchone()
        if data is None:
            return "Password or Username is Wrong!"
        else:
            return "Loggedin Successfully"

if __name__=='__main__':
    app.run(debug=True)
    