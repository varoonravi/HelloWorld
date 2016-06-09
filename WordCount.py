# -*- coding: utf-8 -*-
"""
Created on Tue May 31 14:39:42 2016

@author: Varoon
"""

#word count program

l=['apple','banana','mango','orange','apple','apple','banana','mango','grapes']
dictionary={}

for i in l:
    if i in dictionary:
        dictionary[i]  += 1
    else:
        dictionary[i] = 1
        
print dictionary