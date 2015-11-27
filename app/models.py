from . import db
from datetime import *


class User(db.Model):
    __tablename__ = 'users'
    id     = db.Column(db.Integer, primary_key = True)
    openid = db.Column(db.String(40), unique = True, index = True, nullable = False)
    goal   = db.Column(db.Integer, default = 10000)
    steps  = db.relationship('Step', backref='user', lazy='dynamic')
    rates  = db.relationship('Rate', backref='user', lazy='dynamic')
    def __repr__(self):
        return '<User %r>' % self.openid


class Step(db.Model):
    __tablename__ = 'steps'
    id      = db.Column(db.Integer, primary_key = True)
    date    = db.Column(db.Date, default = date.today())
    total   = db.Column(db.Integer, default = 0, nullable = False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))


class Rate(db.Model):
    __tablename__ = 'rates'
    id      = db.Column(db.Integer, primary_key = True)
    time    = db.Column(db.DateTime, default = datetime.now())
    total   = db.Column(db.Integer, default = 0, nullable = False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))


def get_goal_by_openid(openid):
    user = User.query.filter_by(openid = openid).first()
    print 'Goal == ', user.goal
    return user.goal


def get_steps_by_openid(openid):
    data = []
    user = User.query.filter_by(openid = openid).first()
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


def get_rate_now_by_openid(openid):
    return 89


def get_rates_by_openid(openid):
    data = []
    lowest = 10000
    highest = 0
    average = 0
    count = 0
    user = User.query.filter_by(openid = openid).first()
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



