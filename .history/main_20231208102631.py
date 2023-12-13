import MySQLdb
from flask import Flask, render_template, flash, redirect, url_for, request, logging
from wtforms import Form, StringField, TextAreaField, validators
from flask_mysqldb import MySQL

app = Flask (__name__)
# Config MySQL
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '1234'
app.config['MYSQL_DB'] = 'todo'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

# Banking management system Update secret key
app.secret_key = 'UPDATETHISPART'

# init MYSQL
# mysql = MySQL(app)


# Task Form Class
class TaskForm(Form):
    name = StringField('Name', [validators.Length(min=1, max=55)])
    description = TextAreaField('Description', [validators.Length(min=5)])


@app.route('/')
def index():
    return render_template('index.html')


# Add task
@app.route('/login', methods=['GET', 'POST'])
def login():
    form = TaskForm(request.form)
    if request.method == 'POST' and form.validate():
        name = form.name.data
        description = form.description.data

        # Create Cursor
        cur = MySQLdb.connection.cursor()

        # Execute
        cur.execute("INSERT INTO todotask(name, description) VALUES(%s, %s)", (name, description))

        # Commit to DB
        MySQLdb.connection.commit()

        # Close connection
        cur.close()

        flash('the task created ', 'success')

        return redirect(url_for('index'))

    return render_template('index.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)