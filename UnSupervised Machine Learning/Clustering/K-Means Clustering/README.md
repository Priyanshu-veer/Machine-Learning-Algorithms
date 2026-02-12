# 📊 K-Means Clustering with Elbow, KneeLocator & Silhouette Analysis
## 📌 Project Overview

This project demonstrates the implementation of the K-Means Clustering algorithm on a synthetic dataset generated using make_blobs.

The main objective is to:
- Apply K-Means clustering
- Determine the optimal number of clusters (K)
- Compare different evaluation techniques:
    - Elbow Method
    - KneeLocator (Automated Elbow Detection)
    - Silhouette Score

This project highlights why relying on only one evaluation metric may not always give the best clustering result.

## 🧠 About K-Means Algorithm
>**What is K-Means?**

K-Means is an unsupervised machine learning algorithm used to group data into K distinct clusters based on similarity.

It minimizes the Within-Cluster Sum of Squares (WCSS), also called inertia.

>**🔹 How K-Means Works**
1. Choose number of clusters (K)
2. Randomly initialize K centroids
3. Assign each data point to the nearest centroid
4. Recalculate centroids (mean of assigned points)
5. Repeat steps 3–4 until convergence

The algorithm stops when:
- Centroids no longer change significantly
- Maximum iterations are reached

### 📂 Dataset
- Generated using `*sklearn.datasets.make_blobs*`
- 100 samples
- 2 features
- 4 true cluster centers
- `*random_state=42*` for reproducibility

### 📈 Project Workflow
**1. Data Visualization**
- Plotted synthetic dataset
- Observed 4 visually separable clusters

**2. K-Means Clustering (Manual K = 4)**
- Set `*n_clusters=4*`
- Fitted model
- Visualized cluster assignments
- Plotted centroids

This confirms the expected clustering structure.

### 🔍 Finding Optimal K
**Method 1: Elbow Method**

We calculate WCSS for K = 1 to 10.

**Observation:**
- Sharp decrease from K=1 to K=3
- After K=3, curve flattens

> Elbow appears at K = 3

⚠️ Problem: True clusters = 4
Elbow method slightly underestimates K.

**Method 2: KneeLocator (Automated Elbow)**
Used `*kneed*` library:

    KneeLocator(range(1, 11), wcss, curve='convex', direction='decreasing')

**Detected:**

> Detected elbow: 3

Again suggests K = 3

**Method 3: Silhouette Score (Most Reliable Here)**
Silhouette Score measures:
- How close a point is to its own cluster
- How far it is from other clusters

**Formula intuition:**
- Range: -1 to 1
- Closer to 1 → better separation
- Around 0 → overlapping clusters
- Negative → wrong clustering
- We tested K from 2 to 20.

> 📌 Best Silhouette Score occurred at:

    Best K = 4


This correctly identifies the true number of clusters.

### 📊 Key Insight

|Method	             | Suggested K
| -------------------| ------------
|Elbow Method	     |    3
|KneeLocator	     |    3
|Silhouette Score	 |    4


## 🚨 Important Learning:
- Elbow method is heuristic and visual.
- Automated knee detection may fail if curve is smooth.
- Silhouette Score gives better quantitative validation.

👉 Always validate clustering using multiple evaluation techniques.

## 🛠 Technologies Used
- Python
- NumPy
- Matplotlib
- Scikit-learn
- Kneed

## 📌 Conclusion
- Successfully implemented K-Means clustering
- Compared cluster validation methods
- Demonstrated limitations of Elbow method
- Silhouette Score correctly identified true clusters
- Highlighted importance of evaluation in unsupervised learning