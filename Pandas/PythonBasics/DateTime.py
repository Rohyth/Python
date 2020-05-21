#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 22 00:45:43 2020

@author: rohyth
"""


import datetime
import pytz
'''
datetime.date -> Y,M,D
datetime.time -> H,M,M,MS
datetime.datetime -> Y,M,S,h,m,s,ms
'''

today = datetime.date.today()
today
today.year
today.month
today.date
# Monday = 0 , Sunday = 6
today.weekday()

birthday = datetime.date(1992,10,26)
type(birthday)

Days = (today - birthday).days
Days

# Adding to date

tdelta = datetime.timedelta(days=10)
print(birthday - tdelta)


Current_time = datetime.datetime.now()
print(Current_time.time().hour)

timeDel = datetime.timedelta(hours=2)
print(Current_time - timeDel)


# Using pytz for timzome specific details
datetime.datetime.now().astimezone(pytz.timezone('Asia/Kolkata'))

#print time zones
for tz in pytz.all_timezones:
    print(tz)



# string formating with dates ------------------------------

today
# strftime -- here f stands for formatting
today.strftime('%B %d,%Y')


# strptime -- here p refers to parsing
x = today.strftime('%B %d,%Y')
formatted_Date = datetime.datetime.strptime(x,'%B %d,%Y')
formatted_Date

















