# Logistic Regression From Scratch

This repository contains an implementation of the Logistic Regression algorithm using Python.
The goal is to understand the working of the algorithm using high-level ML libraries.

Logistic Regression is a supervised machine learning algorithm used for classification tasks, especially binary classification.
It models the relationship between input features and a categorical target variable by using a logistic (sigmoid) function to estimate probabilities and assign class labels.


Dataset:
- Type: Synthetic
- Source: sklearn.datasets.make_classification
- Also use Employee Turnover

Steps:
- Loaded and explored the dataset
- Performed basic preprocessing
- Implemented the Logistic Regression algorithm
- Trained the model
- Evaluated performance using Accuracy Score, Precision Score, Recall Score, F1 Score, Classification Report & Confusion Matrix

## Pipeline Used
A scikit-learn Pipeline was used to combine preprocessing and model training steps.
This ensures consistent transformations and prevents data leakage.

Pipeline steps:
- StandardScaler
- Model (e.g., Logistic Regression)


Language: Python
Libraries used:
- NumPy
- Pandas
- Scikit-learn

Model Performance (Synthetic Dataset):
- Accuracy Score : 0.9475
- Precision Score : 0.96875
- Recall Score : 0.9220512820512821
- F1 Score : 0.9448239621650026
- Classification Report : 
                  precision    recall  f1-score   support
    
               0       0.93      0.97      0.95      1025
               1       0.97      0.92      0.94       975
    
        accuracy                           0.95      2000
       macro avg       0.95      0.95      0.95      2000
    weighted avg       0.95      0.95      0.95      2000

- Confusion Matrix 
              Predicted 0  Predicted 1
    Actual 0          996           29
    Actual 1           76          899

Model Performance (Employee Turnover Dataset):
- Accuracy Score : 0.8518518518518519
- Precision Score : 0.8609625668449198
- Recall Score : 0.8256410256410256
- F1 Score : 0.8429319371727748
- Classification Report : 
                  precision    recall  f1-score   support
    
               0       0.84      0.88      0.86       210
               1       0.86      0.83      0.84       195
    
        accuracy                           0.85       405
       macro avg       0.85      0.85      0.85       405
    weighted avg       0.85      0.85      0.85       405

- Confusion Matrix 
              Predicted 0  Predicted 1
    Actual 0          184           26
    Actual 1           34          161


Model Performance (Employee Turnover Dataset Using Pipeline):
- Accuracy Score : 0.8629629629629629
- Precision Score : 0.8666666666666667
- Recall Score : 0.832
- F1 Score : 0.8489795918367347
- Classification Report : 
                  precision    recall  f1-score   support
    
               0       0.86      0.89      0.87       145
               1       0.87      0.83      0.85       125
    
        accuracy                           0.86       270
       macro avg       0.86      0.86      0.86       270
    weighted avg       0.86      0.86      0.86       270

- Confusion Matrix : 
              Pridected 0  Predicted 1
    Actual 0          129           16
    Actual 1           21          104


  How to run
1. Clone the repository
2. Install required libraries
3. Run the notebook or Python script