from flask import *

app = Flask(__name__)


@app.route('/')
@app.route('/astronaut_selection')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
