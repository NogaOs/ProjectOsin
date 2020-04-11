from database.db_def import User, Event

from database.funcs import add_event, add_user, user_login, get_user_info

from config.config import db, get_secret_key

from flask import Flask, render_template, request, redirect, url_for, session

from markupsafe import escape


app = Flask(__name__)
app.secret_key = b'\xa8\xa3\xf1T#*\xeb1\xbd[Jyz\nX\x0e$\x06\xc6\xf5#~p\xd8'


@app.route('/')
def index():
    if 'username' in session:
        return 'Logged in as %s' % escape(session['username'])
    return 'you are not logged in, yet.'


@app.route('/users/list')
def users_list():
    users_info = get_user_info()
    return render_template('users_list.html', items=users_info)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('full_name') 
        password = request.form.get('password') 
        if user_login(username, password):
            user_id, user_name = user_login(username, password)
            session['id'] = user_id
            session['username'] = user_name
            return redirect(url_for('index'))
        return 'login failed.'
    return render_template('login.html')


@app.route('/logout')
def logout():
    # remove the username from the session if it's there
    session.pop('username', None)
    return redirect(url_for('index'))


@app.route('/users/add', methods=["GET", "POST"]) 
def web_add_user():
    # in case the user pressed submit on the form
    if request.method == 'POST':  
        name = request.form.get('name')
        email = request.form.get('email')
        phone = request.form.get('phone')
        password = request.form.get("password")
        add_user(name, email, phone, password)
    return render_template('add_user.html')


@app.route('/events/add', methods=["GET", "POST"]) 
def web_add_event():
    if request.method == 'POST':  
        name = request.form.get('event_name')
        date = request.form.get('event_date')
        organized_by = request.form.get('team')
        comments = request.form.get('comments')
        add_event(name, date, organized_by, comments)
    return render_template('add_event.html')