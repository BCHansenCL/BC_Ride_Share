from flask import Flask, render_template, request, redirect, url_for # type: ignore
import sqlite3

def add_event(loc,t,s):
    cursor.execute('INSERT INTO rides(location,timestamp,seats) VALUES(?,?,?)',(location,time,seats))


conn = sqlite3.connect('eaglerides.db')
cursor = conn.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS rides (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        location TEXT,
        time datetime,
        seats INTEGER
    )
''')
location = "test"
time = 1728324000
seats = 3
add_event(location,time,seats)
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



@app.route('/submit')
def submit():
    print("hello")
    name = request.form['name']  # Get name from form
    phone = request.form['phone']  # Get phone number
    location = request.form['destination']  # Get destination
    seats = request.form['num_people'] 
    cursor.execute('INSERT INTO rides(location,timestamp,seats) VALUES(?,?,?)',(location,time,seats))
    return redirect(url_for('index'))



if __name__ == '__main__':
    app.run(debug=True)

