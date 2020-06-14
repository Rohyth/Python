#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt


# In[8]:



plt.style.use('seaborn')

data = pd.read_csv('/home/rohyth/Python/Pandas/Matplotlib/Subplot_data.csv')
ages = data['Age']
dev_S = data['All_Devs']
py_S = data['Python']
js_S = data['JavaScript']

plt.plot(ages, py_S, label='Python')
plt.plot(ages, js_S, label='JavaScript')

plt.plot(ages, dev_S , label='All Developers', color='#444444', linestyle='--')
plt.legend()

plt.title('Median Salaries of Developers')
plt.xlabel('Ages')
plt.ylabel('Salaries')

plt.tight_layout()
plt.show()


# In[9]:


plt.style.use('seaborn')

data = pd.read_csv('/home/rohyth/Python/Pandas/Matplotlib/Subplot_data.csv')
ages = data['Age']
dev_S = data['All_Devs']
py_S = data['Python']
js_S = data['JavaScript']

fig, ax = plt.subplots() 

ax.plot(ages, py_S, label='Python')
ax.plot(ages, js_S, label='JavaScript')

ax.plot(ages, dev_S , label='All Developers', color='#444444', linestyle='--')

ax.legend()

ax.set_title('Median Salaries of Developers')
ax.set_xlabel('Ages')
ax.set_ylabel('Salaries')

plt.tight_layout()
plt.show()


# In[18]:


plt.style.use('seaborn')

data = pd.read_csv('/home/rohyth/Python/Pandas/Matplotlib/Subplot_data.csv')
ages = data['Age']
dev_S = data['All_Devs']
py_S = data['Python']
js_S = data['JavaScript']

fig, (ax1,ax2) = plt.subplots(nrows=2,ncols=1) 

ax2.plot(ages, py_S, label='Python')
ax2.plot(ages, js_S, label='JavaScript')

ax1.plot(ages, dev_S , label='All Developers', color='#444444', linestyle='--')

ax1.legend()
ax1.set_title('Median Salaries of Developers')

ax1.set_ylabel('Salaries')

ax2.legend()
ax2.set_xlabel('Ages')
ax2.set_ylabel('Salaries')

plt.tight_layout()
plt.show()


# In[20]:


plt.style.use('seaborn')

data = pd.read_csv('/home/rohyth/Python/Pandas/Matplotlib/Subplot_data.csv')
ages = data['Age']
dev_S = data['All_Devs']
py_S = data['Python']
js_S = data['JavaScript']

# using share attribute to use common axis
fig, (ax1,ax2) = plt.subplots(nrows=2, ncols=1, sharex=True) 

ax2.plot(ages, py_S, label='Python')
ax2.plot(ages, js_S, label='JavaScript')

ax1.plot(ages, dev_S , label='All Developers', color='#444444', linestyle='--')

ax1.legend()
ax1.set_title('Median Salaries of Developers')

ax1.set_ylabel('Salaries')

ax2.legend()
ax2.set_xlabel('Ages')
ax2.set_ylabel('Salaries')

plt.tight_layout()
plt.show()


# In[21]:


# Using Multiple figures 

plt.style.use('seaborn')

data = pd.read_csv('/home/rohyth/Python/Pandas/Matplotlib/Subplot_data.csv')
ages = data['Age']
dev_S = data['All_Devs']
py_S = data['Python']
js_S = data['JavaScript']

# declaring multiple figures
fig1, ax1 = plt.subplots() 
fig2, ax2 = plt.subplots() 

ax2.plot(ages, py_S, label='Python')
ax2.plot(ages, js_S, label='JavaScript')

ax1.plot(ages, dev_S , label='All Developers', color='#444444', linestyle='--')

ax1.legend()
ax1.set_title('Median Salaries of Developers')

ax1.set_ylabel('Salaries')

ax2.legend()
ax2.set_xlabel('Ages')
ax2.set_ylabel('Salaries')

plt.tight_layout()
plt.show()


# In[ ]:




