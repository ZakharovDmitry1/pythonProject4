import requests.cookies
from flask import *
from jinja2 import *

app = Flask(__name__)

file_loader = FileSystemLoader('templates')
env = Environment(loader=file_loader)
temmplate = env.get_template("index.html")


@app.route('/')
@app.route('/list_prof/<p>')
def sample_file_upload():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
