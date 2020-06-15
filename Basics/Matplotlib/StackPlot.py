#!/usr/bin/env python
# coding: utf-8

# In[6]:


import matplotlib.pyplot as plt
import random


# In[20]:


# Base Stack plot
plt.style.use('fivethirtyeight')

minutes = [i for i in range(1,10)]

bro1 = [random.randrange(1, 5, 1) for _ in range(9)]
bro2 = [random.randrange(1, 5, 1) for _ in range(9)]
bro3 = [random.randrange(1, 5, 1) for _ in range(9)]

labels = ['Bro1','Bro2','Bro3']

plt.stackplot(minutes,bro1,bro2,bro3,labels=labels)

# plt.legend()
#use loc method for locating legend anywhere in the graph

plt.legend(loc='upper left')
plt.title(' Stack Plot ')
plt.tight_layout()
plt.show()


# In[ ]:




