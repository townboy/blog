#! /usr/bin/env/ python
#-*- coding:utf-8 -*-

import json
import random
import string

class handleSta(object):

    shared = None
    
    def __init__(self):
        print string.ascii_letters
        print ''.join(random.sample(string.ascii_letters + string.digits, 8) )
    
    @classmethod
    def getInstance(self):
        if None == handleSta.shared:
            handleSta.shared = handleSta()
        return handleSta.shared

    def read(self, key, default):
        pass
    
    def get(self, key, default):
        pass


if __name__ == '__main__':
    print handleSta.getInstance()
