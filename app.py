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
    return render_template('email.html',trips=trips)


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

@app.route('/email')
def email():
    return render_template(email.html)

@app.route('/send', methods = ['POST'])
def send():
    eml = request.form.get("email")
    sender_email = "eagleridebc@gmail.com"
    receiver_email = eml
    password = "hthrtac1524"
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = "Eagle Ride Code"
    code = random.random()
    body = "Your code is" + code
    msg.attach(MIMEText(body, 'plain'))
    try:
        # Setup the SMTP server
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        
        server.login(sender_email, password)

        text = msg.as_string()
        server.sendmail(sender_email, receiver_email, text)
        
        print("Email sent successfully!")
        
    except Exception as e:
        print(f"Failed to send email: {e}")
    finally:
        server.quit()


if __name__ == '__main__':
    app.run(debug=True)

