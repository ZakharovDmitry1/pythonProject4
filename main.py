import requests.cookies
from flask import *
from jinja2 import *

app = Flask(__name__)

file_loader = FileSystemLoader('templates')
env = Environment(loader=file_loader)
temmplate = env.get_template("index.html")


@app.route('/')
@app.route('/training/<prof>')
def sample_file_upload(prof='hi'):
    if prof.find('строитель') != -1:
        return temmplate.render(title=prof, title2='Научные симуляторы', number=0)
    elif prof.find('инженер') != -1:
        return temmplate.render(title=prof, title2='Инженерные тренажеры', number=1)
    else:
        return temmplate.render(title=prof, title2='Работа дворником', number=2)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
