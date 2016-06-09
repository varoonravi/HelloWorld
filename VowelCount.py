# -*- coding: utf-8 -*-
"""
Created on Tue May 31 14:44:34 2016

@author: Varoon
"""

#vowel count program
string = raw_input("Enter a string to check the vowel count\n")
count=0

for i in string:
    if i == 'a' or i == 'e' or i == 'o' or i == 'i' or i == 'u' :
        count += 1
    
print "The count of the vowels in "+string+" is " ,count
        
