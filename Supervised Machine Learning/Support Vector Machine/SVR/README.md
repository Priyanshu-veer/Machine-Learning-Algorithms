# 📊 Support Vector Regression (SVR) on Diabetes Dataset

This repository demonstrates the implementation of Support Vector Regression (SVR) using scikit-learn on the Diabetes dataset.
The project covers data loading, preprocessing, model training, evaluation, and hyperparameter tuning using GridSearchCV.

# 📌 Project Overview
- Dataset: Diabetes Dataset (sklearn)
- Model: Support Vector Regression (SVR)
- Task: Regression
- Evaluation Metric: R² Score
- Hyperparameter Tuning: GridSearchCV

This project is part of my Supervised Machine Learning practice to build strong fundamentals and reusable ML pipelines.

# 🗂 Dataset Information
- Source: sklearn.datasets.load_diabetes
- Samples: 442
- Features: 10 numerical features
- Target: Disease progression score
- Example features:
    age
    sex
    bmi
    bp
    s1 – s6

# ⚙️ Tech Stack Used
- Python
- Pandas
- Scikit-learn
- Jupyter Notebook

# 🔁 Workflow
- Load Dataset
- Feature–Target Split
- Train–Test Split
- Target Scaling (StandardScaler)
- Train SVR Model
- Model Evaluation
- Hyperparameter Tuning using GridSearchCV

# 🧠 Model Training
    from sklearn.svm import SVR
    
    svr = SVR()
    svr.fit(X_train, y_train_scaled)
    y_pred = svr.predict(X_test)

# 📈 Model Evaluation

- Metric Used: R² Score
- Initial R² Score: ~0.50

        from sklearn.metrics import r2_score
        r2_score(y_test_scaled, y_pred)

# 🔍 Hyperparameter Tuning

Performed GridSearchCV to find optimal parameters:

    param_grid = {
        "C": [2,4,6,8,9,10],
        "kernel": ["rbf", "linear", "poly"],
        "epsilon": [0.1,0.2,0.3,0.01,0.02,0.03]
    }

# ✅ Best Parameters Found
    {
      'C': 8,
      'epsilon': 0.2,
      'kernel': 'linear'
    }

- Best Cross-Validated R² Score: ~0.46

# 📌 Key Learnings
- Importance of scaling target variables for SVR
- Effect of kernel selection
- How C and epsilon influence regression performance
- Practical use of GridSearchCV

# 🚀 Future Improvements
- Feature scaling using Pipeline
- Compare SVR with:
    - Linear Regression
    - Ridge & Lasso
    - Random Forest Regressor
- Visualization of predictions vs actual values
- Cross-validation performance analysis