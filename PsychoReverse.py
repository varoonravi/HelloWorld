# -*- coding: utf-8 -*-
"""
Created on Tue May 31 15:10:23 2016

@author: Varoon
"""

string = 'Hello World!'
revString = string[::-1]
es = ''

l = revString.split()

rl = l[::-1]

for i in rl:
    es += i +' '
    
print es

    


    