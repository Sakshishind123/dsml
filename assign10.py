import numpy as np

# Given points
points = np.array([
    [2, 10],  # P1
    [2, 5],   # P2
    [8, 4],   # P3
    [5, 8],   # P4
    [7, 5],   # P5
    [6, 4],   # P6
    [1, 2],   # P7
    [4, 9]    # P8
])

# Initial centroids
m1 = np.array([2, 10])  # Cluster 1 (C1)
m2 = np.array([5, 8])   # Cluster 2 (C2)
m3 = np.array([1, 2])   # Cluster 3 (C3)


# Function to calculate Euclidean distance
def euclidean_distance(p, m):
    return np.sqrt(np.sum((p - m) ** 2))

# Function to assign points to clusters
def assign_clusters(points, m1, m2, m3):
    cluster1, cluster2, cluster3 = [], [], []
    for point in points:
        dist_to_m1 = euclidean_distance(point, m1)
        dist_to_m2 = euclidean_distance(point, m2)
        dist_to_m3 = euclidean_distance(point, m3)

        # Assign to the nearest centroid
        if dist_to_m1 <= dist_to_m2 and dist_to_m1 <= dist_to_m3:
            cluster1.append(point)
        elif dist_to_m2 <= dist_to_m1 and dist_to_m2 <= dist_to_m3:
            cluster2.append(point)
        else:
            cluster3.append(point)

    return np.array(cluster1), np.array(cluster2), np.array(cluster3)

# Step 1: Assign points to initial clusters
cluster1, cluster2, cluster3 = assign_clusters(points, m1, m2, m3)

# Step 2: Compute new centroids (mean of the points in each cluster)
new_m1 = np.mean(cluster1, axis=0)
new_m2 = np.mean(cluster2, axis=0)
new_m3 = np.mean(cluster3, axis=0)

# Results
print(f"Initial Centroids: m1={m1}, m2={m2}, m3={m3}")
print(f"Cluster 1 (C1): {cluster1}")
print(f"Cluster 2 (C2): {cluster2}")
print(f"Cluster 3 (C3): {cluster3}")
print(f"Updated Centroids: m1={new_m1}, m2={new_m2}, m3={new_m3}")


# Answer to questions
# 1] Which cluster does P6 belong to?
dist_to_m1_p6 = euclidean_distance(np.array([6, 4]), m1)
dist_to_m2_p6 = euclidean_distance(np.array([6, 4]), m2)
dist_to_m3_p6 = euclidean_distance(np.array([6, 4]), m3)

cluster_p6 = "C1" if dist_to_m1_p6 < dist_to_m2_p6 and dist_to_m1_p6 < dist_to_m3_p6 else "C2" if dist_to_m2_p6 < dist_to_m3_p6 else "C3"
print(f"P6 belongs to: {cluster_p6}")

# 2] Population of the cluster around m3 (Cluster 3)
population_m3 = len(cluster3)
print(f"Population of Cluster around m3: {population_m3}")

# 3] Updated value of m1, m2, m3
print(f"Updated m1: {new_m1}, Updated m2: {new_m2}, Updated m3: {new_m3}")

