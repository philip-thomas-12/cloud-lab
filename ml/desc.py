import pandas as pd
from sklearn.tree import DecisionTreeRegressor
import matplotlib.pyplot as plt
import numpy as np

x_=input("enter x values")
y_=input("enter y values")

x=np.array(list(map(float,x_.split()))).reshape(-1, 1)
y=np.array(list(map(float,y_.split())))     


model = DecisionTreeRegressor(random_state=42)
model.fit(x, y)

prediction = model.predict([[6]])
print("Prediction for 6:", prediction[0])


plt.scatter(x, y, color='blue', label='Data points')



plt.plot(x, model.predict(x), color='red', label='Regression line')

plt.xlabel("x")
plt.ylabel("y")
plt.title("Decision Tree Regression")
plt.legend()
plt.show()
