# -*- coding: utf-8 -*-

from .. import db
from . import *
from datetime import *


# 睡眠表
class Sleep(db.Model):
    __tablename__ = 'sleeps'
    id         = db.Column(db.Integer, primary_key = True)
    start_time = db.Column(db.DateTime, default = datetime.now())
    stop_time  = db.Column(db.DateTime, default = datetime.now())
    user_id    = db.Column(db.Integer, db.ForeignKey('users.id'))


# Sleep

def add_sleep(openid, start_time = datetime.now(), stop_time = datetime.now()):
    pass


def get_sleeps(openid):
    pass


def get_sleeps_after(openid, time = datetime.now()):
    pass

