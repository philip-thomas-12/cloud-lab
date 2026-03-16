import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


x = np.array([1, 2, 3, 4])
y = np.array([4, 7, 4, 5])



m = b = 0.0
lr = 0.01
n = len(x)

for _ in range(1000):
    y_pred = m * x + b
    error = y_pred - y
    m -= lr * (2/n) * np.sum(error * x)
    b -= lr * (2/n) * np.sum(error)

print("Slope:", m)
print("Intercept:", b)
print("Prediction for 6:", m * 6 + b)

plt.scatter(x, y, color='blue', label='Data points') 
plt.plot(x, m * x + b, color='red', label='Regression line') 

plt.xlabel("x")
plt.ylabel("y")
plt.title("Linear Regr using Gradient Descent")
plt.legend()
plt.show()

