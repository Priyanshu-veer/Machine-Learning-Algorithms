# Decision Tree

A Decision Tree is a supervised machine learning algorithm used for both classification and regression tasks. It models decisions using a tree-like structure where internal nodes represent feature-based conditions, branches represent outcomes of those conditions, and leaf nodes represent final predictions.

Decision Trees mimic human decision-making by splitting data into smaller subsets based on feature values, making them highly interpretable and easy to understand. At each split, the algorithm selects the feature that best separates the data using metrics such as Gini Impurity, Entropy, or Information Gain.

# Decision Tree Classifier

A Decision Tree Classifier is a specific type of decision tree used for classification problems, where the target variable consists of discrete class labels (e.g., survived vs. not survived).

The classifier works by:
- Selecting the best feature to split the data.
- Recursively splitting the dataset into subsets.
- Assigning class labels at the leaf nodes based on majority voting.

The model continues splitting until a stopping criterion is met, such as maximum depth or minimum samples per leaf.

# 📌 Project Overview

This project demonstrates the implementation of a Decision Tree Classifier using the Titanic dataset from the seaborn library.
The workflow covers data loading, preprocessing, feature engineering, model training, and tree visualization — including basic, pre-pruned, and post-pruned decision tree models.

The goal is to understand how decision trees behave and how pruning helps control overfitting.

## Dataset
- Source : seaborn.load_dataset('titanic')
- target variable : survived
- Type : Binary classification

## Steps
- Loaded & explored the dataset
- Perform basic preprocessing (LabelEncoder, SimpleImputer, Remove colums)
- Implemented Decision Tree Classifier algorithm
- Trained the model
- Evaluate accuracy score, classification report, confusion matix
- Also perfom **Pre-Prunning** (To reduce overfitting) & **Post-Prunning** (Used Cost Complexity Pruning (ccp_alpha))

## Model Visualization
All models were visualized using plot_tree() from sklearn.tree:
- Basic Decision Tree
- Pre-Pruned Tree
- Post-Pruned Tree

Visualizations include:
- Feature names
- Class labels
- Gini impurity
- Sample counts

## Evaluation Metrics
- Accuracy Score used to compare models.
- Observed improvements in generalization after pruning.

## Library Used
- Python
- Sklearn
- Pandas
- Matplotlib
- Seaborn


## Key Learnings
- Decision Trees are easy to interpret but prone to overfitting.
- Pre-pruning controls complexity early.
- Post-pruning refines an already trained tree.
- Visualization helps understand decision paths clearly.

## Conclusion
This notebook provides a complete, beginner-friendly walkthrough of decision tree classification with practical pruning techniques. It highlights how model complexity affects performance and interpretability.