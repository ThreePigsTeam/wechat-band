# -*- coding: utf-8 -*-

from wechat_sdk import WechatBasic

appID = "wx77e762983e6c2463"
appsecret = "96b447b1f7c4dbec926af2ab474edddc"
token = "asdfasdf"

wechat = WechatBasic(token = token, appid = appID, appsecret = appsecret)
def deleteMenu():
    print wechat.delete_menu()

if __name__ == '__main__':
    deleteMenu()