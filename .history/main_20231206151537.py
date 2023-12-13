from flask import Flask, render_template,session, redirect, request,url_for
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from sqlalchemy import CursorResult


# Create a flask application
app=Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')
@app.route('/login',methods=['GET','POST'])
def login():
    msg=''
    if request.method=='POST':
        username=request.form['username']
        password=request.form['password']
        Cursor.execute('SELECT * FROM user WHERE username=%s AND password=%s')
        record=cursor.fetchone()
        if record:
            session['loggedin']=True
            session['username']=record[1]
            return redirect(url_for('home'))
        else:
            msg='Incorrect username/password. Try again!'
        return render_template ('index.html')
        
if __name__=='__main__':
    app.run(debug=True)