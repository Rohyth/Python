import pandas as pd

emp = pd.read_table("https://raw.githubusercontent.com/jbrownlee/Datasets/master/shampoo.csv")
emp
emp = pd.read_table("https://raw.githubusercontent.com/jbrownlee/Datasets/master/shampoo.csv",sep=',')
emp
emp.head()
emp.plot()

df1 = pd.DataFrame({"Name":['Rohit','Sourabh','Bhanu'],"Work":['Engineer','Invoice Processing','linguistic'],"Age":[28,27,23]})
df1
df2 = pd.DataFrame({"Name":['Rohit','Sourabh','Bhanu'],"Work":['Engineer','Invoice Processing','linguistic'],"Salary":[45000,27000,5000]})
df2
df3 = pd.merge(df1,df2)
df3
df2 = pd.DataFrame({"Name":['Rohit','Sourabh','Ravi'],"Work":['Engineer','Invoice Processing','linguistic'],"Salary":[45000,27000,5000]})
df2
df3 = pd.merge(df1,df2)
df3
df3 = pd.merge(df1,df2, on="Name")
df3
df3 = pd.merge(df1,df2, on="Name", how="outer")
df3
df3 = pd.merge(df1,df2, on="Name", how="left")
df3
df3 = pd.merge(df1,df2, on="Name", how="right")
df3
# pivot Data----------------------------------------


data = pd.read_table("pv.tsv")
data
data.pivot_table(index='Name',columns='Position').head()
data.pivot_table(index='Name',columns='Start date').head()
data.pivot_table(index='Name',columns='Start date',aggfunc='sum').head()
data.pivot_table(index='Salary',aggfunc='sum')
data.pivot_table(index='Age',aggfunc='sum')
data.pivot_table(index='Age',aggfunc='max')
data.pivot_table(index='Age',aggfunc='count')