# -*- coding: utf-8 -*-
"""
Created on Mon Jun 06 17:44:27 2016

@author: Varoon
"""
import random
def oneString(len):
    string = 'abcdefghijklmnopqrstuvwxyz '
    res = ''
    for i in range(len):
        res = res + string[random.randrange(27)]
        
    return res
    
    
def score():
    
   perNumber = 0
   resNumber = 0
   maxPercent = 0
   count = 0
   string = 'varoon'
   
   
   while resNumber != 1:
       count += 1
       perNumber = 0
       resNumber = 0
       rstring = oneString(len(string))
       for i,j in enumerate(rstring):
           if j == string[i]:
               perNumber += 1
       resNumber = perNumber / len(string)
       print rstring
       print resNumber
       if resNumber > maxPercent:
           maxPercent = resNumber
#       print count
   print 'The monkey took ' ,count , 'attempts to type correctly'    
    
def main():
    score()
    

if __name__ == '__main__':
    main()        
        