# -*- coding: utf-8 -*-
"""
Created on Tue May 31 16:37:06 2016

@author: Varoon
"""

#factorial


def factorial(n):
    if n == 0:
        return 1
    else:
        return  n * factorial(n-1)
        
# Memoisation
def factorial2(n):
    x = [0]*(n+1)

    for i in range(n+1):
        if i == 0:
            x[i] = 1
        else:
            x[i] = i * x[i - 1]
        print x
    print x[n]    