import numpy as np

Z = np.zeros(10)
Z

Z = np.zeros((10,10))
Z

O = np.ones((10,10))
O

R = np.random.random((10,10))
R

R = np.random.randn(10,10)
R

R.mean()
R.var()

'---------------------- load data'

X = []
for line in open("data_2d.csv"):
    row = line.split(',')
    sample = map(float,row)
    X.append(row)
    
X

X = np.array(X)
X.shape
