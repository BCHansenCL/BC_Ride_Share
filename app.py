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
        timestamp INTEGER,
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
    return render_template('index.html', posts=posts)

@app.route('/post', methods=['POST'])
def post():
    content = request.form['content']
    if content:
        posts.append(content)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)

