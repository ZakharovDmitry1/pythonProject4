import requests.cookies
from flask import *

app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
@app.route('/form_sample', methods=['POST', 'GET'])
def form_sample():
    if request.method == 'GET':
        return render_template('index.html')
    elif request.method == 'POST':
        with open('static/img/img.png', 'wb') as file:
            file.write(request.form['file'].read())
        return "Форма отправлена"


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
