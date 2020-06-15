#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 10:36:30 2020

@author: rohyth
"""

# List
A = []
A = [1,2,3]
A.append(5)
A

# use .append to add into list
Names = ['Rohit','Ravi','Ritu']
Names.append('Nupur')
Names

# Use .insert to add data at specific location 
Names.insert(1, 'Bhanu')
Names

Names.remove('Bhanu')
Names

Names.reverse()
Names

lst =  [1,2,3,59,65,22,44,100]
lst
lst.sort()
lst

for l in lst:
    print(l)