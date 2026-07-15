# Flask Secure Authentication System

A secure authentication web application built with **Flask** and **SQLite3**.  
The project demonstrates user registration, login, session management, and secure password handling using hashing techniques without external authentication libraries or ORM.

## Features

- User registration with validation
- Secure login and logout
- Session-based authentication
- Protected pages for authenticated users
- Password hashing with PBKDF2-HMAC
- Unique salt generation for each user
- Client-side and server-side validation
- Password strength indicator
- SQLite database integration
- Responsive modern UI

## Technology Stack

### Backend
- Python 3
- Flask
- SQLite3
- hashlib
- secrets
- re

### Frontend
- HTML5
- CSS3
- JavaScript

## Project Structure

```
flask-secure-auth-system/

├── app.py
├── database.py
├── security.py
├── requirements.txt
├── README.md
│
├── database/
│   └── users.db
│
├── templates/
│   ├── login.html
│   ├── register.html
│   └── home.html
│
└── static/
    ├── css/
    │   └── style.css
    └── js/
        └── script.js
```

## Installation

### Clone repository

```bash
git clone https://github.com/your-username/flask-secure-auth-system.git

cd flask-secure-auth-system
```

### Create virtual environment

```bash
python -m venv venv
```

Activate:

Windows:
```bash
venv\Scripts\activate
```

macOS/Linux:
```bash
source venv/bin/activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Run application

```bash
python app.py
```

Open in browser:

```
http://127.0.0.1:5000
```

## Security

- Passwords are never stored in plain text.
- Passwords are protected using `PBKDF2-HMAC` hashing.
- Each user has a unique random salt.
- Secure hash comparison is used during login.
- SQLite parameterized queries protect against SQL injection.
- Flask sessions are used for authentication management.

## Screenshots

Add application screenshots here:

- Registration page
- Login page
- Home page

## Future Improvements

- Password reset
- Email verification
- Two-factor authentication
- User profile management
- PostgreSQL integration

## Author

Developed as a university project to demonstrate Flask backend development, database integration, and secure authentication principles.

## License

MIT License
