from sqlite3 import Cursor
from flask import Flask, render_template,session, redirect, request,url_for
from flask_mysqldb import MySQL
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from sqlalchemy import CursorResult


# Create a flask application
app=Flask(__name__)
app.secret_key='your-secret-key'

#Mysql db configuration
app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_USER']='root'
app.config['MYSQL_PASSWORD']=''
app.config['MYSQL_DB']='flask_users'

mysql=MySQL(app)


@app.route('/',methods=['GET','POST'])
def index(): 
    if request.method=='POST':
        username=request.form['username']
        password=request.form['password']
        cursor=mysql.connection.Cursor()
        
        
        Cursor.execute('SELECT * FROM user WHERE username=%s AND password=%s')
        record=Cursor.fetchone()
        if record:
            session['loggedin']=True
            session['username']=record[1]
            return redirect(url_for('index'))
        else:
            msg='Incorrect username/password. Try again!'
    return render_template ('index.html')       
if __name__=='__main__':
    app.run(debug=True)