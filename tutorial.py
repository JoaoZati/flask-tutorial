from flask import Flask, redirect, url_for, render_template, request, session, flash
from datetime import timedelta
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = 'hello'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.permanent_session_lifetime = timedelta(minutes=5)

db = SQLAlchemy(app)


@app.route("/")
def home():
    return render_template('index.html', content='Testing', y=['a', 2])


@app.route('/user', methods=['GET', 'POST'])
def user():
    email = None

    if 'user' in session:
        user = session['user']
        if request.method == 'POST':
            email = request.form['email']
            session['email'] = email
            flash('Email was saved!')
        else:
            if 'email' in session:
                email = session['email']
        return render_template('user.html', user=user, email=email)

    flash('You are already Logged in')
    return redirect(url_for("login"))


@app.route("/admin")
def admin():
    return redirect(url_for("home"))


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session.permanent = True
        user = request.form['nm']
        session['user'] = user
        flash('Login successful')
        return redirect(url_for('user'))
    if 'user' in session.keys():
        flash('Already Logged in')
        return redirect(url_for('user'))
    return render_template('login.html')


@app.route("/logout")
def logout():
    if 'user' in session:
        user = session['user']
        flash(f'You have been log out, {user}', 'info')
    session.pop("user", None)
    session.pop("email", None)
    return redirect(url_for("login"))


if __name__ == '__main__':
    app.run(debug=True)
