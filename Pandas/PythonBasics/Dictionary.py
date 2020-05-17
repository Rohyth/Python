#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 16 21:32:54 2020

@author: rohyth
"""

# Dictionary 
grocery = {'Banana':5,'oranges':3}

print(grocery['Banana'])

print(grocery['oranges'])
#or
print(grocery.get('Banana'))
print(grocery.get('Hello')) # to check if not found


#----------------------------------------------------
#Important 

contacts = {
    'Rohit':['7290845646', 'Karol Bagh'],
    'Rohyth':['8954221891','Haridwar'],
    'Mom':['123456','Delhi']    
    }

print(contacts['Rohyth'])


#dict.items()
print(contacts.items())

#dict.key()
print(contacts.keys())

#dict.values()
print(contacts.values())


#Delete
print(contacts.pop('Mom'))


contacts
# Method to Add to dict
contacts['Soldi']=['456789','Gurgaon']

# example


test = {'Name':[]}
test
for i in range(10):
    test['Name'] = i
        
test

for i in range(10):
    test[i] = [i*10] 
    
test
test.pop('Name')
test

#test.clear()
#test











