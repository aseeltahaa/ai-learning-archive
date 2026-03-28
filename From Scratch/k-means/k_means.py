import numpy as np
import matplotlib.pyplot as plt

class KMeansClustering:
    
    def __init__(self, k=3):
        self.k = k
        self.centroids = None
     
    @staticmethod    
    def euclidean_distance(data_point, centroids):
        return np.sqrt(np.sum((centroids - data_point) ** 2, axis=1))
    
    def fit(self, X, max_iterations=200):
        # Initialize centroids randomly within data range
        self.centroids = np.random.uniform(
            np.amin(X, axis=0), 
            np.amax(X, axis=0),
            size=(self.k, X.shape[1])
        )

        for _ in range(max_iterations):
            y = []  # cluster labels

            # Assign each point to the nearest centroid
            for data_point in X:
                distances = self.euclidean_distance(data_point, self.centroids)
                cluster_number = np.argmin(distances)
                y.append(cluster_number)

            y = np.array(y)

            # Group indices by cluster
            cluster_indices = []
            for i in range(self.k):
                cluster_indices.append(np.argwhere(y == i))

            # Compute new centroids
            cluster_centers = []
            for i, indices in enumerate(cluster_indices):
                if len(indices) == 0:
                    cluster_centers.append(self.centroids[i])  # keep old centroid
                else:
                    indices = indices.flatten()
                    cluster_centers.append(np.mean(X[indices], axis=0))

            cluster_centers = np.array(cluster_centers)

            # Check for convergence
            if np.max(np.abs(self.centroids - cluster_centers)) < 1e-4:
                break

            self.centroids = cluster_centers

        return y

    def predict(self, X):
        labels = []
        for data_point in X:
            distances = self.euclidean_distance(data_point, self.centroids)
            labels.append(np.argmin(distances))
        return np.array(labels)


# testing
if __name__ == "__main__":
    np.random.seed(42)
    
    random_points = np.random.randint(0, 100, (100, 2))

    kmeans = KMeansClustering(k=3)
    labels = kmeans.fit(random_points)

    # Plot points
    plt.scatter(random_points[:, 0], random_points[:, 1], c=labels)

    # Plot centroids
    plt.scatter(
        kmeans.centroids[:, 0], 
        kmeans.centroids[:, 1], 
        c=range(len(kmeans.centroids)),
        marker="*", 
        s=200
    )

    plt.title("K-Means Clustering")
    plt.show()