from bottle import *

@route('/')
def index():
    return 'hello kitty'

run(host = 'localhost', port = 8080)
