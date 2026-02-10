# Voting Regressor Example (Scikit-learn)

## 📌 Introduction

This project demonstrates the use of a **Voting Regressor**, an ensemble learning technique used for **regression problems**.  
Instead of depending on a single regression model, a Voting Regressor combines predictions from multiple regressors and outputs their average prediction.

Ensemble regression methods often lead to:
- Better generalization
- Reduced model variance
- Improved predictive stability

---

## 🗳️ What is a Voting Regressor?

A **Voting Regressor** is an ensemble method that aggregates predictions from several base regression models.

### How it works:
- Each regressor predicts a continuous value
- The final prediction is the **average of all predictions**

Unlike classification, voting in regression is always numerical averaging (no hard/soft voting).

---

## 🚀 Models Used

This project combines three different regression algorithms:

- **Linear Regression** – Captures linear relationships
- **Decision Tree Regressor** – Handles non-linear patterns
- **Support Vector Regressor (SVR)** – Margin-based regression model

The diversity of these models helps improve overall performance.

---

## 🧪 Dataset

- Synthetic regression dataset generated using `make_regression`
- **Samples:** 1000  
- **Features:** 20  
- **Informative features:** 10  
- **Noise:** 0.1  

The dataset is split into:
- **80% training**
- **20% testing**

---

## 🛠️ Implementation Steps

1. Generate a synthetic regression dataset
2. Split the data into training and testing sets
3. Initialize individual regression models
4. Combine them using `VotingRegressor`
5. Train the ensemble model
6. Evaluate performance using R² score

---

## 📊 Evaluation Metrics

### R² Score
- **Training R² Score:** ~0.72
- **Testing R² Score:** ~0.71

The close training and testing scores indicate **good generalization** with minimal overfitting.

### Interpretation
- R² ≈ 0.71 means the model explains around **71% of the variance** in the target variable
- Performance is consistent across training and test data

---

## ✅ Key Takeaways

- Voting regressors improve prediction stability
- Combining linear and non-linear models is effective
- Ensemble methods are simple to implement using Scikit-learn

---

## 📚 Requirements

- Python 3.x
- scikit-learn
- NumPy

**Install dependencies:**
    
    pip install scikit-learn numpy
