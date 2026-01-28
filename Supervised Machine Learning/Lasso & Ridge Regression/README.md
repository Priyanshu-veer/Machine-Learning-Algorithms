## 📌 Dataset
The dataset (insurance.csv) contains 1338 rows and 7 columns:
    Column	        Description
    age	           Age of the individual
    sex	           Gender (male/female)
    bmi	           Body Mass Index
    children	   Number of children
    smoker	       Smoking status (yes/no)
    region	       Residential region
    charges	       Medical insurance charges (target variable)

# 🛠️ Libraries Used
- pandas
- scikit-learn
    - LinearRegression
    - Lasso
    - StandardScaler
    - OneHotEncoder
    - ColumnTransformer
    - Pipeline
    - train_test_split
    - r2_score

# ⚙️ Feature Engineering

- Numerical features are scaled using StandardScaler
- Categorical features are encoded using OneHotEncoder
- ColumnTransformer is used to apply transformations efficiently
- A Pipeline is created to combine preprocessing and modeling

num_cols = X.select_dtypes(exclude='object').columns
cat_cols = X.select_dtypes(include='object').columns

# 🤖 Models Implemented
1. Lasso Regression
- Helps with feature selection using L1 regularization
- Handles multicollinearity
- R² Score: ~0.785

2. Ridge Regression
- Uses L2 regularization
- Reduces overfitting
- R² Score: ~0.785

Both models are trained using an 80/20 train-test split.

# 📊 Model Evaluation
- Evaluation Metric: R² Score
- The performance of both Lasso and Ridge models is comparable on this dataset.