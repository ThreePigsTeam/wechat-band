# -*- coding: utf-8 -*-

from flask import render_template, session, redirect, url_for, current_app, request
from .. import db
from ..models import *
from . import main
from wechat_sdk import WechatBasic
from config import wechat_config, ranklist

def response_rank(source, target):
    return ranklist % (target, source)

@main.route('/hello')
def hello():
    return "hello, world"

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
        # 获得解析结果, message 为 WechatMessage 对象 (wechat_sdk.messages中定义)
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
            print '----------click'
            if message.key == 'STEP':
                response = wechat.response_news([
                    {
                        'title': u'步数信息',
                        'url': u'http://%s:5000%s' % (wechat_config['localAddr'], url_for('main.step', openid = openid))
                    }])
            elif message.key == 'HEART':
                response = wechat.response_news([
                    {
                        'title': u'心率信息',
                        'url': u'http://%s:5000%s' % (wechat_config['localAddr'], url_for('main.heart', openid = openid))
                    }])
            elif message.key == 'RANK':
                response = response_rank(message.target, message.source)
                print "-------------rank"
                print response
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
    #print wechat_config
    #data = [1,2,3,4,5,6,7]
    print "data: ", data
    return render_template('steps_num.html', today = data[-1], goal = get_goal_by_openid(openid = openid), data = data)

@main.route('/heart/<openid>')
def heart(openid):
    #data = getRatesByOpenid(openid = openid)
    data = []
    print "hear: ", data
    print "ave: ", sum(data) / len(data)
    print "max: ", max(data)
    print "min: ", min(data)
    return render_template('heart_rate.html', average = sum(data)/len(data), highest = max(data), lowest = min(data), data = data)
