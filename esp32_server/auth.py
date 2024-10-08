import hashlib
from database import load_db, save_db

def hash_password(password):
    return hashlib.sha256(password.encode('utf-8')).hexdigest()

def register_user(username, password):
    db = load_db()
    if username in db['users']:
        return False, "User already exists."

    db['users'][username] = {
        'password': hash_password(password)
    }
    save_db(db)
    return True, "User registered successfully."

def login_user(username, password):
    db = load_db()
    if username in db['users']:
        hashed_password = db['users'][username]['password']
        if hashed_password == hash_password(password):
            return True, "Login successful."
        else:
            return False, "Invalid password."
    return False, "User not found."

def edit_user(username, new_password):
    db = load_db()
    if username in db['users']:
        db['users'][username]['password'] = hash_password(new_password)
        save_db(db)
        return True, "Password updated."
    return False, "User not found."

def delete_user(username):
    db = load_db()
    if username in db['users']:
        del db['users'][username]
        save_db(db)
        return True, "User deleted."
    return False, "User not found."
