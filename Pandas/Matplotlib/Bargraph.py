#!/usr/bin/env python
# coding: utf-8

# In[22]:


from matplotlib import pyplot as plt
import numpy as np
import random


# In[25]:


# Base Data --------------------------
plt.style.use("fivethirtyeight")

ages_x = [i for i in range(25,35)]
dev_y = random.sample(range(10000,90000),10)
dev_y.sort()

py_dev = random.sample(range(20000,80000),10)
py_dev.sort()

js_dev = random.sample(range(15000,70000),10)
js_dev.sort()


# In[26]:


# Simple Bar graph
plt.bar(ages_x,dev_y, color="#444444", label="All Devs")
plt.legend()
plt.title('Salary distribution')
plt.xlabel("Ages")
plt.ylabel("Salaries")

plt.tight_layout()
plt.show()


# In[28]:


# Adding single or multiple lines in Bar graph
plt.bar(ages_x,dev_y, color="#444444", label="All Devs")



plt.plot(ages_x,py_dev,color="#33ff3c",label="Python Developers")

plt.plot(ages_x,js_dev,color="#9e3535",label="Js Developers")

plt.legend()
plt.title('Salary distribution')
plt.xlabel("Ages")
plt.ylabel("Salaries")

plt.tight_layout()
plt.show()


# In[29]:


# Adding single or multiple bars in Bar graph
plt.bar(ages_x,dev_y, color="#444444", label="All Devs")

plt.bar(ages_x,py_dev,color="#33ff3c",label="Python Developers")

plt.bar(ages_x,js_dev,color="#9e3535",label="Js Developers")

plt.legend()
plt.title('Salary distribution')
plt.xlabel("Ages")
plt.ylabel("Salaries")

plt.tight_layout()
plt.show()


# In[35]:


# Adding single or multiple bars with spacing in Bar graph
# use numpy artay to specify indexes of multiple bars

x_index = np.arange(len(ages_x))
width = 0.25

plt.bar(x_index - width,dev_y, width=width, color="#444444", label="All Devs")

plt.bar(x_index,py_dev, width=width, color="#33ff3c",label="Python Developers")

plt.bar(x_index + width, js_dev, width=width, color="#9e3535",label="Js Developers")

plt.legend()
plt.xticks(ticks=x_index,labels=ages_x)

plt.title('Salary distribution')
plt.xlabel("Ages")
plt.ylabel("Salaries")

plt.tight_layout()
plt.show()


# In[ ]:




