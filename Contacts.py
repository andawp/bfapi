# __author__ = 'Administrator'
# coding=utf-8
# 微信企业号通讯录管理类
import utils, urllib2, json

TOKEN = utils.get_token()

# 部门类
class Department(object):
    def __init__(self, name, parentid, order=None):
        self.name = name
        self.parentid = parentid
        self.order = order

    # 创建部门
    def create(self):
        url = 'https://qyapi.weixin.qq.com/cgi-bin/department/create?access_token=' + TOKEN
        data = {
            "name": self.name,
            "parentid": self.parentid,
            "order": self.order
        }
        res = json.loads(urllib2.urlopen(url, data=data).read())
        return res

    # 更新部门
    @classmethod
    def update(cls, depart_id, name, parentid, order):
        url = 'https://qyapi.weixin.qq.com/cgi-bin/department/update?access_token='+ TOKEN
        data = {
            "id": int(depart_id),
            "name": name,
            "parentid": parentid,
            "order": order
        }
        res = json.loads(urllib2.urlopen(url, data=data).read())
        return res

    # 删除部门
    @classmethod
    def delete(cls, depart_id):
        url = 'https://qyapi.weixin.qq.com/cgi-bin/department/delete?access_token=' + TOKEN + '&id=' + depart_id
        res = json.loads(urllib2.urlopen(url).read())
        return res

    # 获取部门列表
    @classmethod
    def get_department_list(cls):
        url = 'https://qyapi.weixin.qq.com/cgi-bin/department/list?access_token=' + TOKEN
        res = json.loads(urllib2.urlopen(url).read())
        return res

class Contacts(object):
    def __init__(self):
        pass

    # 获取部门成员，返回一个list。
    @classmethod
    def get_dept_user_simplelist(cls, department_id, fetch_child=0, status=0):
        url = 'https://qyapi.weixin.qq.com/cgi-bin/user/simplelist?access_token=' + TOKEN + '&department_id=' \
              + department_id + '&fetch_child=' + fetch_child + '&status=' + status
        response = json.loads(urllib2.urlopen(url).read())['userlist']
        return response

    # 判断某个名字name是否在通讯录中，如果存在就返回用户id；否则就返回'0'。
    @classmethod
    def user_is_exist(cls, name):
        allusers = cls.get_dept_user_simplelist('1', '1', '0')
        allnames = [user['name'] for user in allusers]
        if allnames.count(name) == 0:
            return '0'
        return allusers[allnames.index(name)]['userid']

class User(object):
    def __init__(self, userid, name, department, position, mobile, email, weixinid, extattr ,avatar=None):
        self.userid = userid
        self.name = name
        self.department = department
        self.position = position
        self.mobile = mobile
        self.email = email
        self.weixinid = weixinid
        self.extattr = extattr
        self.avatar = avatar

    # 创建成员
    def create(self):
        url = 'https://qyapi.weixin.qq.com/cgi-bin/user/create?access_token=' + TOKEN
        data = {
            "userid": self.userid,
            "name": self.name,
            "department": self.department,
            "position": self.position,
            "mobile": self.mobile,
            "email": self.email,
            "weixinid": self.weixinid,
            "extattr": self.extattr
        }
        response = json.loads(urllib2.urlopen(url, data=data).read())
        return response

    # 更新成员
    def update(self):
        url = 'https://qyapi.weixin.qq.com/cgi-bin/user/update?access_token=' + TOKEN
        data = {
            "userid": self.userid,
            "name": self.name,
            "department": self.department,
            "position": self.position,
            "mobile": self.mobile,
            "email": self.email,
            "weixinid": self.weixinid,
            "extattr": self.extattr
        }
        response = json.loads(urllib2.urlopen(url, data=data).read())
        return response

    # 删除成员
    @classmethod
    def delete(cls, userid):
        url = 'https://qyapi.weixin.qq.com/cgi-bin/user/delete?access_token=' + TOKEN + '&userid=' + userid
        response = json.loads(urllib2.urlopen(url).read())
        return response

    # 批量删除成员
    @classmethod
    def batchdelete(cls, useridlist):
        url = 'https://qyapi.weixin.qq.com/cgi-bin/user/batchdelete?access_token=' + TOKEN
        data = {
            "useridlist": useridlist
        }
        response = json.loads(urllib2.urlopen(url, data=data).read())
        return response

    # 获取成员
    @classmethod
    def get_user(cls, userid):
        url = 'https://qyapi.weixin.qq.com/cgi-bin/user/get?access_token=' + TOKEN + '&userid=' + userid
        res = json.loads(urllib2.urlopen(url).read())
        return res

    # 获取部门成员
    @classmethod
    def get_department_simplelist(cls, department_id, fetch_child=1, status=0):
        url = 'https://qyapi.weixin.qq.com/cgi-bin/user/simplelist?access_token=' + TOKEN + '&department_id=' + department_id + '&fetch_child=' + fetch_child + '&status=' + status
        res = json.loads(urllib2.urlopen(url).read())
        return res

    # 获取部门成员(详情)
    @classmethod
    def get_department_userlist(cls, department_id, fetch_child=1, status=0):
        url = 'https://qyapi.weixin.qq.com/cgi-bin/user/list?access_token=' + TOKEN + '&department_id=' + department_id + '&fetch_child=' + fetch_child + '&status=' + status
        res = json.loads(urllib2.urlopen(url).read())
        return res

