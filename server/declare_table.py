from flask import Flask

from flask_table import Table, Col

def print_usernames():
    db.connect()
    query = User.select()
    for user in query:
        print(user.full_name)
    db.close()

class ItemTable(Table):
    name = Col('fullName')

items = [dict(name='Name1', description='Description1'),
         dict(name='Name2', description='Description2'),
         dict(name='Name3', description='Description3')]

table = ItemTable(items)
# items = ItemModel.query.all()

print(table.__html__())