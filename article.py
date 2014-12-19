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

    def read(self):
        content = StringIO.StringIO()
        markdown.markdownFromFile(input = 'article/' + self.filename + '.md', \
                                            output = content)
        return jinja2_template('templates/article.html', \
                               domain = settings.domain, \
                               article_content = content.getvalue().decode('utf-8'))

if __name__ == '__main__':
    read = article('2014-02-10-i-am-dasan')
    print read.read()
