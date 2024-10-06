from flask import Flask, render_template, request, redirect, url_for # type: ignore
import sqlite3
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import random

conn = sqlite3.connect('eaglerides.db',check_same_thread=False)
cursor = conn.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS rides (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        location TEXT,
        date datetime,
        seats INTEGER,
        name TEXT,
        phone TEXT
    )
''')
app = Flask(__name__)

# In-memory list to store posts
posts = []



@app.route('/')
def index():
    cursor.execute('SELECT location, date, seats, name, phone FROM rides')
    trips = cursor.fetchall()
    return render_template('index.html',trips=trips)


@app.route('/post')
def post():
    return render_template('post.html')

@app.route('/drivers')
def drivers():
    return render_template('drivers.html')


@app.route('/submit', methods = ['POST'])
def submit():
    name = request.form.get("name")  # Get name from form
    phone = request.form.get("phone")  # Get phone number
    location = request.form.get("destination")  # Get destination
    seats = request.form.get("num_people") 
    date = request.form.get("date")
    with sqlite3.connect('eaglerides.db') as conn:  # Open a connection for each request
        cursor = conn.cursor()
        cursor.execute('INSERT INTO rides(location, date, seats, name, phone) VALUES (?, ?, ?, ?, ?)', 
                       (location, date, seats, name, phone))
        conn.commit()  # Commit the changes
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)

