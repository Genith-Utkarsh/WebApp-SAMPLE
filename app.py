from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

# Explicitly serve login.html at the root URL
@app.route('/')
def login():
    return render_template('login.html')

# Serve index.html at /home
@app.route('/home')
def home():
    return render_template('index.html')

# Block direct access to static .html files (e.g., /index.html)
@app.route('/<path:path>')
def catch_all(path):
    if path.endswith('.html'):
        return redirect(url_for('login'))  # Redirect to login if .html is accessed directly
    return render_template('login.html')  # Fallback for other undefined routes

if __name__ == '__main__':
    app.run()
