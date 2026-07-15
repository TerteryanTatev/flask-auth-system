import sqlite3
import os
from datetime import datetime

DATABASE_PATH = os.path.join(os.path.dirname(__file__), 'database', 'users.db')


def get_connection():
    connection = sqlite3.connect(DATABASE_PATH)
    connection.row_factory = sqlite3.Row
    return connection


def init_db():
    os.makedirs(os.path.dirname(DATABASE_PATH), exist_ok=True)
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            email TEXT UNIQUE NOT NULL,
            password_hash TEXT NOT NULL,
            salt TEXT NOT NULL,
            created_at TEXT NOT NULL
        )
    ''')
    connection.commit()
    connection.close()


def create_user(username, email, password_hash, salt):
    connection = get_connection()
    cursor = connection.cursor()
    created_at = datetime.now().isoformat()
    cursor.execute(
        'INSERT INTO users (username, email, password_hash, salt, created_at) VALUES (?, ?, ?, ?, ?)',
        (username, email, password_hash, salt, created_at)
    )
    connection.commit()
    connection.close()


def get_user_by_email(email):
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM users WHERE email = ?', (email,))
    user = cursor.fetchone()
    connection.close()
    return user


def get_user_by_username(username):
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM users WHERE username = ?', (username,))
    user = cursor.fetchone()
    connection.close()
    return user


def get_user_by_id(user_id):
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM users WHERE id = ?', (user_id,))
    user = cursor.fetchone()
    connection.close()
    return user