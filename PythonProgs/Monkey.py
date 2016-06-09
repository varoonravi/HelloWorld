# -*- coding: utf-8 -*-
"""
Created on Mon Jun 06 10:42:11 2016

@author: Varoon
"""


class myClass():
    def __init__(self, x, name):
        self.x = x
        self.name = name
    def __str__(self):
        #return "This is a obkect of type myClass" + str(self.x) + self.name
        return repr((self.name, self.x))
        
    