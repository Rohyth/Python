#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 22 21:59:52 2020

@author: rohyth
"""

# Using zip functions

l1 = [1,2,3,4]
l2 = ['One','Two','Three','four']

'Only zips lists with equal number of arguments/items'
zipped = list(zip(l1,l2))
print('zipped1',zipped)

'trying on three lists'
l1 = [1,2,3,4]
l2 = ['One','Two','Three','four']
l3 = ['Alpha','beta','gama','neo']


'Only zips lists with equal number of arguments/items'
'Ignores extra arguments--------------------------'

zipped2 = list(zip(l1,l2,l3))
print()
print('zipped2',zipped2)


'--------------------------------------------------------'
'Unzipping function -------------------------------------'

'for unzipping , the func remains the same but an * is added '


unzipped = list(zip(*zipped2))
print()
print(unzipped)


'using python way to loop using zip'

print()
for (ls1,ls2) in zip(l1,l2):
    print(ls1)
    print(ls2)


print()
'Example to zip and form sentence-----------------------------------'

fruits = ['Apple','Banana','Grapes']
counts = [3,5,7]
prices = [10,20,25]

sentences = []
for (fruit,count,price) in zip(fruits,counts,prices):
    sentences.append('i purchased ' + str(count) + ' ' + fruit +' in Rs.' + str(count*price))

print(sentences)











































