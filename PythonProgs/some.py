# -*- coding: utf-8 -*-
"""
Created on Sun Jun 05 19:27:12 2016

@author: Varoon
"""

class SomeException(Exception):
    def __init__(self,value):
        self.value = value
    def __string__(self):
        return repr(self.value)
        
        
        
        
        
try:
    raise SomeException("ha ha exception")
except SomeException as e:
    e.args
    raise