# K-Nearest Neighbors (KNN) classification

##K-Nearest Neighbors (KNN)
    K-Nearest Neighbors (KNN) is a simple, intuitive, and widely used supervised machine learning algorithm for both classification and regression tasks. Instead of learning explicit model parameters, KNN makes predictions by comparing a data point to the K closest points in the training dataset using a distance metric (such as Euclidean distance).
    For classification, the algorithm assigns the most common label among the K nearest neighbors. For regression, it predicts the average value of those neighbors. Because KNN is non-parametric and lazy, it requires minimal training but can be computationally expensive at prediction time.
    KNN is easy to understand, works well with small datasets, and serves as a strong baseline for many machine learning problems.

This project implements a K-Nearest Neighbors (KNN) classification model using scikit-learn. It demonstrates a complete machine learning workflow, including data splitting, feature scaling, model training, performance evaluation, and hyperparameter tuning with GridSearchCV and cross-validation. The goal is to show how tuning model parameters and using proper validation techniques can significantly improve classification accuracy.

# Dataset
    - heart.csv

# 📌 Project Overview
The notebook walks through:
- Splitting data into training and testing sets
- Building a machine learning pipeline
- Training a KNN classifier
- Evaluating model performance using accuracy
- Optimizing hyperparameters using GridSearchCV
- Applying cross-validation for more reliable results

# 🛠️ Technologies Used
- Python 🐍
- NumPy
- Pandas
- scikit-learn
- Jupyter Notebook

# 📊 Workflow Breakdown
1. Data Preparation
- Features (X) and target (y) are separated
- Dataset is split using train_test_split
- Reproducibility ensured with random_state

2. Pipeline Creation
- A pipeline is used to streamline preprocessing and modeling:
- StandardScaler for feature scaling
- KNeighborsClassifier for classification

Pipeline([
    ("Scale", StandardScaler()),
    ("Model", KNeighborsClassifier())
])

3. Baseline Model Evaluation
- The initial KNN model is trained
- Accuracy is evaluated on the test set

4. Hyperparameter Tuning (GridSearchCV)
- Tuned the n_neighbors parameter
- Tested multiple values to find the optimal K
    - param_grid = {'n_neighbors': [3,5,7,9,11,13,15,17]}

- Best parameter found:
    - n_neighbors = 5

5. Cross-Validation
- Applied 5-fold cross-validation
- Improves generalization and reduces overfitting
- Final accuracy improved significantly after tuning

# Results
    Model Stage	                   Accuracy
    - Baseline KNN	                ~0.75
    - Tuned KNN	                    ~0.85
    - Tuned + Cross-Validation	    ~0.88

✔️ Best performance achieved with 5 neighbors

# How to Run the Project
1. Clone the repository
2. Install dependencies
3. Open the notebook
4. Run all cells to reproduce results

# 📈 Key Takeaways
- Feature scaling is crucial for distance-based models like KNN
- Hyperparameter tuning can significantly improve accuracy
- Cross-validation provides more reliable performance estimates
- Pipelines help keep ML workflows clean and reproducible
