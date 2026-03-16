import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LogisticRegression 
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor

x=([[1],[2],[3],[4]])
y=([3,5,3,2])


model=LogisticRegression()
model.fit(x,y)

plt.scatter(x,y,color="red",label="pnt")
x_range=np.linspace(0,7,100).reshape(-1,1)
y_prob=model.predict_proba(x_range)[:,1]
plt.plot(x_range,y_prob,color='blue',label='line')

plt.show()