from flask import Flask,render_template,url_for, request,Cursor,session
from flaskext.mysql import MySQL

mysql=MySQL()

app = Flask (__name__)
# Config MySQL
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'admin'
app.config['MYSQL_PASSWORD'] = '1234'
app.config['MYSQL_DB'] = 'bank_mng_sys'
mysql.init_app(app)

@app.route('/')
def index():
    return render_template('index.html')
@app.route('/login', methods=['GET','POST'])
def login():
    username=request.form['username']
    password=request.form['password']
    cursor=MySQL.connection.Cursor()
    Cursor.execute('SELECT * FROM user WHERE username=%s AND password=%s')
    record=Cursor.fetchone()
    if record:
            session['loggedin']=True
            session['username']=record[1]
            return redirect(url_for('home'))
    else:
            msg='Incorrect username/password. Try again!'
    return render_template ('index.html')  
