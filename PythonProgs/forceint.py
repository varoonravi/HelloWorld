# -*- coding: utf-8 -*-
"""
Created on Sun Jun 05 13:38:39 2016

@author: Varoon
"""


while True:
    try:
        num = input('Enter a valid integer \n')
        if isinstance(num , int):
            break
        else:
            print 'Oops!! , you have provided a wrong input, please try once again.'
    except NameError:
        print 'please focus maadi and try again'
print 'The number entered is ',num



