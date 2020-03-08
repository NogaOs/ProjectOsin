from database.db_def import add_user, hash_password, db, User

from database.funcs import print_usernames

from flask import Flask, render_template, request, session, redirect, url_for

from markupsafe import escape


app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

# @app.route('/')
# def welcomePage():
#     return '<html><p style="color:blue">I am the main page!</p></html>'


@app.route('/users/list')
def usersList():
    username_list = print_usernames()
    return '''
    <table style="width:100%">
    <tr>
    <th>name</th>
    </tr>
    {% for username in username_list %}
    <tr>
        <td>{{username}}</td>
    </tr>
    {% endfor %}
    </table>
    '''


@app.route('/')
def index():
    if 'username' in session:
        return 'Logged in as %s' % escape(session['username'])
    return 'You are not logged in'

# if (hmac_hash("sha256", $_POST['password'], $saltFromDatabase) === $hashFromDatabase)
#     $login = true;

# def hash_password(user_paswd, salt):
#     user_paswd = bytes(user_paswd, 'utf-8')
#     hashed = bcrypt.hashpw(user_paswd, salt)
#     print(hashed, user_paswd, salt)
#     return hashed 

# def print_usernames():
#     db.connect()
#     query = User.select()
#     for user in query:
#         print(user.full_name)
#     db.close()
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('full_name') 
        password = request.form.get('password') 
        db.connect()
        User.get(User.full_name == username)
        db.close()
        if hash_password(password, User.salt) == User.password:
            session['full_name'] = request.form['full_name']
            return redirect(url_for('index'))
    return '''
        <form method="post">
            <p><input type=text name=full_name></p><br>
            <p><input type=text name=password></p>
            <p><input type=submit value=Login></p>
        </form>
    '''

@app.route('/logout')
def logout():
    # remove the username from the session if it's there
    session.pop('username', None)
    return redirect(url_for('index'))


@app.route('/users/add', methods=["GET", "POST"]) 
def addUser():
    # in case the user pressed submit on the form
    if request.method == 'POST':  
        name = request.form.get('name')
        email = request.form.get('email')
        phone = request.form.get('phone')
        password = request.form.get("password")
        add_user(name, email, phone, password)
        
    return render_template('add_user.html')