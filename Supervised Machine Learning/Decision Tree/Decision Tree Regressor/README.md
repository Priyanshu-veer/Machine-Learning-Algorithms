## Decision Tree Regressor on Diabetes Dataset

# 📌 Overview

This project demonstrates the use of a Decision Tree Regressor to predict disease progression using the Diabetes dataset provided by scikit-learn.
The project also explores Cost Complexity Pruning (CCP) to control overfitting and improve generalization.

# 📊 Dataset
- Source: sklearn.datasets.load_diabetes
- Samples: 442
- Features: 10 numerical features
- Target: Disease progression after one year

# Features
- age
- sex
- bmi
- bp
- s1, s2, s3, s4, s5, s6

# 🧠 Model
- Algorithm: DecisionTreeRegressor
- Metrics Used:
    - R² Score
    - Mean Squared Error (MSE)

# 🔧 Data Preparation
- Split data into training and testing sets
- 70% training, 30% testing
- Random state set for reproducibility

        X = df.drop("target", axis=1)
        y = df["target"]
        
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.3, random_state=42
        )

# 🌲 Initial Model Training
    dt = DecisionTreeRegressor(
        max_depth=7,
        min_samples_leaf=20
    )
    dt.fit(X_train, y_train)

# 📈 Performance
- R² Score: ~0.41
- Mean Squared Error: ~3177

# ✂️ Cost Complexity Pruning

To reduce overfitting, cost complexity pruning was applied.

### Extract CCP Alphas
    path = full_tree.cost_complexity_pruning_path(X_train, y_train)
    ccp_alphas = path.ccp_alphas

### Train Models for Different Alpha Values
    for alpha in ccp_alphas:
        model = DecisionTreeRegressor(
            random_state=42,
            ccp_alpha=alpha
        )
        model.fit(X_train, y_train)

### Best Result After Pruning
- Best R² Score: ~0.39516206956807265
- Best ccp_alpha: ~0.39516206956807265

# ❗ Observations
- Pruning slightly reduced overfitting but did not significantly improve performance
- Decision Trees struggle with small datasets and linear relationships
- Diabetes dataset is not ideal for a single decision tree

# ⚠️ Why Performance Is Limited
- High variance nature of decision trees
- Limited dataset size
- Mostly linear relationships in data
- Overfitting or underfitting depending on tree depth

# 🚀 Possible Improvements
## Use ensemble models:
- RandomForestRegressor
- GradientBoostingRegressor

## Try linear models:
- LinearRegression
- Ridge
- Lasso
## Apply cross-validation (GridSearchCV)
## Feature engineering and scaling

# ✅ Conclusion

The Decision Tree Regressor with cost complexity pruning was implemented correctly, but the model achieved moderate performance.
For better results on the Diabetes dataset, ensemble or linear models are recommended.

# 📚 Requirements
- Python
-scikit-learn
- pandas
- numpy
- matplotlib

# 🏁 How to Run
1. Load the dataset
2. Train the model
3. Apply pruning
4. Evaluate performance using R² and MSE