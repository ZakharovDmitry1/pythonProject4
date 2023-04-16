import datetime
import time

import sqlalchemy
from flask import Flask, request, render_template, make_response, redirect
from flask_login import LoginManager, login_user
from werkzeug.security import generate_password_hash

from data import db_session
from data.Department import Department
from data.LoginForm import LoginForm
from data.News import News
from data.jobs import Jobs
from data.users import User

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'
login_manager = LoginManager()
login_manager.init_app(app)
db_session.global_init('db/blogs.db')
db_sess = db_session.create_session()

print(generate_password_hash('123'))

@app.route('/')
def index():
    news = db_sess.query(News).filter(News.is_private != True)
    return render_template("main.html", news=news)

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template('register.html')
    elif request.method == 'POST':
        print(request.form['Login'])
        print(request.form['Password'])
        print(request.form['Repeat_password'])
        print(request.form['Surname'])
        print(request.form['Name'])
        print(request.form['Age'])
        print(request.form['Position'])
        print(request.form['Speciality'])
        print(request.form['Addess'])

        user = User()
        user.surname = request.form['Surname']
        user.name = request.form['Name']
        user.email = request.form['Login']
        user.position = request.form['Position']
        user.age = request.form['Age']
        user.address = request.form['Addess']
        user.speciality = request.form['Speciality']
        user.hashed_password = request.form['Password']

        db_sess.add(user)
        db_sess.commit()

        return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        user = db_sess.query(User).filter(User.email == form.email.data).first()
        user.check_password(form.password.data)
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember_me.data)
            return redirect("/")
        return render_template('index.html',
                               message="Неправильный логин или пароль",
                               form=form)
    return render_template('index.html', title='фигня', form=form)


@login_manager.user_loader
def load_user(user_id):
    db_sess = db_session.create_session()
    return db_sess.query(User).get(user_id)

@login_manager.user_loader
def load_user(user_id):
    db_sess = db_session.create_session()
    return db_sess.query(User).get(user_id)

def main():
    app.run(port=8080, host='127.0.0.1')



if __name__ == '__main__':
    main()
