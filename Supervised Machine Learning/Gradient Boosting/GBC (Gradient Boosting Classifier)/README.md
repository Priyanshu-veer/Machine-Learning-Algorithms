# 🚀 Gradient Boosting Classifier
## 📌 Project Overview

This project demonstrates the end-to-end workflow of a supervised machine learning classification problem using Gradient Boosting Classifier from scikit-learn.
- The focus is not only on model training but also on:
- Model evaluation
- Overfitting & underfitting analysis
- Cross-validation
- Hyperparameter tuning using GridSearchCV

This project is created for learning and practice purposes to deeply understand ensemble learning techniques.

## 🧠 Problem Statement

Build a binary classification model using synthetic data and analyze:
- Model performance before tuning
- Overfitting vs generalization
- Performance improvement after hyperparameter optimization

## 🗂 Dataset

Dataset generated using make_classification
- Samples: 1000
- Features: 10
    - Informative: 8
    - Redundant: 2
- Target Classes: 2

        make_classification(
            n_samples=1000,
            n_features=10,
            n_informative=8,
            n_redundant=2,
            n_classes=2,
            random_state=42
        )


  *📌 Synthetic data is used to clearly observe model behavior without real-world noise.*

## ⚙️ Model Used

**GradientBoostingClassifier**

Initial Hyperparameters

`- loss = "log_loss"`

`- learning_rate = 0.001`

`- n_estimators = 100`

`- max_depth = 3`

`- subsample = 0.8`

## 📊 Model Evaluation (Before Tuning)
**Metrics Used**
- Accuracy
- Precision, Recall, F1-score
- Train vs Test accuracy comparison
- Cross-validation score

**Results**
        
        - Metric	                   Score
        
        - Training Accuracy	           0.81
        
        - Testing Accuracy	           0.735
        
        - Cross-Validation Mean	      ~0.746

**📌 Observation:**
The model shows slight overfitting, as training accuracy is higher than testing accuracy.

### 🔍 Overfitting & Underfitting Analysis
- Compared training vs testing accuracy
- Used cross-validation to validate generalization
- Identified variance issue and applied tuning

### 🛠 Hyperparameter Tuning (GridSearchCV)
**Parameters Tuned**
        
        {
          "learning_rate": [0.0001, 0.001, 0.01, 0.1],
          "max_depth": [2, 3, 4, 5],
          "n_estimators": [80, 90, 100, 120]
        }


- Cross-Validation: 5-fold
- Scoring Metric: Accuracy

## ⭐ Best Model After Tuning
**Best Parameters**
           
            learning_rate = 0.1
            max_depth = 4
            n_estimators = 100

**Performance**
           
            Metric	             Score
            Training Accuracy	 0.997
            Testing Accuracy	 0.845
            CV Mean Score	     ~0.878

**📌 Key Insight:**
Although training accuracy is high, test and CV scores improved significantly, indicating better generalization with controlled overfitting.

## 📈 Final Conclusion
- Gradient Boosting is powerful but prone to overfitting without tuning
- Cross-validation is essential to judge real performance
- GridSearchCV significantly improved model generalization
- High training accuracy alone is not a reliable metric

## 🧰 Tech Stack
- Python
- Scikit-learn
- Jupyter Notebook

# 📚 Learning Outcomes
✔ Ensemble learning concepts

✔ Bias-variance tradeoff

✔ Overfitting detection

✔ Cross-validation

✔ Hyperparameter optimization

✔ Proper ML evaluation workflow

# 🚀 Future Improvements
- Add ROC-AUC and confusion matrix
- Feature importance visualization
- Compare with Random Forest & XGBoost
- Apply regularization strategies
