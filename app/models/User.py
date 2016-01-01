# -*- coding: utf-8 -*-

from .. import db
from . import *


# 用户表
class User(db.Model):
    __tablename__ = 'users'
    id     = db.Column(db.Integer, primary_key = True)
    openid = db.Column(db.String(40), unique = True, index = True, nullable = False)
    sex    = db.Column(db.String(10))
    age    = db.Column(db.Integer)
    height = db.Column(db.Integer)
    weight = db.Column(db.Integer)
    goal   = db.Column(db.Integer, default = 10000)
    steps  = db.relationship('Step', backref='user', lazy='dynamic')
    rates  = db.relationship('Rate', backref='user', lazy='dynamic')
    sports = db.relationship('Sport', backref='user', lazy='dynamic')
    sleeps = db.relationship('Sleep', backref='user', lazy='dynamic')
    pets   = db.relationship('Pet', backref='user', lazy='dynamic')
    free_flag = db.Column(db.Boolean, default = False)
    def __repr__(self):
        return '<User %r>' % self.openid


# User


def get_free_flag(openid):
    user = User.query.filter_by(openid = openid).first()
    if user == None:
        return False
    return user.free_flag


def exist_user(openid):
    return (User.query.filter_by(openid = openid).first() != None)


def get_user_info_by_openid(openid):
    user = User.query.filter_by(openid = openid).first()
    if user == None:
        return None
    return {'sex': user.sex, 'age': user.age, 'height': user.height, 'weight': user.weight}


def add_user(openid, goal = 10000, sex = 'male', age = 20, height = 170, weight = 65):
    if User.query.filter_by(openid = openid).all() != []:
        return 1
    user = User(openid = openid, goal = goal, sex = sex, age = age, height = height, weight = weight)
    db.session.add(user)
    db.session.commit()
    return 0


def set_user(openid, goal = 10000, sex = 'male', age = 20, height = 170, weight = 65):
    if add_user(openid = openid, goal = goal, sex = sex, age = age, height = height, weight = weight) == 0:
        return 0
    user = User.query.filter_by(openid = openid).first()
    user.goal = goal
    user.sex = sex
    user.age = age
    user.height = height
    user.weight = weight
    db.session.add(user)
    db.session.commit()
    return 0


def del_user(openid):
    user = User.query.filter_by(openid = openid).first()
    if user == None:
        return 1
    db.session.delete(user)
    db.session.commit()
    return 0


# Goal

def get_goal_by_openid(openid):
    user = User.query.filter_by(openid = openid).first()
    if user == None:
        return 0
    #print 'Goal == ', user.goal
    return user.goal

