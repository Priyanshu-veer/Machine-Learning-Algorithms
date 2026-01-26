# Linear Regression from Scratch

This repository contains an implementation of the Linear Regression algorithm using Python.
The goal is to understand the working of the algorithm using high-level ML libraries.

Linear Regression is a supervised machine learning algorithm used for predicting continuous values.
It models the relationship between input features and the target variable by fitting a linear equation.

Dataset:
- Type: Synthetic
- Source: sklearn.datasets.make_regression
- Also use Salary Dataset

Steps:
- Loaded and explored the dataset
- Performed basic preprocessing
- Implemented the Linear Regression algorithm
- Trained the model
- Evaluated performance using R^2 score, Adjusted R^2 Score, Mean Absolute Error, Mean Squared Error, Root Mean Squared Error 

## Pipeline Used
A scikit-learn Pipeline was used to combine preprocessing and model training steps.
This ensures consistent transformations and prevents data leakage.

Pipeline steps:
- StandardScaler
- Model (e.g., Linear Regression)


Language: Python
Libraries used:
- NumPy
- Pandas
- Matplotlib
- Scikit-learn

Model Performance (Synthetic Dataset):
- R^2 score: 1.0
- Adjusted r^2: 1.0
- Mean absolute error: 5.682553386177069e-15
- Mean squared error: 5.451486750338147e-29
- Root mean absolute error: 7.383418415841098e-15

Model Performance (Salary Dataset):
- R^2 score: 0.9024461774180498
- adjusted r^2: 0.8780577217725622
- Mean absolute error: 6286.453830757743
- Mean square error: 49830096.855908364
- Root mean squared error: 7059.043621901508

Model Performance (Salary Dataset Using Pipeline):
- R^2 score: 0.9024461774180499
- Adjusted r^2: 0.8780577217725624
- Mean absolute error: 6286.453830757742
- Mean square error: 49830096.8559083
- Root mean squared error: 7059.043621901504

A plot showing predicted(Best Fit Line) vs actual values is included.

How to run
1. Clone the repository
2. Install required libraries
3. Run the notebook or Python script
