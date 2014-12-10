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
def article(artname):
    print artname
    return jinja2_template('templates/test.html', domain = settings.domain)

@application.route('/static/<filename:path>')
def static(filename):
    return static_file(filename, root = './static')

if __name__ == '__main__':
    run(application, host = settings.host, port = settings.port)
