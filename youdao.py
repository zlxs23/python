# -*- coding: utf-8 -*-

import urllib2
import json

# 这里最大问题 即 仅仅支持 py2
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

def youdao(word):
    qword = urllib2.quote(word)
    ID = '你的 id'
    KEY = '你的 key'
    baseurl = r'http://fanyi.youdao.com/openapi.do?keyfrom=' + ID + '&key=' + KEY + '&type=data&doctype=json&version=1.1&q='
    url = baseurl+qword
    resp = urllib2.urlopen(url)
    resp.encoding = 'utf-8'
    fanyi = json.loads(resp.read())
    if fanyi['errorCode'] == 0:
        if 'basic' in fanyi.keys():
            trans = u'%s:\n%s\n%s\nWeb Explanation:\n%s' % (fanyi['query'], ''.join(fanyi['translation']), ''.join(
                fanyi['basic']['explains']), ''.join(fanyi['web'][0]['value']))
            print trans
        else:
            trans = u'%s:\nBase Translation:%s\n' % (
                fanyi['query'], ''.join(fanyi['translation']))
            print trans
    else:
        return u'Sorry,Spelling %s is Error...[ErrorCode is %s]' % (word, fanyi['errorCode'])