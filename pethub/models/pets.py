from app import db

class Pet(db.Model):
    """ 定义了三个字段， 数据库表名为model名小写
    """
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.Integer)
    city = db.Column(db.String(64))
    age = db.Column(db.Integer)
    wechat = db.Column(db.String(32))
    email = db.Column(db.String(64))
    source = db.Column(db.Integer)
    status = db.Column(db.Integer)
    createtime = db.Column(db.String(32))
    host = db.Column(db.String(32))

    def __init__(self, username, email):
        self.username = username
        self.email = email

    def __repr__(self):
        return '<Pet %r>' % self.username
