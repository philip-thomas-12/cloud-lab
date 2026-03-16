import pandas as pd
from sklearn.ensemble import RandomForestRegressor
import matplotlib.pyplot as plt
import numpy as np

x = np.array([1, 2, 3, 4]).reshape(-1, 1)
y = np.array([4, 7, 4, 5])



model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(x, y)

prediction = model.predict([[6]])
print("Prediction for 6:", prediction[0])


plt.scatter(x, y, color='blue', label='Data points')

#x_sorted = x.sort_values(by="x") if it was taken from csv file
xsort=np.sort(x, axis=0)

plt.plot(xsort, model.predict(xsort),color='green', label='Random Forest Prediction')

plt.xlabel("x")
plt.ylabel("y")
plt.title("Random Forest Regression")
plt.legend()
plt.show()

