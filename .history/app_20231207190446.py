from sqlite3 import Cursor
from mysql import 
from flask import Flask, render_template,session, redirect, request,url_for
from flask_mysqldb import MySQL
connection=MySQLdb.connector.connect(host='localhost',port='3307',database='mbks',user='root',password='1234')
 


# Create a flask application
app=Flask(__name__)



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
            return redirect(url_for('home'))
        else:
            msg='Incorrect username/password. Try again!'
    return render_template ('index.html')  
@app.route('/home')
def home():
    return render_template('home.html')    
if __name__=='__main__':
    app.run(debug=True)