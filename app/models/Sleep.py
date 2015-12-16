# -*- coding: utf-8 -*-

from . import db


# 睡眠表
class Sleep(db.Model):
    __tablename__ = 'sleeps'
    id         = db.Column(db.Integer, primary_key = True)
    start_time = db.Column(db.DateTime, default = datetime.now())
    stop_time  = db.Column(db.DateTime, default = datetime.now())
    user_id    = db.Column(db.Integer, db.ForeignKey('users.id'))


