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
    Cursor.execute('SELECT * FROM users WHERE username=%s AND password=%s')
    data=Cursor.fetchone()
    if data is None:
        return "Username or Password wrong"
    else:
        return "Logged in Successfully"
if __name__=='__main__':
    app.run(debug=True)
    