# Stacking Regressor
## 🔍 Project Overview

This project demonstrates the implementation of a Stacking Regressor using Scikit-learn in Python. Stacking is an ensemble learning technique that combines multiple regression models to improve prediction performance.

The model is trained on a synthetic regression dataset generated using make_regression() and evaluated using the R² score.

## Introduction to Stacking (Stacked Generalization)
**What is Stacking?**

Stacking, also known as Stacked Generalization, is an ensemble learning method where:

- Multiple base models (Level-0 models) are trained on the dataset.
- Their predictions are used as inputs to another model.
- A final model (Level-1 model or Meta-Model) makes the final prediction.

Instead of depending on one algorithm, stacking combines the strengths of multiple algorithms to produce better generalization performance.

### How Stacking Works
- Train base regressors on training data.
- Generate predictions from each base model.
- Use those predictions as new features.
- Train a final estimator on those features.
- The final estimator produces the final prediction.

### Dataset

The dataset is synthetically generated using:
- 1000 samples
- 20 features
- 10 informative features
- Noise = 0.2
- Random state = 42

        make_regression(
            n_samples=1000,
            n_features=20,
            n_informative=10,
            noise=0.2,
            random_state=42
        )

The data is split into:
- 80% Training Data
- 20% Testing Data

### 🤖 Models Used
**Base Regressors (Level-0 Models)**
1. Linear Regression
2. Decision Tree Regressor (max_depth = 3)
3. Support Vector Regressor (SVR)

**Final Estimator (Meta-Model)**
1. Linear Regression

Cross-validation (cv=5) is used internally in the stacking process.

***Architecture in This Project***
         
                Base Models
     -----------------------------------
     | Linear Regression              |
     | Decision Tree Regressor        |
     | Support Vector Regressor (SVR) |
     -----------------------------------
                   ↓
             Final Estimator
           Linear Regression
                   ↓
              Final Prediction

### 🚀 Model Training

The stacking regressor is trained using:

    stacking_regressor.fit(X_train, y_train)

### 📈 Model Evaluation

The model performance is evaluated using R² Score.

**Test R² Score**
    
    Stacking Regressor R² Score: 0.9999988125627736

**Training vs Testing Performance**

    Stacking Training Score: 0.999998405462629
    Stacking Testing Score: 0.9999988125627736

### 📊 Interpretation of Results
- The R² score is extremely close to 1.
- This indicates excellent model performance.
- Training and testing scores are nearly identical.
- This suggests minimal overfitting.
- The ensemble model generalizes very well on unseen data.

### 🛠 Libraries Used
- scikit-learn
- numpy (implicitly used by sklearn)

Install dependencies using:

    pip install scikit-learn

### 📌 Key Takeaways
- Stacking combines multiple regression models for better performance.
- Linear Regression works effectively as a meta-learner.
- Ensemble methods often outperform single models.
- Cross-validation inside stacking improves robustness.

### 📚 Conclusion

This project demonstrates how to implement and evaluate a Stacking Regressor using Scikit-learn. By combining Linear Regression, Decision Tree Regressor, and SVR into a stacked ensemble, the model achieves near-perfect prediction performance on synthetic regression data.