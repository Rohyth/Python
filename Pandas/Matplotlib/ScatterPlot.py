#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import matplotlib.pyplot as plt
import random


# In[26]:


# Scatter Plot
plt.style.use('seaborn')

x = [random.randint(1,9) for i in range(15)]
y = [random.randint(1,9) for j in range(15)]

'marker="X"'
plt.scatter(x,y, s=100, c='green', edgecolor='black', linewidths=1, alpha=0.75)


plt.title('Scatter Plot')

plt.tight_layout()
plt.show()


# In[28]:


# Scatter Plot
plt.style.use('seaborn')

colors = [random.randint(1,9) for j in range(15)]

'marker="X"'
plt.scatter(x,y, s=100, c=colors, edgecolor='black', linewidths=1, alpha=0.75)

plt.title('Scatter Plot')

plt.tight_layout()
plt.show()


# In[32]:


# Scatter Plot
plt.style.use('seaborn')


'marker="X"'
plt.scatter(x,y, s=100, c=colors,cmap='Greens' ,edgecolor='black', linewidths=1, alpha=0.75)

plt.title('Scatter Plot')

plt.tight_layout()
plt.show()


# In[35]:


# Scatter Plot
plt.style.use('seaborn')

colors = [random.randint(1,9) for j in range(15)]

'marker="X"'
plt.scatter(x,y, s=100, c=colors,cmap='Greens', edgecolor='black', linewidths=1, alpha=0.75)

cbar = plt.colorbar()
cbar.set_label('Success')



plt.title('Scatter Plot')
plt.tight_layout()
plt.show()


# In[37]:


# Scatter Plot
plt.style.use('seaborn')

sizes = [random.randint(200,1000) for n in range(15)]

plt.scatter(x,y, s=sizes, c=colors,cmap='Greens', edgecolor='black', linewidths=1, alpha=0.75)


cbar = plt.colorbar()
cbar.set_label('Success')

plt.title('Scatter Plot')
plt.tight_layout()
plt.show()


# In[39]:


# Loading data  
plt.style.use('seaborn')

data = pd.read_csv('/home/rohyth/Python/Pandas/Matplotlib/ScatterPlot.csv')
views = data['view_count']
likes = data['likes']
ratio = data['ratio']

plt.scatter(views,likes, edgecolor='black', linewidths=1, alpha=0.75)

plt.title('Scatter Plot')
plt.tight_layout()
plt.show()


# In[44]:


# Using log scale
plt.style.use('seaborn')

data = pd.read_csv('/home/rohyth/Python/Pandas/Matplotlib/ScatterPlot.csv')
views = data['view_count']
likes = data['likes']
ratio = data['ratio']

plt.scatter(views,likes,c=ratio, cmap='summer'
            ,edgecolor='black', linewidths=1, alpha=0.75)

cbar = plt.colorbar()
cbar.set_label('like/dislike ratio')

plt.xscale('log')
plt.yscale('log')

plt.title('Scatter Plot')
plt.tight_layout()
plt.show()

