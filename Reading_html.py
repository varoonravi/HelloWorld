## -*- coding: utf-8 -*-
#"""
#Created on Thu Jun 02 08:06:38 2016
#
#@author: Varoon
#"""

#x = '<tr align="right"><td>22</td><td>Zachary</td><td>Michelle</td>'


import codecs
import re

f = codecs.open(r'E:\Python Exercises\Google Exercises\google-python-exercises\google-python-exercises\babynames\baby1990.html','Ur')
l = []
for i in f:
    match = re.search(r'(\d+)</h3>' , i)
    if match:
        print 'In the year ' +match.group(1)



    match1 = re.search(r'<tr align="right"><td>(\d*)</td><td>(\w*)</td><td>(\w*)</td>',i)
    if match1:
         str1 ='Male: ' + match1.group(2)+' Female: '+match1.group(3)+' Rank: '+match1.group(1) 
         l.append(str1)
         
    
print l    
    


f.close()














