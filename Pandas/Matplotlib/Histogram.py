#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import matplotlib.pyplot as plt
import random


# In[19]:


data = pd.read_csv('./BarData.csv')
xdata = random.sample(range(10,60),11)
xdata.sort()


# In[24]:


# Histogram Example

plt.style.use('fivethirtyeight')
# use bins to define total number of bars required
bins = [0,20,30,40,50,60]

plt.hist(xdata, bins=bins, edgecolor='black')

plt.title('Ages of respondents')
plt.xlabel('Ages')
plt.ylabel('Total respondants')
plt.tight_layout()
plt.show()


# In[35]:


# Histogram with loading data
plt.style.use('fivethirtyeight')

ids = data['Responder_id']
ages = []
for i in range(0,87569):
    ages.append(random.randint(10,100))
    
ages.sort()

bins = [10,20,30,40,50,60,70,80,90,100]

plt.hist(ages,bins=bins, edgecolor='black')

plt.title('Ages of respondents')
plt.xlabel('Ages')
plt.ylabel('Total respondants')
plt.tight_layout()
plt.show()


# In[38]:


# Histogram with median age line 
plt.style.use('fivethirtyeight')

ids = data['Responder_id']
ages = []
for i in range(0,87569):
    ages.append(random.randint(10,100))
    
ages.sort()

bins = [10,20,30,40,50,60,70,80,90,100]

plt.hist(ages,bins=bins, edgecolor='black', log=True)

median_age = 29
color = 'red'

plt.axvline(median_age,color=color, label='median age')

plt.legend()
plt.title('Ages of respondents')
plt.xlabel('Ages')
plt.ylabel('Total respondants')
plt.tight_layout()
plt.show()


# In[39]:


# In[ ]:




