from sqlite3 import Cursor
import MySQLdb
from flask_mysqldb import MySQL
from flask import Flask, render_template, url_for, request, session, redirect


app=Flask(__name__)
app.secret_key='your secret key'

#Mysql Configuration
app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_USER']='root'
app.config['MYSQL_PASSWORD']=''
app.config['MYSQL_DB']='users'

mysql=MySQL(app)

@app.route('/')
def index(): 
    if request.method=='POST':
        username=request.form['username']
        password=request.form['password']
        cursor=MySQLdb.connection.Cursor()
        Cursor.execute('SELECT * FROM user WHERE username=%s AND password=%s')
        record=Cursor.fetchone()
        if record:
            session['loggedin']=True
            session['username']=record[1]
            return redirect(url_for('home'))
        else:
            msg='Incorrect username/password. Try again!'
    return render_template ('index.html')  

    

@app.route('/home')
def home():
    return render_template('home.html')    

@app.route('/login', methods=['GET','POST'])
def login():
    return 

if __name__=='__main__':
    app.run(debug=True)