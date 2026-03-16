import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression

x=([[1],[2],[3],[4],[5]])
y=([1,2,3,4,5])

model=LogisticRegression()
model.fit(x,y)

plt.scatter(x, y, color='blue', label='Data points')
x_range = np.linspace(0, 7, 100).reshape(-1, 1)
y_prob = model.predict_proba(x_range)[:, 1]
plt.plot(x_range, y_prob, color='red', label='Logistic curve')

plt.xlabel("x")
plt.ylabel("y")
plt.title("log")
plt.legend()
plt.show()