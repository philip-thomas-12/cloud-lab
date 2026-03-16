import numpy as np
import matplotlib.pyplot as plt

x = np.array([1, 2, 3, 4, 5])
y = np.array([8, 6, 3, 4, 5])

m=b=0.0
lr=.01
n=len(x)

for _ in range(1000):
    
    y_pr=m*x+b 
    err=y_pr-y
    m=m-lr*(2/n)*np.sum(err * x)
    b=b-lr*(2/n)*np.sum(err)

plt.scatter(x,y,color='blue',label="dp")
plt.plot(x,m*x+b,color='red',label="plot")

plt.show()