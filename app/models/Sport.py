# -*- coding: utf-8 -*-

from .. import db
from . import *
from datetime import *


# 运动表
class Sport(db.Model):
    __tablename__ = 'sports'
    id      = db.Column(db.Integer, primary_key = True)
    time    = db.Column(db.DateTime, default = datetime.now())
    total   = db.Column(db.Integer, default = 0, nullable = False)
    kind    = db.Column(db.Integer, nullable = False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))


# Sport

def add_sport(openid, time = datetime.now(), total = 0):
    pass


def get_sports(openid):
    pass


def get_sports_after(openid, time = datetime.now()):
    pass


# Sleep

def add_sleep(openid, start_time = datetime.now(), stop_time = datetime.now()):
    pass


def get_sleeps(openid):
    pass


def get_sleeps_after(openid, time = datetime.now()):
    pass

