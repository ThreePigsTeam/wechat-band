# -*- coding: utf-8 -*-

from flask import Flask, request, url_for,render_template
from wechat_sdk import WechatBasic
app = Flask(__name__)

localAddr = "183.173.41.88"
appID = "wx77e762983e6c2463"
appsecret = "96b447b1f7c4dbec926af2ab474edddc"
token = "asdfasdf"

ranklist = """<xml>
    <ToUserName><![CDATA[%s]]></ToUserName>
    <FromUserName><![CDATA[%s]]></FromUserName>
    <CreateTime>123456789</CreateTime>
    <MsgType><![CDATA[hardware]]></MsgType>
    <HardWare>
        <MessageView><![CDATA[myrank]]></MessageView>
        <MessageAction><![CDATA[ranklist]]></MessageAction>
    </HardWare>
    <FuncFlag>0</FuncFlag>
</xml>"""

wechat = WechatBasic(token = token, appid = appID, appsecret = appsecret)

def response_rank(source, target):
    return ranklist % (target, source)


@app.route('/', methods=['GET', 'POST'])
def index():
    print "gxd1"
    echostr = request.args.get("echostr", "")
    if (echostr != ""):
        print "echostr: ", echostr
        return echostr

    print "gxd2"
    signature = request.args.get("signature")
    timestamp = request.args.get("timestamp")
    nonce = request.args.get("nonce")
    body_text = request.data
    print "gxd3"
    print signature
    print timestamp
    print nonce
    print "======="
    print body_text
    print "======="
    # 对签名进行校验
    if wechat.check_signature(signature=signature, timestamp=timestamp, nonce=nonce):
        # 对 XML 数据进行解析 (必要, 否则不可执行 response_text, response_image 等操作)
        wechat.parse_data(body_text)
        # 获得解析结果, message 为 WechatMessage 对象 (wechat_sdk.messages中定义)
        message = wechat.get_message()

        
        if message.type == 'text':
            if message.content == 'wechat':
                response = wechat.response_text(u'^_^')
            elif message.content == u'运动数据':
                response = wechat.response_text(u'您今天的运动步数是14，今天的卡路里消耗是2000')
            elif message.content == u'新闻':
                response = wechat.response_news([
                    {
                        'title': u'第一条新闻标题',
                        'description': u'第一条新闻描述，这条新闻没有预览图',
                        'url': u'http://www.google.com.hk/',
                    }, {
                        'title': u'第二条新闻标题, 这条新闻无描述',
                        'picurl': u'http://doraemonext.oss-cn-hangzhou.aliyuncs.com/test/wechat-test.jpg',
                        'url': u'http://www.github.com/',
                    }, {
                        'title': u'第三条新闻标题',
                        'description': u'第三条新闻描述',
                        'picurl': u'http://doraemonext.oss-cn-hangzhou.aliyuncs.com/test/wechat-test.jpg',
                        'url': u'http://www.v2ex.com/',
                    }
                ])
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
                        'url': u'http://%s:5000%s' % (localAddr, url_for('step', openid = message.source))
                    }])
            elif message.key == 'SLEEP':
                response = wechat.response_text(u'您今天的睡眠时间是7h')
            elif message.key == 'RANK':
                response = response_rank(message.target, message.source)
                print "-------------rank"
                print response
                print ranklist
            else:
                response = wechat.response_text(u'wrong key.')
        else:
            response = wechat.response_text(u'未知')

        # 现在直接将 response 变量内容直接作为 HTTP Response 响应微信服务器即可，此处为了演示返回内容，直接将响应进行输出
        print "response: ========"
        print response
        print "========"
    print "get: "
    return response


@app.route('/hello/')
def hello():
    return 'Hello Word'

@app.route('/step/<openid>')
def step(openid):
    print 'step.........'
    return render_template('steps_num.html', today = 1000, goal = 100, data = [1,2,3,4,5,6,7])

with app.test_request_context():
    print url_for('index')
    print url_for('hello')
    print url_for('step', openid = 'gxd')

if __name__ == '__main__':
    app.run(host = '0.0.0.0', debug = True)


