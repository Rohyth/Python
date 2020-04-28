import  pandas as pd
empl = pd.read_table('sample.tsv')
empl.head()
empl.shape
url = pd.read_table("https://www.nrc.gov/reading-rm/doc-collections/event-status/reactor-status/2009/2009PowerStatus.txt")
url.head()
url = pd.read_table("https://www.nrc.gov/reading-rm/doc-collections/event-status/reactor-status/2009/2009PowerStatus.txt",sep="|")
url.head()
url
empl.head()
cols = ['Name','Salary']
empl[cols]
empl[cols][0:10]
empl[cols][5:10]
empl = pd.read_table('sample.tsv', nrows=4)
empl
# Data types
empl = pd.read_table('sample.tsv')
empl.dtypes
import numpy as np
empl.select_dtypes(include = [np.number]).dtypes
# this WAS used for filtering data as per datatypes
empl.describe()
empl.shape
type(empl)
#concat data in columns
empl.head()
empl['Name_Salary'] = empl['Name']+empl['Salary']
empl.head()
#drop a column
empl.drop('Office',axis=1,inplace=True)
empl
empl.head()
# change Columns Name
empl = pd.read_table('sample.tsv')
cols = ['Name','Postion','ofc','Age','stDate','Paisa']
empl.columns = cols
empl.head()

# Column Indexing
empl.columns[1]
empl.columns[2]


