# -*- coding: utf-8 -*-

from .. import db
from . import *
from datetime import *


# 步数表
class Step(db.Model):
    __tablename__ = 'steps'
    id      = db.Column(db.Integer, primary_key = True)
    date    = db.Column(db.Date, default = date.today())
    total   = db.Column(db.Integer, default = 0, nullable = False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))


# Step

def add_step(openid, data = 0):
    user = User.query.filter_by(openid = openid).first()
    if user == None:
        return 1
    step = user.steps.filter_by(date = date.today()).first()
    if step == None:
        step = Step(date = date.today(), total = 0, user = user)
    step.total += data
    db.session.add(step)
    db.session.commit()
    return 0


def get_steps_by_openid(openid):
    data = []
    user = User.query.filter_by(openid = openid).first()
    if user == None:
        return [0, 0, 0, 0, 0, 0, 0]
    steps = user.steps.filter(Step.date > date.today() - timedelta(days = 7)).order_by(Step.date).all()
    cdate = date.today() - timedelta(days = 6)
    j = 0
    for i in range(7):
        if j >= len(steps) or steps[j].date != cdate:
            data.append(0)
        else:
            data.append(steps[j].total)
            j += 1
        cdate += timedelta(days = 1)
    return data

