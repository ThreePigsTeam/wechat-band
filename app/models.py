from . import db
from datetime import *


class User(db.Model):
    __tablename__ = 'users'
    id     = db.Column(db.Integer, primary_key = True)
    openid = db.Column(db.String(40), unique = True, index = True, nullable = False)
    goal   = db.Column(db.Integer, default = 10000)
#    steps  = db.relationship('Step', backref='user', lazy='dynamic')
    def __repr__(self):
        return '<User %r>' % self.openid

class Step(db.Model):
    __tablename__ = 'steps'
    id      = db.Column(db.Integer, primary_key = True)
    date    = db.Column(db.Date, default = date.today())
    total   = db.Column(db.Integer, default = 0, nullable = False)
#    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
