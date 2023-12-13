from flask import Flask, render_template, flash, redirect, url_for, request, 
logging
from wtforms import Form, StringField, TextAreaField, validators
from flask_mysqldb import MySQL

app = Flask (__name__)
# Config MySQL
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'todo'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

# init MYSQL
mysql = MySQL(app)
@app.route('/')
def index():
return render_template('index.html')


@app.route('/add')
def task():
return render_template('add.html')

# Task Form Class
class TaskForm(Form):
name = StringField('Name', [validators.Length(min=1, max=55)])
description = TextAreaField('Description', [validators.Length(min=5)])

# Add task
@app.route('/add', methods=['GET', 'POST'])
def add():
    form = TaskForm(request.form)
    if request.method == 'POST' and form.validate():
    name = form.name.data
    description = form.description.data

    # Create Cursor
    cur = mysql.connection.cursor()

    # Execute
    cur.execute("INSERT INTO todotask(name, description) VALUES(%s, %s)",
    (name, description))

    # Commit to DB
    mysql.connection.commit()

    #Close connection
    cur.close()

    flash('the task created ', 'success')

    return redirect(url_for('add'))

return render_template('index.html', form=form)
if __name__ == '__main__':
app.run(debug = True)