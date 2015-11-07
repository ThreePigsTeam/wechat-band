# -*- coding: utf-8 -*-

from flask import Flask, request
from wechat_sdk import WechatBasic
app = Flask(__name__)

appID = "wx77e762983e6c2463"
appsecret = "96b447b1f7c4dbec926af2ab474edddc"
token = "asdfasdf"
body_text = """
<xml>
<ToUserName><![CDATA[touser]]></ToUserName>
<FromUserName><![CDATA[fromuser]]></FromUserName>
<CreateTime>1405994593</CreateTime>
<MsgType><![CDATA[text]]></MsgType>
<Content><![CDATA[wechat]]></Content>
<MsgId>6038700799783131222</MsgId>
</xml>
"""

wechat = WechatBasic(token = token， appid = addID, appsecret = appsecret)
wechat.create_menu({
    'button':[
        {
            'type': 'click',
            'name': '今日歌曲',
            'key': 'V1001_TODAY_MUSIC'
        },
        {
            'type': 'click',
            'name': '歌手简介',
            'key': 'V1001_TODAY_SINGER'
        },
        {
            'name': '菜单',
            'sub_button': [
                {
                    'type': 'view',
                    'name': '搜索',
                    'url': 'http://www.soso.com/'
                },
                {
                    'type': 'view',
                    'name': '视频',
                    'url': 'http://v.qq.com/'
                },
                {
                    'type': 'click',
                    'name': '赞一下我们',
                    'key': 'V1001_GOOD'
                }
            ]
        }
    ]})

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
    # 实例化 wechat
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
                response = wechat.resonpse_text(u'您今天的运动步数是14，今天的卡路里消耗是2000')
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
        else:
            response = wechat.response_text(u'未知')

        # 现在直接将 response 变量内容直接作为 HTTP Response 响应微信服务器即可，此处为了演示返回内容，直接将响应进行输出
        print "response: ", response
    print "get: "
    return response


@app.route('/hello/')
def hello():
    return 'Hello Word'

if __name__ == '__main__':
    app.run(host = '0.0.0.0', debug = True)