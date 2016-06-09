# -*- coding: utf-8 -*-
"""
Created on Wed Jun 01 22:31:04 2016

@author: Varoon
"""

#word count from file

f = open('C:\Users\Varoon\Desktop\Checking.txt','r')
words = {}
for line in f:
    for word in line.split():
        if word in words:    
            words[word] += 1
        else:
            words[words] = 1
        
#print d

for k,v in word.items():
    print 'The word '+k+' has occured '+str(v)+' times, in the document Checking.txt'
    
    
