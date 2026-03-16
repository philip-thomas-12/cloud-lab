import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression


x_ = input("Enter x values separate")
y_ = input("Enter y values separate")


# FIX: Added .reshape(-1, 1) to make x a 2D array
x = np.array(list(map(float, x_.split()))).reshape(-1, 1)


# FIX: Changed float to int for classification labels
y = np.array(list(map(int, y_.split())))


model = LogisticRegression()
model.fit(x, y)
prediction = model.predict([[6]])


print("Predicted class for 6:", prediction[0])
plt.scatter(x, y, color='blue', label='Data points')


x_range = np.linspace(0, 7, 100).reshape(-1, 1)
y_prob = model.predict_proba(x_range)[:, 1]


plt.plot(x_range, y_prob, color='red', label='Logistic curve')
plt.xlabel("x")
plt.ylabel("Probability")
plt.title("Logistic Regression")
plt.legend()
plt.show()
