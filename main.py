import requests.cookies
from flask import *

app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
@app.route('/sample_file_upload', methods=['POST', 'GET'])
def sample_file_upload():
    if request.method == 'GET':
        return render_template('index.html')
    elif request.method == 'POST':
        f = request.files['file']
        with open('static/img/img.png', 'wb') as file:
            file.write(f.read())
        return "Форма отправлена"


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
