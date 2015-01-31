#! /usr/bin/env python
# -*- coding:utf-8 -*-

import urllib
from bottle import request
import json

class ip(object):
    def __init__(self):
        self.IPV4 = request.headers.environ['REMOTE_ADDR']
        self.USER_AGENT = request.headers.environ['HTTP_USER_AGENT']
        self.api = 'http://ip.taobao.com/service/getIpInfo.php?ip='
        
    def getIpInfo(self):
        #.decode('unicode-escape') 
        ret = []
        text = json.load( urllib.urlopen(self.api + self.IPV4) )
        if '1' == text['code']:
            return ['IP定位失败']
        ret.append(text['data']['ip'])
        if '' != text['data']['country']:
            location = text['data']['country'] + ' '
            location += text['data']['area'] + ' '
            location += text['data']['region'] + ' '
            location += text['data']['city'] + ' '
            location += text['data']['county']
            ret.append(location)

        if '' == text['data']['isp']:
            ret.append(text['data']['isp'])
        return ret
        
if __name__ == '__main__':
    run = ip()
    run.getIpInfo()
