# -*- coding: utf-8 -*-

# imports
from contextlib import closing
import sqlite3
from flask import g, abort

def getStepsByOpenid(openid):
    data = []
    for day in range(7):
        cur = g.db.execute("SELECT total_steps FROM steps WHERE openid = '%s' AND day = date('now', '-%d day')" % (openid, 6-day))
        rows = cur.fetchall()
        if (len(rows) == 0):
            data.append(0)
        else:
            data.append(rows[0][0])
    print "data:", data
    return data

def getRatesByOpenid(openid):
    cur = g.db.execute("SELECT total_rates, day FROM heart_rates WHERE openid = '%s' ORDER BY day" % openid)
    #print cur.fetchall()
    rates = [row[0] for row in cur.fetchall()]
    data = [int(rate) for rate in rates[-1].split(',')]
    return data

def getGoalByOpenid(openid):
    cur = g.db.execute("SELECT goal FROM users WHERE openid = '%s'" % openid)
    res = cur.fetchall()
    if (len(res) == 0):
        return 0
    else:
        return res[0][0]

def updateStepByOpenid(openid, step):
    pass

def updateRateByOpenid(openid, rate):
    pass
