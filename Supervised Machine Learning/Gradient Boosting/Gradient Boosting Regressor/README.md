# Gradient Boosting Regression with Hyperparameter Tuning

This project demonstrates how to build, evaluate, and tune a **Gradient Boosting Regressor** using **scikit-learn** on a synthetic regression dataset. It covers the full workflow from data generation to model evaluation and hyperparameter optimization using GridSearchCV.

---

## 📌 Project Overview

The goal of this project is to:

* Generate a synthetic regression dataset
* Train a Gradient Boosting Regression model
* Evaluate model performance using **R² Score** and **Mean Squared Error (MSE)**
* Detect **overfitting / underfitting** by comparing training and testing scores
* Improve performance using **GridSearchCV** for hyperparameter tuning

---

## 🧰 Technologies Used

* Python
* scikit-learn
* NumPy
* Jupyter Notebook

---

## 📊 Dataset Description

The dataset is generated using `make_regression` from `sklearn.datasets`.

**Dataset Parameters:**

* Samples: 1000
* Features: 20
* Informative Features: 10
* Targets: 1
* Noise: 0.5
* Random State: 42

This synthetic dataset is ideal for experimenting with regression algorithms.

---

## ⚙️ Model Configuration

The initial **GradientBoostingRegressor** is configured with:

* Loss Function: Squared Error
* Learning Rate: 0.1
* Number of Estimators: 100
* Max Depth: 3
* Min Samples Split: 3
* Min Samples Leaf: 2
* Random State: 42

---

## ✂️ Train-Test Split

The dataset is split as follows:

* Training Set: 80%
* Testing Set: 20%
* Random State: 42

---

## 📈 Model Evaluation

### Initial Model Performance

* **R² Score (Test):** ~0.924
* **Mean Squared Error:** ~2937

### Overfitting Check

| Metric   | R² Score |
| -------- | -------- |
| Training | ~0.987   |
| Testing  | ~0.924   |

✔ The model generalizes well with minimal overfitting.

---

## 🔍 Hyperparameter Tuning (GridSearchCV)

GridSearchCV is used to find the best combination of hyperparameters.

### Parameter Grid

* `learning_rate`: [0.1, 0.01, 0.2, 0.02]
* `n_estimators`: [100, 110, 115, 120]
* `max_depth`: [3, 4, 5, 6]

### GridSearch Configuration

* Cross-validation: 5-fold
* Scoring Metric: R²

---

## 🏆 Best Model Results

**Best Parameters:**

* Learning Rate: 0.2
* Max Depth: 3
* Number of Estimators: 120

**Performance:**

| Metric   | R² Score |
| -------- | -------- |
| Training | ~0.995   |
| Testing  | ~0.932   |

🚀 The tuned model shows improved performance over the baseline model.

---

## 📂 Project Structure

```
├── gradientboostingregressor.ipynb
├── README.md
```

---

## ✅ Key Learnings

* Gradient Boosting performs well on complex regression problems
* Comparing training and testing scores helps detect overfitting
* Hyperparameter tuning significantly improves model performance
* GridSearchCV is a powerful tool for systematic model optimization

---

## 📌 Future Improvements

* Try **XGBoost / LightGBM** for better performance
* Perform **feature importance analysis**
* Use **cross-validation plots** for deeper insights
* Apply the workflow to a real-world dataset

---

⭐ If you find this project helpful, consider giving it a star!
