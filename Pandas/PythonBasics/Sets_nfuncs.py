#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 16 20:58:59 2020

@author: rohyth
"""

#Sets in python


l = [1,2,3,4,45,56,6,77,8,45]

#conversion to set 
#Use .add to add in sets
Alpha = set(l)
Alpha
l = list(Alpha)
l


# Example of Venn diagram . Function Union

lib_1 = {'Harry','Rohyth'}
lib_2 = {'Harry','Alpha','Beta'}

lib_1.union(lib_2) 

lib_1.intersection(lib_2)


diff1 = lib_1.difference(lib_2)
diff2 = lib_2.difference(lib_1)

print(diff1)