from flask import Flask, redirect, url_for, render_template, request, session
from datetime import timedelta

app = Flask(__name__)
app.secret_key = 'hello'


@app.route("/")
def home():
    return render_template('index.html', content='Testing', y=['a', 2])


@app.route('/<name>')
def user(name):
    return f'Hello {name}'


@app.route("/admin")
def admin():
    return redirect(url_for("home"))


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = request.form['nm']
        return redirect(url_for('user', name=user))
    return render_template('login.html')


if __name__ == '__main__':
    app.run(debug=True)
