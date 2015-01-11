# coding=utf-8
from flask import Flask, request
import urllib2,json, time, urllib, message, Contacts, random, string, uuid, os
from WXBizMsgCrypt import WXBizMsgCrypt

app = Flask(__name__)
app.config.from_pyfile('config.py')

@app.route('/')
def hello_world():
    return Contacts.User.get_user(Contacts.Contacts.user_is_exist('邓兴'))

@app.route('/gettoken')
def gettoken():
    return get_token() + str(app.config.get('ACCESSTOKENTIME'))

@app.route('/wzcx/v1.0/status')
def get_status():
    return 'Nomal!'

@app.route('/wxpush', methods=['GET', 'POST'])
def wxpush():
    if request.method == 'GET':
        return UrlVerify()
    else:
        msg_signature = urllib.quote(request.args.get('msg_signature'))
        timestamp = urllib.quote(request.args.get('timestamp'))
        nonce = urllib.quote(request.args.get('nonce'))
        # request.data不需要urllib.quote
        reqdate = request.data
        token = app.config.get('TXLTOKEN')
        encodingaeskey = app.config.get('TXLENCODINGAESKEY')
        corpid = app.config.get('CORPID')
        wxcpt = WXBizMsgCrypt(token, encodingaeskey, corpid)
        ret,sMsg = wxcpt.DecryptMsg(reqdate, msg_signature, timestamp, nonce)
        if ret != 0:
             print "ERR: DecryptMsg ret: " + str(ret)
        tree = ET.fromstring(sMsg)
        resmsg = message.Message("wangp", None, None, "text", "2", "0", {"text":{"content":tree.find(
            'Content').text}}).send()
        return resmsg

def UrlVerify():
    sToken = app.config.get('TXLTOKEN')
    sEncodingAESKey = app.config.get('TXLENCODINGAESKEY')
    sCorpID = app.config.get('CORPID')
    wxcpt = WXBizMsgCrypt(sToken, sEncodingAESKey, sCorpID)
    sVerifyMsgSig = urllib.unquote(request.args.get('msg_signature'))
    sVerifyTimeStamp = urllib.unquote(request.args.get('timestamp'))
    sVerifyNonce = urllib.unquote(request.args.get('nonce'))
    sVerifyEchoStr = urllib.unquote(request.args.get('echostr'))
    ret, echostr = wxcpt.VerifyURL(sVerifyMsgSig, sVerifyTimeStamp, sVerifyNonce,sVerifyEchoStr)
    print(echostr)
    if ret != 0:
        print "ERR: VerifyURL ret: " + ret
    return echostr

def make_resmessage(tousername, fromusername, createtime, msgtype, content, msgid, agentid, *args, **kw):
    root = ET.Element('xml')
    touser = ET.SubElement(root, 'ToUserName')
    touser.text = '<![CDATA[' + tousername + ']]>'
    fromuser = ET.SubElement(root, 'FromUserName')
    fromuser.text = '<![CDATA[' + fromusername + ']]>'
    crtime = ET.SubElement(root, 'CreateTime')
    crtime.text = createtime
    type = ET.SubElement(root, 'MsgType')
    type.text = '<![CDATA[' + msgtype + ']]>'
    cont = ET.SubElement(root, 'Content')
    cont.text = '<![CDATA[' + content + ']]>'
    mid = ET.SubElement(root, 'MsgId')
    mid.text = msgid
    aid = ET.SubElement(root, 'AgentID')
    aid.text = agentid
    return ET.tostring(root).replace('&lt;', '').replace('&gt;', '').replace(' ', '')

def get_token():
    if app.config.get('ACCESSTOKEN') is '' or app.config.get('ACCESSTOKENTIME') is '' or app.config.get('ACCESSTOKENTIME') < time.time():
        url = str(app.config.get('TOKENURL')) + 'corpid=' + str(app.config.get('CORPID')) + '&corpsecret=' + str(app.config.get('CORPSECRET'))
        content = json.loads(urllib2.urlopen(url).read())
        if 'access_token' in content:
            token = content['access_token']
            expires_in = content['expires_in'] + time.time()
            app.config.update(
                ACCESSTOKEN=token,
                ACCESSTOKENTIME=expires_in
            )
        else:
            raise Exception(message='Get AccessToken Failure!')
    else:
        token = app.config.get('ACCESSTOKEN')
    return token

# 随机生成sn_num个序列号，且不重复，并保持到sn_save_url文件中
def generate_sn(sn_num, sn_save_url):
    sn = set()
    while len(sn) < sn_num:
        sn.add(str(uuid.uuid4())[4:23])
    with open(sn_save_url, 'w') as fp:
        for ssn in sn:
            fp.write(str(ssn) + '\n')
    return str('Num:' + str(sn_num) + ' Sn_save_url:' + sn_save_url)

if __name__ == '__main__':
    app.run(host='192.168.0.57', port=80, debug=True)