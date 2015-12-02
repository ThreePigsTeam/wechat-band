#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from app import create_app, db
from app.models import *
from flask.ext.script import Manager, Shell
from flask.ext.migrate import Migrate, MigrateCommand

app = create_app(os.getenv('FLASK_CONFIG') or 'default')
manager = Manager(app)
migrate = Migrate(app, db)


def make_shell_context():
    return dict(app = app, db = db, User = User, Step = Step, Rate = Rate, Sport = Sport, Sleep = Sleep, Pet = Pet, OriginalPet = OriginalPet, Nature = Nature)
manager.add_command("shell", Shell(make_context=make_shell_context))
manager.add_command('db', MigrateCommand)


@manager.command
def test():
    """Run the unit tests."""
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)

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
