import pandas as pd
empl = pd.read_table('sample.tsv')
empl.head()
# Sorting Data----
empl.sort_values(by='Age',ascending=False)
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)
empl.sort_values(by='Age',ascending=False)
empl.sort_values(by='Age',ascending=False).head()
#sorting by name
empl.sort_values(by='Name')
empl.sort_values(by='Name').head()
# filtering Data
empl[empl.Age <40]
empl[(empl.Age <40) & (empl.Name == 'Airi')]
empl[(empl.Age < 40) & (empl.Name == 'Airi Satou')]
empl.head()
empl.mean()
# string manipulation
empl.Name.str.upper()
empl.Name.str.lower().head()
empl.Position.str.contains('Software')
empl[empl.Position.str.contains('Software')]
empl.Position.str.contains('London')
empl[(empl.Position.str.contains('Software')) & (empl.Position.str.contains('London'))]
empl[empl.Position.str.contains('Software','London')]
empl[empl.Position.str.contains('Software' & 'London')]
empl.Position.str.replace('Software','Developer')
empl.Position.str.replace('Software','Developer').head()
empl
empl.head()
empl = empl.Position.str.replace('Software','Developer')
empl
empl.head()
# aggregations
empl.head()
emp = pd.read_table('sample.tsv')
emp.head()
emp.Age.max()
emp.Age.min()
emp.groupby('Position').Age.min()
emp.groupby('Position').Age.max()
emp.groupby('Position').Salary.max()
emp.groupby('Position').Age.agg(['count','min','max'])
empl.Name
empl['Name']
emp
emp.Name
emp.Name.str.len()
emp.Name.str.len().head()
emp.Name.str.len().head().max()
emp.Name.str.len().head().min()
emp.Name.str.len().max()