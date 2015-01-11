# __author__ = 'Administrator'
# coding:utf-8
# 微信企业号发送消息类
import bfapi, urllib, urllib2, json, utils


class Message(object):
    def __init__(self, touser, toparty, totag, msgtype, agentid, safe="0"):
        self.touser = touser
        self.toparty = toparty
        self.totag = totag
        self.msgtype = msgtype
        self.agentid = agentid
        self.safe = safe
        self._url = 'https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token=' + utils.get_token() + '&debug=1'

    def send(self, data):
        with urllib2.urlopen(self._url, data=data) as req:
            res = json.loads(req.read())
            return res


# textmessage, touser中多个用户用|隔开
class TextMessage(Message):
    def __init__(self, touser, toparty, totag, msgtype, agentid, content, safe="0"):
        super(TextMessage, self).__init__(touser, toparty, totag, msgtype, agentid, safe)
        self.content = content

    def send(self):
        data = {
            "touser": self.touser,
            "toparty": self.toparty,
            "totag": self.totag,
            "msgtype": "text",
            "agentid": self.agentid,
            "text": {
                "content": self.content
            },
            "safe": self.safe
        }
        return super(TextMessage, self).send(data=data)

class ImageMessage(Message):
    def __init__(self, touser, toparty, totag, msgtype, agentid, media_id, safe="0"):
        super(ImageMessage, self).__init__(touser, toparty, totag, msgtype, agentid, safe)
        self.media_id = media_id

    def send(self):
        data = {
            "touser": self.touser,
            "toparty": self.toparty,
            "totag": self.totag,
            "msgtype": self.msgtype,
            "agentid": self.agentid,
            "image": {
                "media_id": self.media_id
            },
            "safe": self.safe
        }
        super(ImageMessage,self).send(data=data)


class VoiceMessage(Message):
    def __init__(self, touser, toparty, totag, msgtype, agentid, media_id, safe="0"):
        super(VoiceMessage, self).__init__(touser, toparty, totag, msgtype, agentid, media_id, safe)
        self.media_id = media_id

    def send(self):
        data = {
            "touser": self.touser,
            "toparty": self.toparty,
            "totag": self.totag,
            "msgtype": self.msgtype,
            "agentid": self.agentid,
            "voice": {
                "media_id": self.media_id
            },
            "safe": self.safe
        }
        super(VoiceMessage, self).send(data=data)


class VideoMessage(Message):
    def __init__(self, touser, toparty, totag, msgtype, agentid, media_id, title, description, safe="0"):
        super(VideoMessage, self).__init__(touser, toparty, totag, msgtype, agentid, safe)
        self.media_id = media_id
        self.title = title
        self.description = description

    def send(self):
        data = {
            "touser": self.touser,
            "toparty": self.toparty,
            "totag": self.totag,
            "msgtype": self.msgtype,
            "agentid": self.agentid,
            "video":{
                "media_id": self.media_id,
                "title": self.title,
                "description": self.description
            },
            "safe": self.safe
        }
        super(VideoMessage, self).send(data=data)


class FileMessage(Message):
    def __init__(self, touser, toparty, totag, msgtype, agentid, media_id, safe="0"):
        super(FileMessage, self).__init__(touser, toparty, totag, msgtype, agentid, safe)
        self.media_id = media_id

    def send(self):
        data = {
            "touser": self.touser,
            "toparty": self.toparty,
            "totag": self.totag,
            "msgtype": self.msgtype,
            "agentid": self.agentid,
            "file": {
                "media_id": self.media_id
            },
            "safe": self.safe
        }
        super(FileMessage, self).send(data=data)


class NewsMessage(Message):
    def __init__(self, touser, toparty, totag, msgtype, agentid, articles, safe="0"):
        super(NewsMessage, self).__init__(touser, toparty, totag, msgtype, agentid, safe)
        self.news = articles

    def send(self):
        data = {
            "touser": self.touser,
            "toparty": self.toparty,
            "totag": self.totag,
            "msgtype": self.msgtype,
            "agentid": self.agentid,
            "news": {
                "articles": self.news
            },
            "safe": self.safe
        }
        super(NewsMessage, self).send(data=data)


class MpNewsMessage(Message):
    def __init__(self, touser, toparty, totag, msgtype, agentid, articles, safe="0"):
        super(MpNewsMessage, self).__init__(touser, toparty, totag, msgtype, agentid, safe)
        self.mpnews = articles

    def send(self):
        data = {
            "touser": self.touser,
            "toparty": self.totag,
            "totag": self.totag,
            "msgtype": self.msgtype,
            "agentid": self.agentid,
            "mpnews": {
                "articles": self.mpnews
            },
            "safe": self.safe
        }
        super(MpNewsMessage, self).send(data=data)