# 📊 Agglomerative Hierarchical Clustering

## Introduction

This project demonstrates Agglomerative Hierarchical Clustering, a bottom-up clustering algorithm that groups data points based on similarity.

Unlike K-Means, hierarchical clustering does not require iterative centroid updates. Instead, it builds a tree-like structure called a dendrogram, which helps visualize how clusters are formed step by step.

### What is Agglomerative Clustering?

Agglomerative clustering is a bottom-up approach:

1. Initially, each data point is treated as its own cluster.
2. The two closest clusters are merged.
3. This process continues until:
    - A predefined number of clusters is reached, OR
    - All points are merged into a single cluster.

It creates a hierarchy of clusters represented as a tree (dendrogram).

### 🔬 Linkage Methods

The linkage method determines how the distance between clusters is calculated.

**Common methods:**
- Ward (used in this project) → Minimizes variance within clusters.
- Single → Minimum distance between cluster points.
- Complete → Maximum distance between cluster points.
- Average → Average distance between cluster points.

In this project, we use:

    linkage(X, method='ward')

# 📂 Project Workflow
**1. Generate Dataset**
We generate synthetic data using:
- 1000 samples
- 4 centers (clusters)
- 2 features
- Standard deviation = 1.3

This creates clearly separable clusters.

**2. Visualize Raw Data**

We plot the generated blobs to understand the distribution before clustering.

**3. Apply Agglomerative Clustering**
    
    AgglomerativeClustering(n_clusters=4)

- The model merges clusters step-by-step.
- We specify n_clusters=4 to stop merging at 4 groups.
- The predicted cluster labels are visualized using different colors.

**4. Dendrogram Visualization**
Using SciPy:

    linkage(X, method='ward')
    dendrogram(L)

The dendrogram:
- Shows hierarchical merging
- Helps determine optimal number of clusters
- Visualizes distance at which clusters merge

## 📈 Output
- Scatter plot of original dataset
- Clustered dataset visualization
- Dendrogram showing hierarchical structure

## ⚙️ Libraries Used
- scikit-learn
- matplotlib
- scipy

Install dependencies:

    pip install scikit-learn matplotlib scipy

**🚀 Why Use Hierarchical Clustering?**

✔ No need to pre-specify cluster centroids
✔ Dendrogram helps choose optimal cluster number
✔ Works well for small-to-medium datasets
✔ Captures hierarchical relationships

**📊 When to Use It?**
- When you want a cluster hierarchy
- When number of clusters is unknown
- When dataset size is manageable (not ideal for very large datasets due to O(n²) complexity)

### 🔎 Complexity

**Time Complexity:**
- O(n² log n) (varies with implementation)

**Space Complexity:**
- O(n²)

## 🎯 Conclusion

Agglomerative Hierarchical Clustering is a powerful technique for discovering natural groupings in data while also providing insight into the hierarchical structure of clusters.

This project demonstrates:
- Data generation
- Model implementation
- Cluster visualization
- Hierarchical interpretation using dendrograms