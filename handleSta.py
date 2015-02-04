#! /usr/bin/env/ python
#-*- coding:utf-8 -*-

import json
import random
import string
import os

class handleSta(object):

    def __init__(self):
        self.name = ''.join(random.sample(string.ascii_letters + string.digits, 8) )
        self.filename = 'statistics'
    
    def read(self):
        self.newdict = json.load(open(self.filename))

    def getValue(self, key, default):
        return self.newdict.get(key, default)

    def setValue(self, key, value):
        self.newdict[key] = value

    def write(self):
        fd = open(self.name, 'w')
        fd.write(json.dumps(self.newdict))
        fd.close()
        os.remove(self.filename)
        os.rename(self.name, self.filename)
     
if __name__ == '__main__':
    run = handleSta()
    run.read()
    run.write()
