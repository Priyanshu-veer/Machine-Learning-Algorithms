# Stacking Classifier
## 🔍 Project Overview

This project demonstrates how to implement a Stacking Classifier using Scikit-learn in Python. Stacking (also known as Stacked Generalization) is an ensemble learning technique that combines multiple machine learning models to improve predictive performance.

The model is trained on a synthetic classification dataset generated using `*make_classification()*` and evaluated using accuracy score, classification report, and confusion matrix.

## Introduction to Stacking Algorithm
**What is Stacking?**

Stacking is an ensemble learning method that combines multiple base models (level-0 models) and trains a meta-model (level-1 model) to make the final prediction.

Instead of relying on a single model, stacking leverages the strengths of different models to reduce bias and variance.

**How It Works**
1. Base Models (Level-0 models) are trained on the original dataset.
2. Their predictions are collected.
3. A Meta-Model (Level-1 model) is trained on those predictions.
4. The meta-model produces the final prediction.

### Architecture in This Project
    
                    Base Models
         -----------------------------------
         | Logistic Regression             |
         | Decision Tree Classifier        |
         | Support Vector Classifier (SVC) |
         -----------------------------------
                       ↓
                 Final Estimator
               Logistic Regression
                       ↓
                  Final Prediction

### Why Use Stacking?
- Combines strengths of different algorithms
- Often achieves better generalization performance
- Reduces overfitting compared to individual models

### Libraries Used
- sklearn.ensemble.StackingClassifier
- sklearn.datasets.make_classification
- sklearn.model_selection.train_test_split
- sklearn.linear_model.LogisticRegression
- sklearn.tree.DecisionTreeClassifier
- sklearn.svm.SVC
- sklearn.metrics

### Dataset

A synthetic dataset is generated using:
- 1000 samples
- 20 features
- 10 informative features
- 2 redundant features
- Binary classification
- Random state: 42

        make_classification(
            n_samples=1000,
            n_features=20,
            n_informative=10,
            n_redundant=2,
            random_state=42
        )


The dataset is split as:
- 80% Training
- 20% Testing

### 🤖 Models Used
**Base Learners:**
- Logistic Regression
- Decision Tree (max_depth=3)
- Support Vector Classifier (SVC)

### Final Estimator (Meta-Learner):
- Logistic Regression

Cross-validation (cv=5) is used internally during stacking.

#### 🚀 Model Training
stacking_classifier.fit(X_train, y_train)

### 📊 Model Evaluation
**Accuracy**
- Training Accuracy: 0.98125
- Testing Accuracy: 0.96

This indicates strong generalization with minimal overfitting.

**📋 Classification Report**

| Class	  | Precision  | Recall	  | F1-score  |	Support |
| ------- | ---------- | -------- | --------- | --------|
|0	      | 0.98       | 0.94	  | 0.96	  | 104     |
|1	      | 0.94       | 0.98	  | 0.96	  | 96      | 

- Overall Accuracy: 96%
- Balanced performance across classes

**🔢 Confusion Matrix**

    [[98  6]
     [ 2 94]]

- 98 True Negatives
- 94 True Positives
- 6 False Positives
- 2 False Negatives

## 📈 Key Takeaways
- Stacking improves predictive performance by combining multiple models.
- Logistic Regression performs well as both base learner and meta-learner.
- The model shows high accuracy with balanced precision and recall.
- Minimal overfitting (training accuracy ≈ testing accuracy).