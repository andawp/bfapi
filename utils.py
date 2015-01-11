__author__ = 'Peng'
# coding=utf-8
import bfapi
import json, urllib2, time,config

def get_token():
    if config.ACCESSTOKEN is '' or config.ACCESSTOKENTIME is '' or config.ACCESSTOKENTIME < time.time():
        url = str(config.TOKENURL) + 'corpid=' + str(config.CORPID) + '&corpsecret=' + str(config.CORPSECRET)
        content = json.loads(urllib2.urlopen(url).read())
        if 'access_token' in content:
            token = content['access_token']
            expires_in = content['expires_in'] + time.time()
            config.ACCESSTOKEN = token
            config.ACCESSTOKENTIME = expires_in
        else:
            raise Exception(message='Get AccessToken Failure!')
    else:
        token = config.ACCESSTOKEN
    return token