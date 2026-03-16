import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import numpy as np


x = np.array([[1],[2],[3],[4]])
y = np.array([4, 7, 4, 5])


model = LinearRegression()
model.fit(x, y)
prediction = model.predict([[6]])

print("Slope:", model.coef_[0])
print("Intercept:", model.intercept_)
print("Prediction for 6:", prediction[0])



plt.scatter(x, y, color='blue', label='Data points') 




plt.plot(x, model.predict(x), color='red',
label='Regression line') 


plt.xlabel("x")
plt.ylabel("y")
plt.title("Linear Regression (scikit-learn)")
plt.legend()
plt.show()
