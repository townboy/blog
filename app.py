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
from paste import httpserver

application = Bottle()
debug(True)

@application.route('/')
def index():
    art = os.listdir('./article')

    give = []
    for item in art:
        read = article.article(item)
        give.append([item, read.read_title() + ' (' + read.read_time() + ')'])
    
    return jinja2_template('templates/home.html', domain = settings.domain, users = give)

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

@application.route('/aboutme')
def aboutme():
    read = article.article('aboutme.md')
    return read.read()

if __name__ == '__main__':
    httpserver.serve(application, host = settings.host, port = settings.port)
