import hashlib
import secrets
import re


def generate_salt():
    return secrets.token_hex(16)


def hash_password(password, salt):
    derived_key = hashlib.pbkdf2_hmac(
        'sha256',
        password.encode('utf-8'),
        salt.encode('utf-8'),
        100000
    )
    return derived_key.hex()


def verify_password(password, salt, stored_hash):
    computed_hash = hash_password(password, salt)
    return secrets.compare_digest(computed_hash, stored_hash)


def is_valid_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None


def is_valid_username(username):
    return 3 <= len(username) <= 20


def is_valid_password(password):
    if len(password) < 8:
        return False
    if not re.search(r'[A-Z]', password):
        return False
    if not re.search(r'[a-z]', password):
        return False
    if not re.search(r'[0-9]', password):
        return False
    if not re.search(r'[!@#$%^&*(),.?":{}|<>_\-+=~`\[\]/;\']', password):
        return False
    return True