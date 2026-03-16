import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

x=([[1],[2],[3],[4],[5]])
y=([1,2,3,45,5])

model=LinearRegression()
model.fit(x,y)

plt.scatter(x, y, color='blue', label='Data points')
plt.plot(x, model.predict(x),color='red',label='Regress')

plt.xlabel("x")
plt.ylabel("y")
plt.title("Decision Tree Regression")
plt.legend()
plt.show()