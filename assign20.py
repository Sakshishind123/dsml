# import pandas as pd
# import numpy as np

# # Load the Iris dataset
# iris_data = pd.read_csv('C:/Users/saksh/OneDrive/Desktop/DSML PRACT. EXAM/IRIS.csv')

# # Extract only the numeric features for clustering
# features = iris_data[['sepal_length', 'sepal_width', 'petal_length', 'petal_width']].values

# # Define the number of clusters and iterations
# K = 3
# iterations = 10

# # Step 1: Randomly initialize cluster centroids
# np.random.seed(42)  # For reproducibility
# random_indices = np.random.choice(features.shape[0], K, replace=False)
# centroids = features[random_indices]

# # K-means clustering algorithm
# for i in range(iterations):
#     # Step 2: Assign each point to the nearest cluster centroid
#     distances = np.array([[np.linalg.norm(point - centroid) for centroid in centroids] for point in features])
#     labels = np.argmin(distances, axis=1)
    
#     # Step 3: Recalculate cluster centroids
#     new_centroids = np.array([features[labels == k].mean(axis=0) for k in range(K)])
   
# # Step 4: Print final cluster centroids
# print("Final cluster means (centroids):")
# for cluster_id, centroid in enumerate(centroids):
#     print(f"Cluster {cluster_id + 1}: {centroid}")














import numpy as np
import pandas as pd 


iris_data = pd.read_csv('C:/Users/saksh/OneDrive/Desktop/DSML PRACT. EXAM/IRIS.csv')

features=iris_data[['sepal_length','sepal_width','petal_length','petal_width']].values

iterations=10
K=3

np.random.seed(42)
rnadom_indices=np.random.choice(features.shape[0],K,replace=False)
centroids=features[rnadom_indices]

distances=np.array([[np.linalg.norm(point-centroid) for centroid in centroids] for point in features])
labels=np.argmin(distances,axis=1)

new=np.array(features[labels==k].min(axis=0)for k in range (K))

for centroid_id ,centroid in enumerate(centroids):
    print(f"Clusters {centroid_id +1}: {centroid} ")





