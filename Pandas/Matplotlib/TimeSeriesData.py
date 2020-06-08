#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pandas as pd
import random
import matplotlib.pyplot as plt
from matplotlib import dates as mpl_dates
from datetime import datetime, timedelta


# In[22]:



plt.style.use('seaborn')

dates = [datetime(2019, 5, x) for x in range(24,30)]
y = [random.randint(1,7) for n in range(6)]
y.sort()

plt.plot_date(dates, y, linestyle='solid')

plt.tight_layout()
plt.show()


# In[24]:


# Using Autoformat 


plt.style.use('seaborn')


plt.plot_date(dates, y, linestyle='solid')
plt.gcf().autofmt_xdate()

plt.tight_layout()
plt.show()


# In[26]:


# Date formating using mpl_dates lib

plt.style.use('seaborn')

plt.plot_date(dates, y, linestyle='solid')
plt.gcf().autofmt_xdate()

date_format = mpl_dates.DateFormatter('%b , %d, %Y')
plt.gca().xaxis.set_major_formatter(date_format)

plt.tight_layout()
plt.show()


# In[52]:


# New Example ---------------------------------

plt.style.use('seaborn')

data = pd.read_csv('https://raw.githubusercontent.com/CoreyMSchafer/code_snippets/master/Python/Matplotlib/08-TimeSeries/data.csv')


price_date = data['Date']
price_close = data['Close']

plt.plot_date(price_date, price_close, linestyle='solid')
plt.gcf().autofmt_xdate()


plt.title('Bitcoin prices')
plt.xlabel('Date')
plt.ylabel('Closing Price')
plt.tight_layout()
plt.show()


# In[51]:


#formatting as per date using pandas

plt.style.use('seaborn')

data = pd.read_csv('https://raw.githubusercontent.com/CoreyMSchafer/code_snippets/master/Python/Matplotlib/08-TimeSeries/data.csv')

data['Date'] = pd.to_datetime(data['Date'])
data.sort_values('Date', inplace=True)

price_date = data['Date']
price_close = data['Close']

plt.plot_date(price_date, price_close, linestyle='solid')
plt.gcf().autofmt_xdate()


plt.title('Bitcoin prices')
plt.xlabel('Date')
plt.ylabel('Closing Price')
plt.tight_layout()
plt.show()


# In[ ]:




