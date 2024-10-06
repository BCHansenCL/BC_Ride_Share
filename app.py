from flask import Flask, render_template, request, redirect, url_for # type: ignore
import sqlite3


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
    return render_template('index.html')


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
    print(location,date,seats,name,phone)
    cursor.execute('INSERT INTO rides(location,date,seats,name,phone) VALUES(?,?,?,?,?)',(location,date,seats,name,phone))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)

