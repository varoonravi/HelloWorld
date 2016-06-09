# -*- coding: utf-8 -*-
"""
Created on Wed Jun 01 23:12:33 2016

@author: Varoon
"""

import re

string = 'hhhhhllo bro, he this is just a test strinng'

match = re.search(r'\bword\b',string)
if match:
    print 'Match found ', match.group()
else:
    print 'Match not found'
    
print match.group()