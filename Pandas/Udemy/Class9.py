import pandas as pd

data = pd.read_csv("data.csv")
data
data.head()
data.shape
data.shift(1)
data = pd.read_csv("data.csv", index_col='Date')
data.head()
data.shift(1).head()
data['prev_closing'] = data['Close'].shift(1)
data.head()
data['new_closing_price'] = data['Close']-data['prev_closing']
data.head
data
data.head()
# write to csv ----------------------
data.to_csv('Result.csv')
