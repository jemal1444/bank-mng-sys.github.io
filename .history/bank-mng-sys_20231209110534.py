from flask import Flask, render_template, request, flash, redirect, url_for
from flask_mysqldb import MySQL
from passlib.hash import sha256_crypt

app = Flask(__name__)

# MySQL configurations
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'Test@1234'
app.config['MYSQL_DB'] = 'bank_mng_sys'


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
        
        cur=MySQL.connection.cur()
        cur.execute('SELECT * FROM users WHERE username=%s AND password=%s')
        data=cur.fetchone()
        if data is None:
            return "Password or Username is Wrong!"
        else:
            return "Loggedin Successfully"

# Route for registering a user
@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm(request.form)
    if request.method == 'POST' and form.validate():
        name = form.name.data
        email = form.email.data
        username = form.username.data
        password = hash.encrypt(str(form.password.data))

        try:
            # Create connection
            conn = mysql.connect()

            # Create cursor
            cur = conn.cursor()

            # Execute query
            cur.execute("INSERT INTO users(name, email, username, password) VALUES(%s, %s, %s, %s)",
            [name, email, username, password])

            # Commit to database
            conn.commit()

            # Close cursor and connection
            cur.close()
            conn.close()

            flash('You are now registered and can log in', 'success')

            return redirect(url_for('login'))

        except Exception as e:
            flash('An error occurred while registering: {}'.format(str(e)), 'danger')
            return redirect(url_for('register'))

    return render_template('register.html', form=form)

if __name__=='__main__':
    app.run(debug=True)
    