#!/usr/bin/env python
# coding: utf-8

# In[58]:


import matplotlib.pyplot as plt
import numpy as np

#plt.style.available
plt.style.use('fivethirtyeight')


# In[37]:


# data sources ---------------------------------------
dev_x = []
dev_y = []

ages_x = [25,26,27,28,29,30,31,32,33,34,35]
dev_y = [m for m in range(40000,50000,1000)]
dev_y.append(50000)

py_y = [m for m in range(60500,71500,1000)]
py_y[4]=67000


# In[59]:


#ploting line graphs -----------------------------------
plt.plot(ages_x,dev_y)

plt.xlabel('Employee Age')
plt.ylabel('Salary') 
plt.title('Median Salary')
plt.show()


# In[39]:


#ploting multiple lines  in graphs -----------------------------------
plt.plot(ages_x,dev_y)
plt.plot(ages_x,py_y)

plt.xlabel('Employee Age')
plt.ylabel('Salary') 
plt.title('Median Salary')
plt.show()


# In[41]:


#Adding legend 1st way in graphs -----------------------------------
plt.plot(ages_x,dev_y)

plt.plot(ages_x,py_y)

plt.xlabel('Employee Age')
plt.ylabel('Salary') 
plt.title('Median Salary')

plt.legend(['All Developers','Python'])
plt.show()


# In[43]:


#Adding legend 2nd way in graphs -----------------------------------
plt.plot(ages_x,dev_y,label='All Developers')

plt.plot(ages_x,py_y,label='Python')

plt.xlabel('Employee Age')
plt.ylabel('Salary') 
plt.title('Median Salary')

plt.legend()
plt.show()


# In[44]:


#formating in graphs with color and line style
plt.plot(ages_x,dev_y,'k--',label='All Developers')

plt.plot(ages_x,py_y,'b:',label='Python')

plt.xlabel('Employee Age')
plt.ylabel('Salary') 
plt.title('Median Salary')

plt.legend()
plt.show()


# In[47]:


#formating in graphs with color and line style
plt.plot(ages_x,dev_y,color='k',linestyle='--',label='All Developers')

plt.plot(ages_x,py_y,color='b',label='Python')

plt.xlabel('Employee Age')
plt.ylabel('Salary') 
plt.title('Median Salary')

plt.legend()
plt.show()


# In[48]:


#formating in graphs with Markers
plt.plot(ages_x,dev_y,color='k',linestyle='--',marker='o',label='All Developers')

plt.plot(ages_x,py_y,color='b',marker='.',label='Python')

plt.xlabel('Employee Age')
plt.ylabel('Salary') 
plt.title('Median Salary')

plt.legend()
plt.show()


# In[61]:


#formating in graphs with linewidth
plt.style.use('dark_background')

plt.plot(ages_x,dev_y,color='k',linestyle='--',marker='o',label='All Developers')

plt.plot(ages_x,py_y,color='b',marker='.',label='Python',linewidth=3)

js_y = [x for x in range(37000,48000,1000)]

plt.plot(ages_x,js_y,label='Javascript',linewidth=3)

plt.xlabel('Employee Age')
plt.ylabel('Salary') 
plt.title('Median Salary')

plt.legend()

#use tight_layout method for padding issue
#plt.tight_layout()

plt.show()


# In[64]:


#formating in graphs with linewidth
plt.plot(ages_x,dev_y,color='k',linestyle='--',marker='o',label='All Developers')

plt.plot(ages_x,py_y,color='b',marker='.',label='Python',linewidth=3)

js_y = [x for x in range(37000,48000,1000)]

plt.plot(ages_x,js_y,label='Javascript',linewidth=3)

plt.xlabel('Employee Age')
plt.ylabel('Salary') 
plt.title('Median Salary')

plt.legend()

#use tight_layout method for padding issue
#plt.grid(True)
plt.tight_layout()
plt.show()


# In[65]:


#formating in graphs with linewidth
plt.xkcd()
plt.plot(ages_x,dev_y,color='k',linestyle='--',marker='o',label='All Developers')

plt.plot(ages_x,py_y,color='b',marker='.',label='Python',linewidth=3)

js_y = [x for x in range(37000,48000,1000)]

plt.plot(ages_x,js_y,label='Javascript',linewidth=3)

plt.xlabel('Employee Age')
plt.ylabel('Salary') 
plt.title('Median Salary')

plt.legend()

plt.tight_layout()
plt.show()


# In[74]:


#Saving plots
plt.style.use('seaborn-dark')
plt.xkcd() #hand drawn plots
plt.plot(ages_x,dev_y,color='k',linestyle='--',marker='o',label='All Developers')

plt.plot(ages_x,py_y,color='b',marker='.',label='Python',linewidth=3)

js_y = [x for x in range(37000,48000,1000)]

plt.plot(ages_x,js_y,label='Javascript',linewidth=3)

plt.xlabel('Employee Age')
plt.ylabel('Salary') 
plt.title('Median Salary')

plt.legend()
plt.tight_layout()
#saving plots

plt.savefig('plot1.png')
plt.show()


# In[75]:


ls


# In[ ]:




