from flask import Flask,session,g,request,abort,render_template
from flask_session import Session

import logging
from logging.handlers import RotatingFileHandler

import sqlite3
""" this app is a flask demo"""

app = Flask(__name__)
app.config.from_pyfile('config.py')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/wel')
def wel():
    if not session.get('name'):
        abort(404)
    return session.get('name')

@app.errorhandler(404)
def not_handler(error):
    return 'url wrong'


def init_logger():
    handler = RotatingFileHandler('foo.log', maxBytes=10000, backupCount=1)
    formatter = logging.Formatter(
        "[%(asctime)s] {%(pathname)s:%(lineno)d} %(levelname)s - %(message)s")
    handler.setFormatter(formatter)
    app.logger.addHandler(handler)
    app.logger.setLevel(logging.DEBUG)

if __name__ == "__main__":
    init_logger()
    app.run("0.0.0.0",port=8000)
