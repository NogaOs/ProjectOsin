import bcrypt

from config.config import db

from database.db_def import User, Event

from flask import session, redirect, url_for


def get_user_info():
    db.connect()
    users_info = [(user.full_name, user.mail) for user in User.select()]
    db.close()
    return users_info


def hash_password(user_paswd, salt):
    user_paswd = bytes(user_paswd, 'utf-8')
    hashed = bcrypt.hashpw(user_paswd, salt)
    return hashed 
    

def add_user(user_name, user_mail, user_phone, user_password):
    salt = bcrypt.gensalt()
    db.connect()
    User.create(
        full_name=user_name, mail=user_mail, phone=user_phone, 
        salt=salt, password=hash_password(user_password, salt)
    ) 
    db.close()


def add_event(event_name, event_date, organized_by, comments=None):
    db.connect()
    Event.create(
        name=event_name, date=event_date, 
        team=organized_by, comments=comments
    )
    db.close() 


def user_login(user_name, user_password):
    db.connect()
    user = User.get(User.full_name == user_name)
    db.close()
    salt = bytes(user.salt, 'utf-8') 
    # if not bcrypt.checkpw(user_password, user.password):
    #     return 'login unsuccessfulllll.'
        # raise SyntaxError ('Username or password is invalid.')
    if hash_password(user_password, salt) == bytes(user.password, 'utf-8'):
        session['id'] = user.id
        session['user_name'] = user_name
        return redirect(url_for('index'))
    return 'login unsuccessful.' # search for 401

