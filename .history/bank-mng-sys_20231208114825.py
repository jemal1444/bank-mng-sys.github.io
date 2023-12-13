from flask import Flask,render_template,url_for, request
from flaskext.mysql import MySQL

mysql=MySQL()

app = Flask (__name__)
# Config MySQL
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'admin'
app.config['MYSQL_PASSWORD'] = '1234'
app.config['MYSQL_DB'] = 'bank_mng_sys'
mysql.init_app(app)
