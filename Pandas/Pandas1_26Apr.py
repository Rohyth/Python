import pandas as pd
X = pd.read_csv("data_2d.csv",header=None)
X
type(X)
X.info
X.info()
X.head(5)
X.head(100)
X.head(50)

X[0]
X.ix[0]
X.iloc[0]
X[[0,2]]
X[ X[0] < 5]
X[ X[0] > 5]

'-------------------------------New File'

import pandas as pd
import matplotlib.pyplot as plt
A = pd.read_csv("data_1d.csv", header=None).values
x = A[:,0]
y = A[:,1]
plt.plot(x,y)
plt.scatter(x,y)
plt.show()
plt.scatter(x,y)
plt.show()
plt.hist(x)
plt.hist(y)
plt.show()
plt.draw()

import numpy as np

R = np.random.random(10000)
import numpy as np
R = np.random.random(10000)
plt.hist(R)
plt.hist(R, bits=20)
plt.hist(R, bims=20)
plt.hist(R, bins=20)
