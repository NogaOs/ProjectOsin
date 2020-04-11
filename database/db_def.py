from peewee import (
    AutoField, CharField, DateTimeField, ForeignKeyField,
    Model, PostgresqlDatabase, SqliteDatabase
)


# from my_config.config import db
import bcrypt

from datetime import datetime

# db = SqliteDatabase('application.db')


class AppBaseModel(Model):
    class Meta: 
        # database = db
        db = PostgresqlDatabase(
        'scheduleDB', 
        user='noga_osin', 
        password='correctNogaZokLamba', 
        host='schedule-db.clhrtwy2vi9q.us-east-2.rds.amazonaws.com', port=5432)

class User(AppBaseModel):
    id = AutoField()
    full_name = CharField()
    created_at = DateTimeField(default=datetime.now)
    mail = CharField()
    password = CharField()
    phone = CharField(null=True)


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
    team = ForeignKeyField(Team, backref='events')
    comments = CharField(null=True)


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


db.connect()
if __name__ == '__main__':
    db.drop_tables([User, Team, Role, Event, Availability, UserAssociation])
    db.create_tables([User, Team, Role, Event, Availability, UserAssociation])
    noga = User.create(full_name="Noga Osin", mail="test@test.com", salt=bcrypt.gensalt(), password="veryshushu") 
    nogasTeam = Team.create(name="Nogas team")
    eventush = Event.create(name = "Motherlovhiffing international day", team=nogasTeam)
    nossaNova = Role.create(name="DJ")
    assoc = UserAssociation.create(user=noga, team=nogasTeam, role=nossaNova)
    aval = Availability.create(user_association=assoc, event=eventush)

db.close()







