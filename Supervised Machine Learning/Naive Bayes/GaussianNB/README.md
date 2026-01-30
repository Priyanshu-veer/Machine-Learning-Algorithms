# Naive Bayes Classification

## Introduction

 Naive Bayes is a family of probabilistic machine learning algorithms based on Bayes’ Theorem, commonly used for classification tasks. The key assumption behind Naive Bayes is that features are conditionally independent given the class label. Although this assumption is often unrealistic in real-world data, Naive Bayes models perform surprisingly well in many practical applications due to their simplicity and efficiency.

Naive Bayes classifiers are:
- Fast to train and predict
- Effective with small datasets
- Robust to irrelevant features
- Widely used in medical diagnosis, spam detection, and text classification

# Heart Disease Prediction using Naive Bayes

## Overview
 This project demonstrates the use of the **Naive Bayes** classification algorithm, specifically **Gaussian Naive Bayes (GaussianNB)**, to predict the presence of heart disease based on medical attributes. The model is implemented using **scikit-learn** and evaluated with standard classification metrics.

---

## Dataset
The dataset contains patient medical records with the following features:

- `age` – Age of the patient  
- `sex` – Gender (1 = male, 0 = female)  
- `cp` – Chest pain type  
- `trestbps` – Resting blood pressure  
- `chol` – Serum cholesterol  
- `fbs` – Fasting blood sugar  
- `restecg` – Resting ECG results  
- `thalach` – Maximum heart rate achieved  
- `exang` – Exercise-induced angina  
- `oldpeak` – ST depression induced by exercise  
- `slope` – Slope of the peak exercise ST segment  
- `ca` – Number of major vessels  
- `thal` – Thalassemia  
- `target` – Presence of heart disease (1 = Yes, 0 = No)

## Naive Bayes Classifier

### What is Naive Bayes?
 Naive Bayes is a **probabilistic classification algorithm** based on **Bayes’ Theorem**. It assumes that all features are conditionally independent given the class label. Despite this strong assumption, Naive Bayes often performs well in real-world classification tasks.

**Key characteristics:**
- Simple and fast
- Works well with small datasets
- Effective for baseline models

---

## Gaussian Naive Bayes (GaussianNB)

### Description
 Gaussian Naive Bayes is a variant of Naive Bayes used for **continuous numerical data**. It assumes that each feature follows a **Gaussian (normal) distribution** for each class.

For each feature, the algorithm estimates:
- Mean
- Variance

These parameters are used to compute class probabilities.

### Why GaussianNB?
GaussianNB is suitable for this project because:
- Medical attributes are continuous
- The dataset is relatively small
- It provides good performance with minimal computation

---

## Model Implementation
- Data is split into training and testing sets
- GaussianNB is trained on the training data
- Predictions are made on the test set
- A **Pipeline** is also used to structure the model

---

## Evaluation Metrics
The model performance is evaluated using:
- **Accuracy**
- **Precision**
- **Recall**
- **F1-score**
- **Classification Report**
- **Confusion Matrix**

These metrics help assess both overall performance and class-wise predictions.

---

## Results
 The Gaussian Naive Bayes model achieves strong performance with balanced precision and recall, making it a reliable baseline model for heart disease classification.

---

## Libraries Used
- Python
- Pandas
- Scikit-learn

## Why GaussianNB?
 GaussianNB is especially suitable when:
- Features are numerical (e.g., age, blood pressure, cholesterol)
- Data roughly follows a bell-shaped (Gaussian) distribution
- You need a simple and interpretable baseline model

## Conclusion
 Gaussian Naive Bayes provides an efficient and interpretable approach for heart disease prediction. While it makes simplifying assumptions, it delivers solid results and serves as a strong baseline for comparison with more complex models.
