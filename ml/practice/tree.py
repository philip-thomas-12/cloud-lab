import numpy as np
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeRegressor

x=([[1],[2],[3],[4],[5]])
y=([1,5,36,4,7])

model=DecisionTreeRegressor(random_state=42)
model.fit(x,y)
prediction=model.predict([[6]])

plt.scatter(x, y, color='blue', label='Data points')
plt.plot(x, model.predict(x),color='red',label='Regress')

plt.xlabel("x")
plt.ylabel("y")
plt.title("Decision Tree Regression")
plt.legend()
plt.show()