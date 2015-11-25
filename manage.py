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
    return dict(app=app, db=db, User=User, Step=Step, Rate=Rate)
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
        'button':[
            {
                'type': 'click',
                'name': '步数',
                'key': 'STEP'
            },
            {
                'type': 'click',
                'name': '心率',
                'key': 'HEART'
            },
            {
                'type': 'click',
                'name': '排行',
                'key': 'RANK'
            }
        ]})


if __name__ == '__main__':
    manager.run()
