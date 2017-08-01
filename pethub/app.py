from flask import Flask,session,g,request,abort,render_template
from flask_session import Session
from blueprinter.commoninfo.commonview import bp
from flask_sql

import logging
from logging.handlers import RotatingFileHandler

app = Flask(__name__)
app.config.update(dict(EXPLAIN_TEMPLATE_LOADING=True))
app.config.from_pyfile('config.py')

app.register_blueprint(bp)


@app.errorhandler(404)
def not_handler(error):
    return 'url wrong'


def init_logger():
    handler = RotatingFileHandler('pethub.log', maxBytes=10000, backupCount=5)
    formatter = logging.Formatter(
        "[%(asctime)s] {%(pathname)s:%(lineno)d} %(levelname)s - %(message)s")
    handler.setFormatter(formatter)
    app.logger.addHandler(handler)
    app.logger.setLevel(logging.DEBUG)

if __name__ == "__main__":
    init_logger()
    app.run("0.0.0.0",port=8000)
