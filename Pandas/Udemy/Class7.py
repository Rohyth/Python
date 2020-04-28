import pandas as pd
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)

emp = pd.read_table('sample.tsv')
#loc function
emp.loc[0,:]
emp.loc[0:2,:]
emp.loc[0:2,2]
emp.loc[0:2,['Name','Salary']]
emp.loc[:,['Name','Salary']]
emp.loc[0:2,['Name','Salary']]

emp.loc[0:2,'Name':'Start date']

# rows with conditions
emp.loc[emp.Position == 'Software Engineer',:]
#dropna
emp
em = pd.read_table('sample 1.tsv')
em
em.shape
em.dropna(how='any').shape
# above statement was to delete all rows with columns having blank
em = pd.read_table('sample 1.tsv')
em.dropna(subset=['Salary'],how='any').shape
em
em.dropna(subset=['Salary'],how='any').shape
'this was important'
