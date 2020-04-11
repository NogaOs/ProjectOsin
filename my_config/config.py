import os

from peewee import PostgresqlDatabase

db = PostgresqlDatabase(
    'scheduleDB', 
    user='noga_osin', 
    password='correctNogaZokLamba', 
    host='schedule-db.clhrtwy2vi9q.us-east-2.rds.amazonaws.com', port=5432)

def get_secret_key():
    return os.urandom(24)

