# -*- coding: utf-8 -*-

from flask import render_template, session, redirect, url_for, current_app, request
from .. import db
from ..models import *
from . import main
from wechat_sdk import WechatBasic
from config import wechat_config, ranklist


def response_rank(source, target):
    return ranklist % (target, source)


def validate_register(sex, age, height, weight):
    return True


@main.route('/hello')
def hello():
    return 'hello, world'


@main.route('/', methods=['GET', 'POST'])
def index():
    echostr = request.args.get('echostr', '')
    if (echostr != ''):
        return echostr

    signature = request.args.get('signature')
    timestamp = request.args.get('timestamp')
    nonce = request.args.get('nonce')
    body_text = request.data
    print 'body======='
    print body_text
    print '========'
    wechat = WechatBasic(token = wechat_config['token'], appid = wechat_config['appid'], appsecret = wechat_config['appsecret'])
    # 对签名进行校验
    if wechat.check_signature(signature=signature, timestamp=timestamp, nonce=nonce):
        # 对 XML 数据进行解析 (必要, 否则不可执行 response_text, response_image 等操作)
        wechat.parse_data(body_text)
        message = wechat.get_message()
        openid = message.source
        
        if message.type == 'text':
            if message.content == 'wechat':
                response = wechat.response_text(u'^_^')
            else:
                response = wechat.response_text(u'文字')
        elif message.type == 'image':
            response = wechat.response_text(u'图片')
        elif message.type == 'click':
            if message.key == 'GET_STEP':
                response = wechat.response_news([{
                        'title': u'步数信息',
                        'url': u'http://%s:5000%s' % (wechat_config['localAddr'], url_for('main.step', openid = openid))
                    }])
            elif message.key == 'GET_RATE_CURVE':
                response = wechat.response_news([{
                        'title': u'心率曲线',
                        'url': u'http://%s:5000%s' % (wechat_config['localAddr'], url_for('main.rate', openid = openid))
                    }])
            elif message.key == 'GET_RATE_NOW':
                response = wechat.response_news([{
                        'title': u'当前心率',
                        'url': u'http://%s:5000%s' % (wechat_config['localAddr'], url_for('main.rate_now', openid = openid))
                    }])
            elif message.key == 'GET_RANK':
                response = response_rank(message.target, message.source)
                print ranklist
            elif message.key == 'SET_INFO':
                response = wechat.response_news([{
                        'title': u'信息维护',
                        'url': u'http://%s:5000%s' % (wechat_config['localAddr'], url_for('main.register', openid = openid))
                    }])
            elif message.key == 'ADD_SPORT':
                response = wechat.response_news([{
                        'title': u'添加运动',
                        'url': u'http://%s:5000%s' % (wechat_config['localAddr'], url_for('main.add_sport', openid = openid))
                    }])
            elif message.key == 'PET_SYS':
                response = wechat.response_news([{
                        'title': u'宠物系统',
                        'url': u'http://%s:5000%s' % (wechat_config['localAddr'], url_for('main.pet_welcome', openid = openid))
                    }])
            else:
                response = wechat.response_text(u'抱歉，这个功能还在开发中0 0')
        elif message.type == 'subscribe':
            response = wechat.response_text(u'雷吼！')
        else:
            response = wechat.response_text(u'未知')

        # 现在直接将 response 变量内容直接作为 HTTP Response 响应微信服务器即可
        print 'response: ========'
        print response
        print '========'
    return response


@main.route('/step/<openid>')
def step(openid):
    data = get_steps_by_openid(openid = openid)
    print 'data: ', data
    return render_template('steps_num.html', today = data[-1], goal = get_goal_by_openid(openid = openid), data = data)


@main.route('/rate/<openid>')
def rate(openid):
    data, average, highest, lowest = get_rates_by_openid(openid = openid)
    return render_template('heart_rate.html', average = average, highest = highest, lowest = lowest, data = data)


@main.route('/rate_now/<openid>')
def rate_now(openid):
    data = get_rate_now_by_openid(openid = openid)
    return render_template('heart_rate_now.html', data = data)


@main.route('/register/<openid>', methods=['GET', 'POST'])
def register(openid):
    if request.method == 'GET':
        return render_template('register.html')
    else:
        sex = request.form.get('gender')
        age = request.form.get('age')
        height = request.form.get('height')
        weight = request.form.get('weight')
        if validate_register(sex = sex, age = age, height = height, weight = weight):
            set_user(openid = openid, sex = sex, age = age, height = height, weight = weight)
            print '==================success'
            return render_template('register.html')
        else:
            return render_template('register.html')


@main.route('/add_sport/<openid>', methods = ['GET', 'POST'])
def add_sport(openid):
    if request.method == 'GET':
        return render_template('add_sports.html')
    else:
        time = request.form.get('date')
        return ''


@main.route('/pet_welcome/<openid>')
def pet_welcome(openid):
    return redirect(url_for('main.my_pet_list', openid = openid))


@main.route('/my_pet_list/<openid>')
def my_pet_list(openid):
    return render_template('my_pet_list.html')


@main.route('/my_pet_info/<openid>/<petid>')
def my_pet_info(openid, petid):
    pet = get_pet_by_openid_and_petid(openid = openid, petid = petid)
    pet_stages = [{'name' : stage.name, 'picutre' : stage.picture} for stage in pet.original_pet.pet_stages.all()]
    return render_template('my_pet_info.html', pet_stages = pet_stages,
                                                pet = {
                                                    'picture' : pet_stages[pet.stage]['picture'],
                                                    'name' : pet.name,
                                                    'sex' : pet.sex,
                                                    'natures' : [nature.name for nature in pet.original_pet.pet_stages.all()[pet.stage].natures],
                                                    'level' : pet.level,
                                                    'basic_cost' : pet.basic_cost,
                                                    'cur_exp' : pet_exp,
                                                    'req_exp' : 10000,
                                                    'cur_take' : False
                                                })


@main.route('/original_pet_list/<openid>')
def original_pet_list(openid):
    return render_template('original_pet_list.html')


@main.route('/original_pet_info/<openid>/<petid>')
def original_pet_info(openid, petid):
    return render_template('original_pet_info.html')


@main.route('/get_pet/<openid>')
def get_pet(openid):
    return render_template('get_pet.html')




