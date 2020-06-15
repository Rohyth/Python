#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt


# In[10]:


# data set ------------------------------
nData = pd.read_csv("https://raw.githubusercontent.com/CoreyMSchafer/code_snippets/master/Python/Matplotlib/05-Fill_Betweens/data.csv")
Age = nData['Age']
dev_salary = nData['All_Devs']
py_dev = nData['Python']
js_dev = nData['JavaScript']


# In[17]:



plt.plot(Age,dev_salary, color='#444444', linestyle="--", label="All Devs")
plt.plot(Age,py_dev,label='Python')

# use below methods to fill graph are btw line plots
plt.fill_between(Age,py_dev, alpha=0.25)

plt.legend()
plt.title( "Median Salary with age ")
plt.xlabel("Ages")
plt.ylabel("Salaries")
plt.tight_layout()
plt.show()


# In[18]:


plt.plot(Age,dev_salary, color='#444444', linestyle="--", label="All Devs")
plt.plot(Age,py_dev,label='Python')

median_salary = 57287
# Adding arguments to the method using any median salary

plt.fill_between(Age,py_dev, median_salary,
                 where=(py_dev > median_salary), interpolate=True,
                 alpha=0.25)

plt.legend()
plt.title( "Median Salary with age ")
plt.xlabel("Ages")
plt.ylabel("Salaries")
plt.tight_layout()
plt.show()


# In[20]:


plt.plot(Age,dev_salary, color='#444444', linestyle="--", label="All Devs")
plt.plot(Age,py_dev,label='Python')

median_salary = 57287
# Adding arguments to the method using any median salary

plt.fill_between(Age,py_dev, median_salary,
                 where=(py_dev > median_salary), interpolate=True,
                 alpha=0.25)

plt.fill_between(Age,py_dev, median_salary,
                 where=(py_dev <= median_salary), interpolate=True,
                 color='red',alpha=0.25)


plt.legend()
plt.title( "Median Salary with age ")
plt.xlabel("Ages")
plt.ylabel("Salaries")
plt.tight_layout()
plt.show()


# In[22]:


plt.plot(Age,dev_salary, color='#444444', linestyle="--", label="All Devs")
plt.plot(Age,py_dev,label='Python')

median_salary = 57287
# Adding arguments to the method using any median salary

plt.fill_between(Age,py_dev, dev_salary,
                 where=(py_dev > dev_salary), interpolate=True,
                 alpha=0.25, label='Above Avg')

plt.fill_between(Age,py_dev, dev_salary,
                 where=(py_dev <= dev_salary), interpolate=True,
                 color='red',alpha=0.25, label='Below Avg')


plt.legend()
plt.title( "Median Salary with age ")
plt.xlabel("Ages")
plt.ylabel("Salaries")
plt.tight_layout()
plt.show()


# In[ ]:




