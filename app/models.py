from . import db
from datetime import *


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


class Sport(db.Model):
    __tablename__ = 'sports'
    id      = db.Column(db.Integer, primary_key = True)
    time    = db.Column(db.DateTime, default = datetime.now())
    total   = db.Column(db.Integer, default = 0, nullable = False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))


class Sleep(db.Model):
    __tablename__ = 'sleeps'
    id         = db.Column(db.Integer, primary_key = True)
    start_time = db.Column(db.DateTime, default = datetime.now())
    stop_time  = db.Column(db.DateTime, default = datetime.now())
    user_id    = db.Column(db.Integer, db.ForeignKey('users.id'))


class Pet(db.Model):
    __tablename__ = 'pets'
    id      = db.Column(db.Integer, primary_key = True)
    age     = db.Column(db.Integer, default = 0, nullable = False)
    sex     = db.Column(db.String(10), default = 'male', nullable = False)
    hunger  = db.Column(db.Integer, default = 0, nullable = False)
    health  = db.Column(db.Integer, default = 100, nullable = False)
    status  = db.Column(db.String(20), default = 'fit', nullable = False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    

# User

def add_user(openid, goal = 10000, sex = 'Male', age = 20, height = 170, weight = 65):
    if User.query.filter_by(openid = openid).all() != []:
        return 1
    user = User(openid = openid, goal = goal)
    db.session.add(user)
    db.session.commit()
    return 0


def set_user(openid, goal = 10000, sex = 'Male', age = 20, height = 170, weight = 65):
    if add_user(openid = openid, goal = goal, sex = sex, age = age, height = height, weight = weight) == 0:
        return 0
    user = User.query.filter_by(openid = openid).first()
    user.goal = goal
    db.session.add(user)
    db.commit()
    return 0


def del_user(openid):
    user = User.query.filter_by(openid = openid).first()
    if user == None:
        return 1
    db.session.delete(user)
    db.commit()
    return 0


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


# Sport

def add_sport(openid, time = datetime.now(), total = 0):
    pass


# Goal

def get_goal_by_openid(openid):
    user = User.query.filter_by(openid = openid).first()
    if user == None:
        return 0
    print 'Goal == ', user.goal
    return user.goal








