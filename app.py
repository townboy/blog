#! /usr/bin/env python
# -*- coding:utf-8 -*-
from bottle import run,\
     route,\
     Bottle,\
     debug,\
     jinja2_template,\
     static_file,\
     error,\
     request
import sys
import codecs
import markdown
import settings
import os
import ip
import article
from paste import httpserver
import handleSta

application = Bottle()
debug(True)

@application.route('/')
def index():
    art = os.listdir('./article')
    give = []

    instance = handleSta.handleSta()
    instance.read()
    
    for item in art:
        path = './article/' + item
        read = article.article(path)
        instance.setValue(item, instance.getValue(item, 0) )
        give.append([item, read.read_title() + ' (' + read.read_time() + u'浏览  ' + str(instance.getValue(item, 0)) + ')'])
    give = sorted(give)[::-1]
    getIp = ip.ip().getIpInfo()

    instance.setValue('pv', instance.getValue('pv', 0) + 1)
    
    instance.write()
    return jinja2_template('templates/home.html', domain = settings.domain, users = give, ipInfo = getIp, pv = instance.getValue('pv', 0))

@application.route('/test')
def test():
    return jinja2_template('templates/test.html', domain = settings.domain)

@application.route('/article/<artname>')
def func_article(artname):
    instance = handleSta.handleSta()
    instance.read()
    instance.setValue(artname, instance.getValue(artname, 0) + 1)
    instance.setValue('pv', instance.getValue('pv', 0) + 1)
    instance.write()
    
    read = article.article('./article/' + artname)
    return read.read()
   
@application.route('/static/<filename:path>')
def static(filename):
    return static_file(filename, root = './static')

@application.route('/aboutme')
def aboutme():
    read = article.article('./special/aboutme.md')
    return read.read()

@application.error(404)
def error404(error):
    return'Nothing here, sorry'

if __name__ == '__main__':
    httpserver.serve(application, host = settings.host, port = settings.port)
