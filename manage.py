#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from app import create_app, db
from app.models import *
from flask.ext.script import Manager, Shell
from flask.ext.migrate import Migrate, MigrateCommand

COV = None
if os.environ.get('FLASK_COVERAGE'):
    import coverage
    COV = coverage.coverage(branch=True, include='app/*')
    COV.start()

app = create_app(os.getenv('FLASK_CONFIG') or 'default')
manager = Manager(app)
migrate = Migrate(app, db)


def make_shell_context():
    return dict(app = app, db = db, User = User, Step = Step, Rate = Rate, Sport = Sport, Sleep = Sleep, Pet = Pet, OriginalPet = OriginalPet, Nature = Nature, PetStage = PetStage)
manager.add_command("shell", Shell(make_context=make_shell_context))
manager.add_command('db', MigrateCommand)


@manager.command
def test(coverage=False):
    """Run the unit tests."""
    if coverage and not os.environ.get('FLASK_COVERAGE'):
        import sys
        os.environ['FLASK_COVERAGE'] = '1'
        os.execvp(sys.executable, [sys.executable] + sys.argv)
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)
    if COV:
        #COV.stop()
        COV.save()
        print('Coverage Summary:')
        COV.report()
        basedir = os.path.abspath(os.path.dirname(__file__))
        covdir = os.path.join(basedir, 'tmp/coverage')
        COV.html_report(directory=covdir)
        print('HTML version: file://%s/index.html' % covdir)
        COV.erase()


@manager.command
def insert_pet_info():
    #print 'inserting.......'
    f = open('pokemon_info.txt', 'r')
    index = 0
    for line in f.readlines():
        #print '+1'
        index += 1
        info = line.strip().split(' ')
        if info[0] == '0':
            add_original_pet(name = info[1], picture = '%.3d.png' % index, amount = info[-1])
            original_pet = OriginalPet.query.filter_by(name = info[1]).first()
            level_require = 0
        add_pet_stage(name = info[1], natures = info[2:len(info)-1], original_pet = original_pet, picture = '%.3d.png' % index, level_require = level_require)
        level_require += 10


@manager.command
def set_free_flag_true():
    for user in User.query.all():
        user.free_flag = True
        db.session.add(user)
    db.session.commit()


@manager.command
def set_free_flag_false():
    for user in User.query.all():
        user.free_flag = False
        db.session.add(user)
    db.session.commit()


@manager.command
def create_menu():
    from wechat_sdk import WechatBasic
    from config import wechat_config
    wechat = WechatBasic(token = wechat_config['token'], appid = wechat_config['appid'], appsecret = wechat_config['appsecret'])
    print wechat.create_menu({
        'button': [
            {
                'name': '个人',
                'sub_button': [
                    {
                        'type': 'click',
                        'name': '设备绑定',
                        'key' : 'SET_DEVICE'
                    },
                    {
                        'type': 'click',
                        'name': '信息维护',
                        'key' : 'SET_INFO'
                    },
                    {
                        'type': 'click',
                        'name': '排行榜',
                        'key' : 'GET_RANK'
                    },
                    {
                        'type': 'click',
                        'name': '宠物系统',
                        'key' : 'PET_SYS'
                    }
                ]
            },
            {
                'name': '运动',
                'sub_button': [
                    {
                        'type': 'click',
                        'name': '查看步数',
                        'key' : 'GET_STEP'
                    },
                    {
                        'type': 'click',
                        'name': '查看运动',
                        'key' : 'GET_SPORT'
                    },
                    {
                        'type': 'click',
                        'name': '添加运动',
                        'key' : 'ADD_SPORT'
                    },
                    {
                        'type': 'click',
                        'name': '查看目标',
                        'key' : 'GET_GOAL'
                    },
                    {
                        'type': 'click',
                        'name': '设定目标',
                        'key' : 'SET_GOAL'
                    }
                ]
            },
            {
                'name': '健康',
                'sub_button': [
                    {
                        'type': 'click',
                        'name': '查看睡眠',
                        'key' : 'GET_SLEEP'
                    },
                    {
                        'type': 'click',
                        'name': '心率曲线',
                        'key' : 'GET_RATE_CURVE'
                    },
                    {
                        'type': 'click',
                        'name': '当前心率',
                        'key' : 'GET_RATE_NOW'
                    },
                    {
                        'type': 'click',
                        'name': '查看卡路里',
                        'key' : 'GET_CALORIE'
                    }
                ]
            }
        ]})


if __name__ == '__main__':
    manager.run()
