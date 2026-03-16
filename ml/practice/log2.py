import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression

x_=input("enter x")
y_=input("enter y")

x=np.array(list(map(float,x_.split()))).reshape(-1,1)
y=np.array(list(map(int,y_.split())))


model=LogisticRegression()
model.fit(x,y)

plt.scatter(x,y,color='blue',label='dp')

x_range=np.linspace(0,7,100).reshape(-1,1)
y_prob=model.predict_proba(x_range)[:,1]
plt.plot(x_range,y_prob,color='blue',label='dp')

plt.show()