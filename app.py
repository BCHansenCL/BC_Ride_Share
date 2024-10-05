from flask import Flask, render_template, request, redirect, url_for # type: ignore

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
