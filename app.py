from bottle import run, route

@route('/')
def index():
    return 'hello kitty'

run(host = 'localhost', port = 8080)
