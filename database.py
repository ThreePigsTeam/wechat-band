# -*- coding: utf-8 -*-

import pickle

class Database:
    def __init__(self):
        dic = {}

    def init(self, db_path = 'db.txt'):
        db = open(db_path, 'rb')
        dic = pickle.load(db)
        db.close()

    def save(self, db_path = 'db.txt'):
        db = open('db.txt', 'wb')
        pickle.dump(dic, db)
        db.close()

    def get_user(self, openid):
        if openid in db:
            return db[openid]
        else:
            db[openid] = User(openid = openid)

class User:
    def __init__(self, openid, steps = [0, 0, 0, 0, 0, 0, 0], goal = 0):
        self.openid = openid
        self.steps = steps
        self.goal = goal