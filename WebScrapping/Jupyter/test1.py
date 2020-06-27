#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 25 19:15:03 2020

@author: rohyth
"""

from selenium import webdriver
 
# The place we will direct our WebDriver to
url = 'http://www.srcmake.com/'

# Creating the WebDriver object using the ChromeDriver
driver = webdriver.Chrome('/usr/bin/chromedriver')

# Directing the driver to the defined url
driver.get(url)


import webbrowser

webbrowser.open('http://example.com')
