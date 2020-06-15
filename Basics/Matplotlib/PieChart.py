#!/usr/bin/env python
# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt


# In[12]:


# basic example-------------------
plt.style.use('fivethirtyeight')

slices = [20,70,10]
labels = ['Java','Python','Html']
colors = ['#65fafa','#2561ca','#cc1520']

# use wedgeproperties to add lines for color division
plt.pie(slices, labels=labels, wedgeprops={'edgecolor':'black'}, colors=colors)


plt.title('Pie chart Example')
plt.tight_layout()
plt.show()


# In[14]:


# Imported data example-------------------
plt.style.use('fivethirtyeight')

slices = [59219, 55466, 47544, 36443, 35917]
labels = ['JavaScript', 'HTML/CSS', 'SQL', 'Python', 'Java']

plt.pie(slices, labels=labels, wedgeprops={'edgecolor':'black'})

plt.title('Pie chart Example')
plt.tight_layout()
plt.show()


# In[18]:


# use explode method to emphasize any specific item

plt.style.use('fivethirtyeight')

slices = [59219, 55466, 47544, 36443, 35917]
labels = ['JavaScript', 'HTML/CSS', 'SQL', 'Python', 'Java']
explode = [0,0,0,0.1,0]

# use shadow method for a 3d look

plt.pie(slices, labels=labels, wedgeprops={'edgecolor':'black'},explode=explode, shadow=True)

plt.title('Pie chart Example')
plt.tight_layout()
plt.show()


# In[20]:


'---------------------------------------------------'
plt.style.use('fivethirtyeight')

slices = [59219, 55466, 47544, 36443, 35917]
labels = ['JavaScript', 'HTML/CSS', 'SQL', 'Python', 'Java']
explode = [0,0,0,0.1,0]

# use startangle method to rotate the chart with values
# use autopct to add percentages in slices

plt.pie(slices, labels=labels, wedgeprops={'edgecolor':'black'},
        explode=explode, shadow=True, startangle=90,
       autopct='%1.1f%%')

plt.title('Pie chart Example')
plt.tight_layout()
plt.show()


# In[ ]:




