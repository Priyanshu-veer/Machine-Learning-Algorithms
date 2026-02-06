# Random Forest Classification
# 📌 Project Overview

This project demonstrates the use of a Random Forest Classifier on a synthetic dataset generated using make_classification.
The goal is to train, evaluate, and understand the performance of a Random Forest model using a standard train–test split approach.

# 🌲 Introduction to Random Forest

Random Forest is an ensemble learning algorithm that combines multiple decision trees to improve prediction accuracy and reduce overfitting.

## Key ideas:
- Builds many decision trees on random subsets of data
- Uses majority voting for classification
- Reduces variance compared to a single decision tree
- Works well with high-dimensional and non-linear data

## 📊 Dataset

The dataset is generated using sklearn.datasets.make_classification.

### Dataset configuration:
- Number of samples: 10,000
- Number of features: 40
- Informative features: 25
- Redundant features: 10
- Number of classes: 2
- Random state: 42

This synthetic dataset is useful for practicing machine learning workflows without relying on external data.

## ⚙️ Model Configuration

The Random Forest Classifier is initialized with manually selected hyperparameters for faster training.

    RandomForestClassifier(
        n_estimators=100,
        max_depth=5,
        random_state=42
    )

## Hyperparameters used:
- **n_estimators** = 100 → number of trees
- **max_depth** = 5 → limits tree depth to prevent overfitting
- **random_state** = 42 → ensures reproducibility

**Note**: GridSearchCV was initially attempted for hyperparameter tuning, but due to computational constraints, parameters were selected manually for this practice task.

## 🔀 Train–Test Split

The dataset is split into:
- 80% training data
- 20% testing data

        train_test_split(
            test_size=0.2,
            random_state=42
        )

## 📈 Model Evaluation

The model is evaluated using:
- Training accuracy
- Testing accuracy
- Classification report (precision, recall, F1-score)

**Results**

- Training Accuracy: 0.859
- Testing Accuracy: 0.811

The small difference between training and testing accuracy indicates that the model generalizes well and does not strongly overfit.

## Classification Report (Test Data)
- Balanced precision and recall across both classes
- Overall accuracy: 81%
- Macro and weighted averages are consistent, indicating stable performance

## ✅ Key Takeaways
- Random Forest performs well on high-dimensional synthetic data
- Manual hyperparameter selection can be effective when computational resources are limited
- Comparing training and testing accuracy helps detect overfitting
- Classification report provides deeper insight beyond accuracy alone

## 🚀 Future Improvements
- Apply RandomizedSearchCV for faster hyperparameter tuning
- Increase n_estimators for potentially better performance
- Experiment with different max_depth values
- Add a separate validation set or use cross-validation

## 🧠 Purpose

This project is created for learning and practice to understand:
- Random Forest fundamentals
- Model training and evaluation
- Practical limitations of hyperparameter tuning
