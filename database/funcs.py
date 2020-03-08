def print_usernames():
    db.connect()
    query = User.select()
    for user in query:
        print(user.full_name)
    db.close()


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
        salt = salt, password=hash_password(user_password, salt)
    ) 
    db.close()