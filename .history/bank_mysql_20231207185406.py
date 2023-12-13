from flask import Flask, request, render_template

app=Flask(__name__)

app.secret_key='your-secret-key'

#Mysql db configuration
app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_USER']='root'
app.config['MYSQL_PASSWORD']=''
app.config['MYSQL_DB']='flask_users'

mysql=MySQL(app)