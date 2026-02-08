# AdaBoost Regression with Decision Tree (scikit-learn)

This project demonstrates **AdaBoost Regression** using a **Decision Tree Regressor (stump)** as the base estimator. It covers dataset generation, model training, evaluation, overfitting/underfitting checks, and **hyperparameter tuning using GridSearchCV**.

---

## 📌 Project Overview

* **Algorithm**: AdaBoost Regressor
* **Base Estimator**: DecisionTreeRegressor (max_depth = 1)
* **Library**: scikit-learn
* **Task**: Supervised Regression
* **Dataset**: Synthetic data generated using `make_regression`

---

## 🧠 Workflow

1. Generate synthetic regression data
2. Split data into training and testing sets
3. Train AdaBoost Regressor
4. Evaluate model performance (R², MSE)
5. Detect underfitting / overfitting
6. Tune hyperparameters using GridSearchCV
7. Re-evaluate optimized model

---

## 📊 Dataset Details

```text
Samples        : 1000
Features       : 20
Informative    : 10
Targets        : 1
Noise          : 0.1
Random State   : 42
```

Dataset is created using:

```python
make_regression()
```

---

## ⚙️ Model Configuration

### Base Estimator

* Decision Tree Regressor
* `max_depth = 1` (Decision Stump)

### AdaBoost Parameters (Initial)

* `n_estimators = 100`
* `learning_rate = 1.0`
* `loss = 'square'`

---

## 📈 Initial Model Performance

| Metric   | Training | Testing |
| -------- | -------- | ------- |
| R² Score | 0.674    | 0.642   |
| MSE      | 12274    | 13863   |

### 🔎 Observation

* Slight underfitting
* Bias present due to shallow base estimator

---

## 🔧 Hyperparameter Tuning (GridSearchCV)

### Parameter Grid

```python
{
  'n_estimators': [100, 200, 300, 400],
  'learning_rate': [1.0, 2.0, 3.0, 4.0],
  'loss': ['linear', 'square', 'exponential']
}
```

* **Cross-validation**: 5-fold
* **Scoring Metric**: R²

---

## 🏆 Best Model Parameters

```text
n_estimators  : 400
learning_rate: 4.0
loss          : linear
```

---

## 📊 Optimized Model Performance

| Metric   | Training | Testing |
| -------- | -------- | ------- |
| R² Score | 0.814    | 0.797   |
| MSE      | 7019     | 7864    |

### ✅ Improvements

* Higher accuracy
* Reduced error
* Better generalization

---

## 📦 Dependencies

Install required libraries:

```bash
pip install scikit-learn
```

---

## ▶️ How to Run

1. Clone the repository
2. Open the notebook / script
3. Run cells sequentially
4. Observe evaluation metrics

---

## 📚 Concepts Covered

* AdaBoost intuition
* Weak learners
* Bias–Variance tradeoff
* Regression metrics (R², MSE)
* GridSearchCV
* Model optimization

---

## 🚀 Future Improvements

* Try deeper trees (`max_depth > 1`)
* Compare with Gradient Boosting
* Visualize predictions vs actual values
* Add learning curves
