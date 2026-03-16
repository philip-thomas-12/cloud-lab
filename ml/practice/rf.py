import numpy as np
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestRegressor

x=([[1],[2],[3],[4],[5]])
y=([1,2,3,4,5])

model=RandomForestRegressor(n_estimators=100,random_state=42)
model.fit(x,y)


plt.scatter(x, y, color='blue', label='Data points')
plt.plot(x, model.predict(x),color='red',label='Regress')

plt.xlabel("x")
plt.ylabel("y")
plt.title("rf")
plt.legend()
plt.show()