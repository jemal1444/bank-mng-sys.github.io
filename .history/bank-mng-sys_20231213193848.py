import crypt
from hashlib import scrypt
from xml.dom import registerDOMImplementation
from flask import Flask, render_template, request, redirect, url_for, session
#from werkzeug import generate_password_hash, check_password_hash

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
            return "<h1>Password or Username is Wrong!</h1>"
        else:
            return render_template('home.html')
        
# User Registration
@app.route('/templates/register',methods=['GET','POST'])
def register():
    form = registerDOMImplementation()
    if form.validate_on_submit():
        name = form.name.data
        email = form.email.data
        password = form.password.data

        hashed_password = crypt.hashpw(password.encode('utf-8'),scrypt.gensalt())

        # store data into database 
        cursor = mysql.connection.cursor()
        cursor.execute("INSERT INTO users (name,email,password) VALUES (%s,%s,%s)",(name,email,hashed_password))
        mysql.connection.commit()
        cursor.close()

        return redirect(url_for('login'))

    return render_template('register.html',form=form)
    
@app.route('/logout')
def logout():
	session.pop('email', None)
	return redirect('/')
    
    
if __name__=='__main__':
    app.run(debug=True)
    