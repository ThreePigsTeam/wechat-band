# -*- coding: utf-8 -*-

from .. import db
from . import *
from datetime import *


# 心率表
class Rate(db.Model):
    __tablename__ = 'rates'
    id      = db.Column(db.Integer, primary_key = True)
    time    = db.Column(db.DateTime, default = datetime.now())
    total   = db.Column(db.Integer, default = 0, nullable = False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))


# Rate

def add_rate(openid, data = 0):
    user = User.query.filter_by(openid = openid).first()
    if user == None:
        return 1
    time = datetime.now().replace(second = 0, microsecond = 0)
    time = time.replace(minute = time.minute - time.minute % 10)
    rate = user.rates.filter_by(time = time).first()
    if step == None:
        rate = Rate(time = time, total = 0, user = user)
    rate.total = data
    db.session.add(rate)
    db.session.commit()
    return 0


def get_rates_by_openid(openid):
    data = []
    lowest = 10000
    highest = 0
    average = 0
    count = 0
    user = User.query.filter_by(openid = openid).first()
    if user == None:
        return [], 0, 0, 0
    today = date.today()
    rates = user.rates.filter(Rate.time >= datetime(today.year, today.month, today.day)).order_by(Rate.time).all()
    ctime = datetime(today.year, today.month, today.day)
    j = 0
    while ctime <= datetime.now():
        if j >= len(rates) or rates[j].time > ctime:
            data.append(0)
        else:
            data.append(rate[j].total)
            lowest = min(lowest, rate[j].total)
            highest = max(highest, rate[j].total)
            average += rate[j].total
            count += 1
            j += 1
        ctime += timedelta(minutes = 10)
    if count > 0 :
        average /= count
    return data, average, highest, lowest


def get_rate_now_by_openid(openid):
    return 89

