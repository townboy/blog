#! /usr/bin/evn python
# -*- coding:utf-8 -*-

import sys
import markdown
from bottle import jinja2_template
import settings
import StringIO

class article(object):
    def __init__(self, filename):
        self.filename = filename
        print filename
    
    def read(self):
        content = StringIO.StringIO()
        markdown.markdownFromFile(input = 'article/' + self.filename, \
                                   output = content, \
                                   extensions = ['codehilite'])
        return jinja2_template('templates/article.html', \
                               domain = settings.domain, \
                               article_content = content.getvalue().decode('utf-8'), \
                               title = self.read_title(), \
                               pub_time = self.read_time())
    def read_title(self):
        f = open('article/' + self.filename)
        f.readline()
        f.readline() 
        title = f.readline().decode('utf-8')[6:]
        return title[1 : -1]

    def read_time(self):
        f = open('article/' + self.filename)
        f.readline()
        f.readline()
        f.readline()
        return f.readline()[5:]
        

if __name__ == '__main__':
    read = article('2014-12-10-test.md')
    print read.read()
    print read.read_title()
