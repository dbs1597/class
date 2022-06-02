import matplotlib.pyplot as plt
import numpy as np
from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs


X, y_true = make_blobs(n_samples=300, centers=4, cluster_std=0.60, random_state=0)

# plt.scatter(X[:,0],X[:,1])

n_clusters = range(1, 10)
kmeans = [KMeans(n_clusters=i) for i in n_clusters]

score = [kmeans[i].fit(X).inertia_ for i in range(len(kmeans))]

plt.plot(n_clusters, score)
plt.xlabel('Number of Clusters')
plt.ylabel('Score')
plt.title('Elbow Curve')
plt.show()