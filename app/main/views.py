# -*- coding: utf-8 -*-

from flask import render_template, session, redirect, url_for, current_app, request
from .. import db
from ..models import *
from . import main
from wechat_sdk import WechatBasic
from config import wechat_config, ranklist

def response_rank(source, target):
    return ranklist % (target, source)

@main.route('/', methods=['GET', 'POST'])
def index():
    echostr = request.args.get("echostr", "")
    if (echostr != ""):
        return echostr

    signature = request.args.get("signature")
    timestamp = request.args.get("timestamp")
    nonce = request.args.get("nonce")
    body_text = request.data
    print "body======="
    print body_text
    print "========"
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
                response = wechat.response_news([
                    {
                        'title': u'步数信息',
                        'url': u'http://%s:5000%s' % (wechat_config['localAddr'], url_for('main.step', openid = openid))
                    }])
            elif message.key == 'GET_RATE_CURVE':
                response = wechat.response_news([
                    {
                        'title': u'心率曲线',
                        'url': u'http://%s:5000%s' % (wechat_config['localAddr'], url_for('main.rate', openid = openid))
                    }])
            elif message.key == 'GET_RATE_NOW':
                response = wechat.response_news([
                    {
                        'title': u'当前心率',
                        'url': u'http://%s:5000%s' % (wechat_config['localAddr'], url_for('main.rate_now', openid = openid))
                    }])
            elif message.key == 'GET_RANK':
                response = response_rank(message.target, message.source)
                print ranklist
            else:
                response = wechat.response_text(u'wrong key.')
        elif message.type == 'subscribe':
            response = wechat.response_text(u'雷吼！')
        else:
            response = wechat.response_text(u'未知')

        # 现在直接将 response 变量内容直接作为 HTTP Response 响应微信服务器即可
        print "response: ========"
        print response
        print "========"
    return response

@main.route('/step/<openid>')
def step(openid):
    data = get_steps_by_openid(openid = openid)
    print "data: ", data
    return render_template('steps_num.html', today = data[-1], goal = get_goal_by_openid(openid = openid), data = data)

@main.route('/rate/<openid>')
def rate(openid):
    data, average, highest, lowest = get_rates_by_openid(openid = openid)
    print "heart: ", data
    print "ave: ", sum(data) / len(data)
    print "max: ", max(data)
    print "min: ", min(data)
    return render_template('heart_rate.html', average = average, highest = highest, lowest = lowest, data = data)

@main.route('/rate_now/<openid>')
def rate_now(openid):
    #data = getRatesByOpenid(openid = openid)
    return render_template('heart_rate_now.html', data = 1000)
