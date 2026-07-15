from flask import Flask, render_template, request, redirect, url_for, session
import os
import database
import security

app = Flask(__name__)
app.secret_key = os.urandom(24)

database.init_db()


@app.route('/')
def index():
    if 'user_id' in session:
        return redirect(url_for('home'))
    return redirect(url_for('login'))


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username', '').strip()
        email = request.form.get('email', '').strip().lower()
        password = request.form.get('password', '')
        confirm_password = request.form.get('confirm_password', '')

        errors = []

        if not security.is_valid_username(username):
            errors.append('Username must be between 3 and 20 characters.')

        if not security.is_valid_email(email):
            errors.append('Please enter a valid email address.')

        if not security.is_valid_password(password):
            errors.append('Password must be at least 8 characters and include an uppercase letter, a lowercase letter, a number and a special character.')

        if password != confirm_password:
            errors.append('Passwords do not match.')

        if not errors and database.get_user_by_username(username):
            errors.append('This username is already taken.')

        if not errors and database.get_user_by_email(email):
            errors.append('This email is already registered.')

        if errors:
            return render_template('register.html', errors=errors, username=username, email=email)

        salt = security.generate_salt()
        password_hash = security.hash_password(password, salt)
        database.create_user(username, email, password_hash, salt)

        return redirect(url_for('login'))

    return render_template('register.html', errors=[], username='', email='')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email', '').strip().lower()
        password = request.form.get('password', '')

        user = database.get_user_by_email(email)

        if user is None or not security.verify_password(password, user['salt'], user['password_hash']):
            return render_template('login.html', error='Invalid email or password.', email=email)

        session['user_id'] = user['id']
        session['username'] = user['username']

        return redirect(url_for('home'))

    return render_template('login.html', error=None, email='')


@app.route('/home')
def home():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    return render_template('home.html', username=session.get('username'))


@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))


if __name__ == '__main__':
    app.run(debug=True)