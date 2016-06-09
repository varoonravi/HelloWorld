# -*- coding: utf-8 -*-
"""
Created on Tue May 31 14:55:34 2016

@author: Varoon
"""

string = 'new year is celebrated on Jan 1st every year'
upperCase=0
lowerCase=0
spaces=0
digits=0

for i in string:
    if i.isupper():
        upperCase += 1
        continue
    elif i.islower():
        lowerCase += 1
        continue
    elif i.isspace():
        spaces += 1
        continue
    elif i.isdigit():
        digits +=1
        continue
        
print "In the string \""+string+"\" there are ",upperCase , lowerCase , spaces , digits
        