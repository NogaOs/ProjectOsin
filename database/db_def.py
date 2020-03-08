from peewee import (
    AutoField, CharField, DateTimeField, ForeignKeyField,
    Model, PostgresqlDatabase, SqliteDatabase
)
from database.config import db

import bcrypt

from datetime import datetime

# db = SqliteDatabase('application.db')


class AppBaseModel(Model):
    class Meta: 
        database = db

class User(AppBaseModel):
    id = AutoField()
    full_name = CharField()
    created_at = DateTimeField(default=datetime.now)
    mail = CharField()
    password = CharField()
    phone = CharField(null=True)
    salt = CharField()


class Team(AppBaseModel):
    id = AutoField()
    name = CharField()
    created_at = DateTimeField(default=datetime.now)


class Role(AppBaseModel):
    id = AutoField()
    name = CharField()
    created_at = DateTimeField(default=datetime.now)


class Event(AppBaseModel):
    id = AutoField()
    name = CharField()
    date = DateTimeField(default=datetime.now)
    comments = CharField(null=True)
    team = ForeignKeyField(Team, backref='events')


class UserAssociation(AppBaseModel):
    id = AutoField()
    user = ForeignKeyField(User)
    team = ForeignKeyField(Team)
    role = ForeignKeyField(Role)


class Availability(AppBaseModel):
    id = AutoField()
    signed_at = DateTimeField(default=datetime.now)
    user_association = ForeignKeyField(UserAssociation)
    event = ForeignKeyField(Event)


# db.connect()
# if __name__ == '__main__':
#     db.drop_tables([User, Team, Role, Event, Availability, UserAssociation])
#     db.create_tables([User, Team, Role, Event, Availability, UserAssociation])
#     noga = User.create(full_name="Noga Osin", mail="test@test.com", salt=bcrypt.gensalt(), password="veryshushu") 
#     nogasTeam = Team.create(name="Nogas team")
#     eventush = Event.create(name = "Motherlovhiffing international day", team=nogasTeam)
#     nossaNova = Role.create(name="DJ")
#     assoc = UserAssociation.create(user=noga, team=nogasTeam, role=nossaNova)
#     aval = Availability.create(user_association=assoc, event=eventush)

# db.close()


def print_usernames():
    usernames = []
    db.connect()
    for user in User.select():
        usernames.append(user.full_name)
    db.close()
    return usernames


def hash_password(user_paswd, salt):
    user_paswd = bytes(user_paswd, 'utf-8')
    hashed = bcrypt.hashpw(user_paswd, salt)
    print(hashed, user_paswd, salt)
    return hashed 
    

def add_user(user_name, user_mail, user_phone, user_password):
    salt = bcrypt.gensalt()
    db.connect()
    User.create(
        full_name=user_name, mail=user_mail, phone=user_phone, 
        salt=salt, password=hash_password(user_password, salt)
    ) 
    db.close()







