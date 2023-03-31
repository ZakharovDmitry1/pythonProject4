import requests.cookies
from flask import *
from jinja2 import *

app = Flask(__name__)

file_loader = FileSystemLoader('templates')
env = Environment(loader=file_loader)
temmplate = env.get_template("index.html")

items = "инженер-исследователь, пилот, строитель, экзобиолог, врач," \
        " инженер по терраформированию, климатолог, специалист по радиационной защите," \
        " астрогеолог, гляциолог, инженер жизнеобеспечения, метеоролог, оператор марсохода," \
        " киберинженер, штурман, пилот дронов".split(', ')


@app.route('/')
@app.route('/list_prof/<p>')
def sample_file_upload(p=''):
    return render_template('index.html', items=items, list=p)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