# 标签类
class Tag(object):
    def __init__(self, tagname, tagid=None):
        self.tagname = tagname
        self.tagid = tagid

    # 创建标签
    def create(self):
        url = 'https://qyapi.weixin.qq.com/cgi-bin/tag/create?access_token=' + TOKEN
        data = {
            "tagname": self.tagname
        }
        res = json.loads(urllib2.urlopen(url, data=data).read())
        return res

    # 更新标签
    @classmethod
    def update(cls, tagid, tagname):
        url = 'https://qyapi.weixin.qq.com/cgi-bin/tag/update?access_token=' + TOKEN
        data = {
            "tagid": tagid,
            "tagname": tagname
        }
        res = json.loads(urllib2.urlopen(url, data=data))
        return res

    # 删除标签
    @classmethod
    def delete(cls, tagid):
        url = 'https://qyapi.weixin.qq.com/cgi-bin/tag/delete?access_token=' + TOKEN + '&tagid=' + tagid
        res = json.loads(urllib2.urlopen(url).read())
        return res

    # 获取标签成员
    @classmethod
    def get_user(cls, tagid):
        url = 'https://qyapi.weixin.qq.com/cgi-bin/tag/get?access_token=' + TOKEN + '&tagid=' + tagid
        res = json.loads(urllib2.urlopen(url).read())
        return res

    # 增加标签成员
    @classmethod
    def add_user(cls, tagid, userlist=None, parytlist=None):
        if userlist is None and parytlist is None:
            return None
        url = 'https://qyapi.weixin.qq.com/cgi-bin/tag/addtagusers?access_token=' + TOKEN
        data = {
            "tagid": tagid,
            "userlist": userlist,
            "partylist": parytlist
        }
        res = json.loads(urllib2.urlopen(url, data=data).read())
        return res

    # 删除标签成员
    @classmethod
    def delete_user(cls, tagid, userlist=None, partylist=None):
        if userlist is None and partylist is None:
            return None
        url = 'https://qyapi.weixin.qq.com/cgi-bin/tag/deltagusers?access_token=' + TOKEN
        data = {
            "tagid": tagid,
            "userlist": userlist,
            "partylist": partylist
        }
        res = json.loads(urllib2.urlopen(url, data=data).read())
        return res

    # 获取标签列表
    @classmethod
    def get_taglist(cls):
        url = 'https://qyapi.weixin.qq.com/cgi-bin/tag/list?access_token=' + TOKEN
        res = json.loads(urllib2.urlopen(url).read())
        return res