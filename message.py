# __author__ = 'Administrator'
# coding:utf-8
# 微信企业号发送消息类
import bfapi, urllib, urllib2, json


class Message(object):
    def __init__(self, touser, toparty, totag, msgtype, agentid, safe, kw):
        self.msg = {
            "touser":touser,
            "toparty":toparty,
            "totag":totag,
            "msgtype":msgtype,
            "agentid":agentid,
            kw.keys()[0]: kw.values()[0],
            "safe":safe
        }

    def send(self):
        token = bfapi.get_token()
        url = 'https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token=' + token + '&debug=1'
        # 转换成json格式，不能urllib.urlencode
        data = json.dumps(self.msg)

        req = urllib2.Request(url, data=data)
        response = json.loads(urllib2.urlopen(req).read())
        return response['errmsg']