#!/usr/bin/env python
# coding: utf-8

# In[20]:


import matplotlib.pyplot as plt
import numpy as np
import random
import pandas as pd
from collections import Counter


# In[25]:


# importing data using pandas

data = pd.read_csv("/home/rohyth/Python/Pandas/Matplotlib/BarData.csv")
id = data['Responder_id']
languages = data['LanguagesWorkedWith']

language_counter = Counter()

for response in languages:
    language_counter.update(response.split(';'))


# In[30]:


lang = []
popularity = []

for item in language_counter.most_common(15):
    lang.append(item[0])
    popularity.append(item[1])


# In[33]:


plt.style.use('fivethirtyeight')

plt.bar(lang,popularity)


plt.title('Popularity of Languages')
plt.xlabel('languages')
plt.ylabel('Popularity')

plt.tight_layout()
plt.show()


# In[37]:


# horizontal bar using barh
plt.style.use('fivethirtyeight')

# use reverse function 
lang.reverse()
popularity.reverse()

plt.barh(lang,popularity)


plt.title('Popularity of Languages')
#plt.xlabel('languages')
plt.xlabel('Popularity')

plt.tight_layout()
plt.show()


# In[ ]:




