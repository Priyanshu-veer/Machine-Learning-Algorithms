# PCA Dimensionality Reduction & 4D Data Visualization

## 📌 Project Overview

This project demonstrates:
- Generating synthetic 4-dimensional clustered data
- Visualizing high-dimensional data using:
    - 3D scatter plots
    - Color encoding for the 4th dimension
- Reducing dimensionality using Principal Component Analysis (PCA)
- Comparing data before and after dimensionality reduction

The goal is to understand how high-dimensional data can be visualized and compressed while preserving important structure.

## 🧠 Algorithms Used
**1.Blob Data Generation**

We use `make_blobs()` from `sklearn.datasets` to generate synthetic clustered data.

**What it does:**
- Creates isotropic Gaussian blobs for clustering
- Allows control over:
    - Number of samples
    - Number of features
    - Number of cluster centers
    - Random seed for reproducibility

**In this project:**
- Samples: 1000
- Features: 4 (4D space)
- Clusters: 4
- Random state: 42

This provides a structured dataset ideal for visualization and PCA demonstration.

**2. 3D Visualization with 4th Dimension as Color**

Since humans cannot directly visualize 4D space:
- First 3 features → mapped to X, Y, Z axes
- 4th feature → encoded using color gradient

This allows us to:
- Observe spatial clustering in 3D
- Understand how the 4th dimension influences separation

We also compare:
- Pure 3D scatter
- 3D scatter + 4th dimension encoded as color

# 3. Principal Component Analysis (PCA)
**📖 What is PCA?**

**Principal Component Analysis (PCA)** is a dimensionality reduction technique that transforms data into a new coordinate system.

It:
1. Finds directions (principal components) where the data varies the most
2. Orders them by explained variance
3. Projects data onto the top components
4. Reduces dimensionality while preserving maximum information

**🔍 How PCA Works (Mathematically)**
1. Standardize data
2. Compute covariance matrix
3. Calculate eigenvalues & eigenvectors
4. Sort eigenvectors by eigenvalues (variance)
5. Select top k components
6. Project data onto new feature space

## 📊 In This Project
- Original shape: (1000, 4)
- PCA components: 2
- Transformed shape: (1000, 2)

Example explained variance ratio:

    [0.4685, 0.3743]


This means:
- PC1 explains ~46.8% of variance
- PC2 explains ~37.4% of variance
- Together ≈ 84% of total variance retained

This shows that most information from 4D data is preserved in 2D.

## 📈 Visualization Comparison
**Before PCA**
- Data plotted using first two original features
- Shape: (1000, 4)

**After PCA**
- Data plotted using 2 principal components
- Shape: (1000, 2)
- Clusters remain clearly separable

This demonstrates PCA's ability to:
- Compress data
- Maintain cluster structure
- Improve visualization

## 🛠 Technologies Used
- Python
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn

### 🚀 How to Run

**1. Install dependencies:**

    pip install numpy matplotlib seaborn scikit-learn

**2. Run the notebook or script.**

## 🎯 Key Learnings
- High-dimensional data can be visualized using projection techniques.
- The 4th dimension can be encoded using color.
- PCA efficiently reduces dimensionality while preserving structure.
- Explained variance helps measure information retention.

## 📌 Future Improvements
- Apply StandardScaler before PCA (best practice)
- Try 3D PCA (n_components=3)
- Compare with t-SNE
- Compare with UMAP
- Apply clustering (KMeans) before and after PCA