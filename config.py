# configurations
DATABASE = './tmp/band.db'
DEBUG = True
SECRET_KEY = 'development key'
USERNAME = 'admin'
PASSWORD = 'default'
localAddr = "59.66.139.102"
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