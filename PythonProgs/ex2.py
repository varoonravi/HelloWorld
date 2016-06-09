# -*- coding: utf-8 -*-
"""
Created on Fri Jun 03 12:01:03 2016

@author: Varoon
"""

#remeber . is a current working directory

import os
import sys
import os.path


def listDirectories(dir_name):
    l = os.listdir(dir_name)
    for i in l:
       print i
       print os.path.join(dir_name,i)
       print os.path.abspath(os.path.join(dir_name,i)) + '-----abs path----'
       print os.path.isdir(dir_name)

if __name__ == '__main__':
    listDirectories(sys.argv[1])