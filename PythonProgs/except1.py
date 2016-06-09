# -*- coding: utf-8 -*-
"""
Created on Sun Jun 05 18:17:25 2016

@author: Varoon
"""

#checking out exception's arguments

try:
    print 'Inside try block'
    raise Exception('args1','args2')
except Exception as inst:
    print type(inst)
    print inst.args
    print inst
else:
    print 'Try has succeeded'
    
    
    
        