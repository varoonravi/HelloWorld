# -*- coding: utf-8 -*-
"""
Created on Tue May 31 19:22:04 2016

@author: Varoon
"""
#
#l=['hello','who','dont','know']
#
#for i in l:
#    print l[-1:] #this is how to get the last element in the list 
    
    
    #dynamic programming for factorial

def factorial(n):
    l = [0] * (n+1)
    
    for i in range(n+1):
        if i == 0:
            l[i] = 1
        else:
            l[i] = i * l[i-1]
    print l[i]        

    
    
    
                #dynamic programming