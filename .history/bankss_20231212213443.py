from flask import Flask, render_template, request, redirect, url_for, session
from flask_mysqldb import MySQL
import MySQLdb.cursors
import re

mysql=MySQL()
app = Flask (__name__)
import mysql.connector

# Connect to MySQL
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Test@1234",
    database="bank_mng_sys"
)

# Create a cursor object to execute SQL queries
cursor = db.cursor()

# Create a table for storing user credentials (if it doesn't exist)
create_table_query = """
CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(255) NOT NULL,
    password VARCHAR(255) NOT NULL
)
"""
cursor.execute(create_table_query)

# User Registration
def register():
    username = input("Enter username: ")
    password = input("Enter password: ")

    # Check if the username already exists
    check_username_query = "SELECT * FROM users WHERE username = %s"
    cursor.execute(check_username_query, (username,))
    if cursor.fetchone():
        print("Username already exists.")
        return

    # Insert the new user into the database
    insert_user_query = "INSERT INTO users (username, password) VALUES (%s, %s)"
    cursor.execute(insert_user_query, (username, password))
    db.commit()

    print("Registration successful.")

# User Login
def login():
    username = input("Enter username: ")
    password = input("Enter password: ")

    # Check if the credentials are valid
    check_credentials_query = "SELECT * FROM users WHERE username = %s AND password = %s"
    cursor.execute(check_credentials_query, (username, password))
    if cursor.fetchone():
        print("Login successful.")
    else:
        print("Invalid credentials.")

# Main program
while True:
    print("1. Register")
    print("2. Login")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        register()
    elif choice == "2":
        login()
    elif choice == "3":
        break
    else:
        print("Invalid choice.")

# Close the database connection
db.close()