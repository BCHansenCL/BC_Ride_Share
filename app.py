from flask import Flask, render_template, request, redirect, url_for # type: ignore
import sqlite3


conn = sqlite3.connect('eaglerides.db')
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
location = "test"
time = 1728324000
seats = 3
conn.commit()
conn.close()
app = Flask(__name__)

# In-memory list to store posts
posts = []



@app.route('/')
def index():
    return render_template('index.html')


@app.route('/post')
def post():
    return render_template('post.html')

@app.route('/drivers')
def post():
    return render_template('drivers.html')


@app.route('/submit')
def submit():
    print("hello")
    name = request.form['name']  # Get name from form
    phone = request.form['phone']  # Get phone number
    location = request.form['destination']  # Get destination
    seats = request.form['num_people'] 
    date = request.form['date'] 
    cursor.execute('INSERT INTO rides(location,date,seats,name,phone) VALUES(?,?,?,?,?)',(location,date,seats,name,phone))
    return redirect(url_for('index'))



if __name__ == '__main__':
    app.run(debug=True)

