#! /usr/bin/evn python
# -*- coding:utf-8 -*-
from bottle import run,\
     route,\
     Bottle,\
     debug,\
     jinja2_template,\
     static_file
import sys
import codecs
import markdown
import settings
import os

import article

application = Bottle()
debug(True)

@application.route('/')
def index():
    art = os.listdir('./article')
    return jinja2_template('templates/home.html', domain = settings.domain, users = art)


@application.route('/test')
def test():
    return jinja2_template('templates/test.html', domain = settings.domain)

@application.route('/article/<artname>')
def func_article(artname):
    read = article.article(artname)
    return read.read()
    
   
@application.route('/static/<filename:path>')
def static(filename):
    return static_file(filename, root = './static')

if __name__ == '__main__':
    run(application, host = settings.host, port = settings.port)
