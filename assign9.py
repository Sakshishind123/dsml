import numpy as np

# Given points
points = np.array([
    [0.1, 0.6],  # P1
    [0.15, 0.71],  # P2
    [0.08, 0.9],  # P3
    [0.16, 0.85],  # P4
    [0.2, 0.3],  # P5
    [0.25, 0.5],  # P6
    [0.24, 0.1],  # P7
    [0.3, 0.2]  # P8
])

# Initial centroids
m1 = np.array([0.1, 0.6])  # Cluster 1 (C1)
m2 = np.array([0.3, 0.2])  # Cluster 2 (C2)
# Function to calculate Euclidean distance
def euclidean_distance(p, m):
    return np.sqrt(np.sum((p - m) ** 2))

# Function to assign points to clusters
def assign_clusters(points, m1, m2):
    cluster1, cluster2 = [], []
    for point in points:
        dist_to_m1 = euclidean_distance(point, m1)
        dist_to_m2 = euclidean_distance(point, m2)

        # Assign to the nearest centroid
        if dist_to_m1 < dist_to_m2:
            cluster1.append(point)
        else:
            cluster2.append(point)

    return np.array(cluster1), np.array(cluster2)

# Step 1: Assign points to initial clusters
cluster1, cluster2 = assign_clusters(points, m1, m2)
# Step 2: Compute new centroids (mean of the points in each cluster)
new_m1 = np.mean(cluster1, axis=0)
new_m2 = np.mean(cluster2, axis=0)


# Results
print(f"Initial Centroids: m1={m1}, m2={m2}")
print(f"Cluster 1 (C1): {cluster1}")
print(f"Cluster 2 (C2): {cluster2}")
print(f"Updated Centroids: m1={new_m1}, m2={new_m2}")

# Answer to questions
# 1] Which cluster does P6 belong to?
dist_to_m1_p6 = euclidean_distance(np.array([0.25, 0.5]), m1)
dist_to_m2_p6 = euclidean_distance(np.array([0.25, 0.5]), m2)

cluster_p6 = "C1" if dist_to_m1_p6 < dist_to_m2_p6 else "C2"
print(f"P6 belongs to: {cluster_p6}")

# 2] Population of the cluster around m2 (Cluster 2)
population_m2 = len(cluster2)
print(f"Population of Cluster around m2: {population_m2}")

# 3] Updated value of m1 and m2
print(f"Updated m1: {new_m1}, Updated m2: {new_m2}")

