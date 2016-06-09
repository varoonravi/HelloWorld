# -*- coding: utf-8 -*-
"""
Created on Thu Jun 02 16:16:00 2016

@author: Varoon
"""
import sys
cnt = 0
for i in range(10):
    cnt += 1
    if cnt > 5:
        sys.exit(1)
    print "hello world"