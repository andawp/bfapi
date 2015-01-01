from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/wzcx/v1.0/status')
def get_status():
    return 'Nomal!'


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=80, debug=True)
