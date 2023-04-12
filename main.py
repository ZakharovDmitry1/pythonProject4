import datetime

import sqlalchemy
from flask import Flask, request, render_template

from data import db_session
from data.jobs import Jobs
from data.users import User

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blogs.db'
db_session.global_init("db/blogs.db")
db_sess = db_session.create_session()

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html')
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

        return render_template('index.html')


def main():
    app.run(port=8080, host='127.0.0.1')



if __name__ == '__main__':
    main()
