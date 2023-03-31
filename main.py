import requests.cookies
from flask import *
from jinja2 import *

app = Flask(__name__)

file_loader = FileSystemLoader('templates')
env = Environment(loader=file_loader)
temmplate = env.get_template("index.html")

items = ['Ридли Скотт', 'Энди Уир', 'Марк Уотни',
                  'Венката Капур', 'Тедди Сандерс', 'Шон Бин']
@app.route('/')
@app.route('/distribution/')
def sample_file_upload():
    return render_template('index.html', items=items)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
