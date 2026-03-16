import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression

x=np.array([1,2,3,4,5]).reshape(-1,1)
y=np.array([1,4,3,7,8])

model=LinearRegression()
model.fit(x,y)

plt.scatter(x,y,)
plt.plot(x,model.predict(x))

plt.title("linear regression")

plt.show()