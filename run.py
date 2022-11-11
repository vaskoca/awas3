from flask import Flask

awas = Flask(__name__)


@awas.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    awas.run()