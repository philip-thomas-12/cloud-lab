import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import pandas as pd

data=pd.read_csv("data.csv")

X = np.column_stack((data[["x"]],data["y"]))

model = KMeans(n_clusters=2, n_init='auto', random_state=42)
model.fit(X)

labels = model.predict(X)
centers = model.cluster_centers_

plt.scatter(X[:, 0], X[:, 1], c=labels, cmap='viridis')
plt.scatter(centers[:, 0], centers[:, 1], c='red', label='Centroids')

plt.xlabel("x")
plt.ylabel("y")
plt.title("K-Means Cluster")
plt.legend()
plt.show()