#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 22 04:01:50 2020

@author: rohyth
"""

import requests
from bs4 import BeautifulSoup
import pandas as pd


with requests.session() as c:
    f1 = c.get('https://forecast.weather.gov/MapClick.php?lat=34.099695000000054&lon=-118.33539999999999#.XscCAnUzZuQ',verify=False)
    s1 = BeautifulSoup(f1.content,'html.parser')
    
    #open('test.html',"wb").write(f1.content)
    #s1.find(id='seven-day-forecast-body').find_all(class_='forecast-tombstone')
    
    data = s1.find(id='seven-day-forecast-body').find_all(class_='tombstone-container')  
    
    # We get html content in form of a List
    '''
    period_name = data[0].find(class_='period-name').text # or use .get_text()
    short_desc = data[0].find(class_='short-desc').text
    temp = data[0].find(class_='temp').text
    
    '''
    # Using list Comprehension
    
    period_name = [d.find(class_='period-name').text for d in data]
    short_desc = [d.find(class_='short-desc').text for d in data]
    temp = [t.find(class_='temp').text for t in data]
     
    'Using Pandas for Data storage'
    weather_data = pd.DataFrame({
        'period':period_name,
        'Short-description':short_desc,
        'temperature':temp
        })   
    
print(weather_data)
weather_data.to_csv('weather.csv')    
    
    
    
    
    