from flask import Blueprint,render_template,current_app

bp = Blueprint('commoninfo',__name__)

@bp.route('/')
def index():
    return render_template('commoninfo/index.html')

@bp.route('/')
def shouyang():
    return render_template('commoninfo/index.html')

@bp.route('/')
def songyang():
    return render_template('commoninfo/index.html')

@bp.route('/')
def qiuzhu():
    return render_template('commoninfo/index.html')