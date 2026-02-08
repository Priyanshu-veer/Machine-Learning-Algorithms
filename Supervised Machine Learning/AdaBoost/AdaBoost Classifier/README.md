# AdaBoost Classification

This project demonstrates a binary classification model built using AdaBoostClassifier with a Decision Tree (stump) as the base estimator. The workflow covers data generation, training, evaluation, hyperparameter tuning using GridSearchCV, and cross-validation.

## 📌 Project Overview
- Algorithm: AdaBoost (Adaptive Boosting)
- Base Estimator: DecisionTreeClassifier (max_depth = 1)
- Framework: Scikit-learn
- Task: Binary Classification
- Dataset: Synthetic dataset generated using make_classification

## 📊 Dataset Details

The dataset is generated using sklearn.datasets.make_classification with the following parameters:
- n_samples: 1000
- n_features: 20
- n_informative: 10
- n_redundant: 2
- n_classes: 2
- random_state: 42

This ensures reproducibility and a controlled environment for model evaluation.

# ⚙️ Model Architecture

    AdaBoostClassifier
    └── Base Estimator: DecisionTreeClassifier (max_depth=1)

**Initial parameters:**
- n_estimators = 50
- learning_rate = 1.0

**🧪 Train-Test Split**
- Training Set: 80%
- Testing Set: 20%
- Random State: 42

## 📈 Model Performance (Before Tuning)
_________________________________
| Metric	         |    Score
____________________ | _____________
| Training Accuracy	 |    91.38%
| Testing Accuracy	 |    85.00%

➡️ Slight gap between training and testing accuracy, but no major overfitting observed.

## 🔍 Hyperparameter Tuning

Hyperparameter optimization is performed using GridSearchCV with 5-fold cross-validation.
**Parameter Grid**
    
    {
      "n_estimators": [100, 150, 200],
      "learning_rate": [1.0, 0.1, 2.0]
    }

**Best Parameters Found**
- n_estimators: 200
- learning_rate: 0.1

## 🏆 Model Performance (After Tuning)
    
    Metric	                 |    Score
    ______________________________________
    Grid Training Accuracy	 |   88.38%
    Grid Testing Accuracy	 |  83.50%
    Best CV Accuracy	     |   85.50%

## Confusion Matrix (Test Set)

        [[80 24]
         [ 9 87]]


## 🔁 Cross-Validation

5-fold cross-validation was performed on the training set:
- Mean CV Accuracy: ~85.5%

This indicates stable generalization performance across folds.

## 📦 Dependencies
- Python 3.x
- scikit-learn

## 🚀 How to Run

1. Clone the repository
2. Run the notebook or Python script containing the model
3. Observe training, evaluation, and tuning results

## 📝 Key Takeaways
- AdaBoost with decision stumps performs well on structured data.
- Hyperparameter tuning slightly reduced overfitting.
- Cross-validation confirms consistent model performance.