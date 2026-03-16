import numpy as np
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestRegressor

x_=input("enter x")
y_=input("enter y")

x=np.array(list(map(float,x_.split()))).reshape(-1,1)
y=np.array(list(map(int,y_.split())))


model=RandomForestRegressor(n_estimators=100,random_state=42)
model.fit(x,y)

plt.scatter(x,y,color='blue',label='dp')

#x_range=np.linspace(0,7,100).reshape(-1,1)
#y_prob=model.predict_proba(x_range)[:,1]
plt.plot(x,model.predict(x),color='blue',label='dp')

plt.show()