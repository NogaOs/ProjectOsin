import bcrypt

from my_config.config import db

from database.db_def import User, Event

from flask import session, redirect, url_for


def get_user_info():
    db.connect()
    users_info = [(user.full_name, user.mail) for user in User.select()]
    db.close()
    return users_info


def hash_password(user_paswd):
    salt = bcrypt.gensalt()
    user_paswd = bytes(user_paswd, 'utf-8')
    return bcrypt.hashpw(user_paswd, salt)
    

def add_user(user_name, user_mail, user_phone, user_password):
    db.connect()
    User.create(
        full_name=user_name, mail=user_mail, phone=user_phone, 
        password=hash_password(user_password)
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
    if bcrypt.checkpw(bytes(user_password, 'utf-8'), bytes(user.password, 'utf-8')):
        return user.id, user_name
    return False

