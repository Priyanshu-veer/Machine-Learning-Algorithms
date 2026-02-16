# DBSCAN Clustering on make_moons Dataset
## 📌Overview

This project demonstrates clustering using DBSCAN (Density-Based Spatial Clustering of Applications with Noise) on a non-linearly separable dataset generated using make_moons from sklearn.datasets.

Unlike centroid-based methods such as K-Means, DBSCAN is able to correctly cluster arbitrarily shaped data such as interleaving half-moons.

## 📊 Dataset

We use the make_moons synthetic dataset:

    from sklearn.datasets import make_moons
    
    X, y = make_moons(
        n_samples=1000,
        noise=0.05,
        random_state=42
    )

## Dataset Characteristics:
- 1000 samples
- 2 features
- Non-linear half-moon shapes
- Small noise added

This dataset is ideal for testing density-based clustering algorithms.

### 🟢 What is DBSCAN?

**DBSCAN stands for:**

> **Density-Based Spatial Clustering of Applications with Noise**

It is a density-based clustering algorithm that groups points based on how closely packed they are.

**Key Advantages:**
- Detects arbitrarily shaped clusters
- Does not require specifying number of clusters
- Identifies noise (outliers)
-  Works well on non-linear data

**⚙️ How DBSCAN Works**

DBSCAN uses two important parameters:
1. eps (Epsilon)
- Maximum distance between two points to be considered neighbors.
2.  min_samples
- Minimum number of neighboring points required to form a dense region.

## Three Categories in DBSCAN
- **Core Point**: Has at least min_samples neighbors within eps
- **Border Point**: Within eps of a core point
- **Noise Point**: Not dense enough to belong to any cluster

## 🧠 Implementation

    from sklearn.cluster import DBSCAN
    
    dbscan = DBSCAN(eps=0.3, min_samples=5)
    labels = dbscan.fit_predict(X)

## Visualization

    import seaborn as sns
    import matplotlib.pyplot as plt
    
    sns.scatterplot(x=X[:,0], y=X[:,1], hue=labels, palette="viridis")
    plt.title("DBSCAN on make_moons Dataset")
    plt.show()

# Comparision K-Means & DBSCAN

## K-Means Clustering
**How It Works:**

K-Means:
1. Chooses k cluster centroids
2. Assigns points to the nearest centroid (Euclidean distance)
3. Updates centroids iteratively
4. Repeats until convergence

**Implementation**

    from sklearn.cluster import KMeans
    
    kmeans = KMeans(n_clusters=2)
    labels = kmeans.fit_predict(X)

**⚠️ Limitation on make_moons**

K-Means assumes:
- Spherical clusters
- Equal variance
- Linear separability

Because `make_moon` forms curved, non-convex clusters, K-Means incorrectly splits the dataset instead of capturing the true moon shapes.

## DBSCAN Clustering
**📖 Introduction to DBSCAN**

DBSCAN stands for:

>**Density-Based Spatial Clustering of Applications with Noise**

It is a density-based clustering algorithm that:
- Groups together points that are closely packed
- Marks points in low-density regions as outliers
- Does NOT require specifying the number of clusters in advance

**🔎 How DBSCAN Works**

DBSCAN uses two main parameters:
- eps: Maximum distance between two samples to be considered neighbors
- min_samples: Minimum number of points required to form a dense region

It classifies points into:
- **Core Points** – Points with at least min_samples neighbors within eps
- **Border Points** – Points within eps of a core point
- **Noise Points** – Points that are neither core nor border

**Implementation**

    from sklearn.cluster import DBSCAN
    
    db = DBSCAN(eps=0.3, min_samples=5)
    labels = db.fit_predict(X)

**🚀 Why DBSCAN Performs Better Here**

DBSCAN:

1. Detects arbitrarily shaped clusters

2. Works well with non-linear structures

3. Automatically detects noise

4. Does not require specifying number of clusters

On the `make_moons` dataset, DBSCAN successfully separates the two moon shapes because it groups points based on density rather than distance to centroids.

## 📈 Results Comparison

| Algorithm  | Assumption	       | Works on Non-Convex Shapes?  | Needs Number of Clusters?
| ---------  | ------------------  | ---------------------------  | --------------------------
| K-Means	 | Spherical clusters  |  No	                      |  Yes
| DBSCAN	 | Density-based	   |  Yes	                      |  No


## 🛠 Technologies Used
- Python
- scikit-learn
- matplotlib
- seaborn

## 🎯 Key Takeaways
- K-Means is simple and efficient but struggles with non-linear data.
- DBSCAN is powerful for discovering arbitrarily shaped clusters.
- Density-based methods are often better for real-world spatial data.

#### 📌 When to Use What?
**Use K-Means when:**
- Clusters are spherical
- Data is linearly separable
- You know the number of clusters

**Use DBSCAN when:**
- Clusters have irregular shapes
- You expect noise/outliers
- You don't know the number of clusters beforehand

## 📚 References
- Scikit-learn documentation
- Density-based clustering research papers