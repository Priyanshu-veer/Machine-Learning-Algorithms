# XGBoost Regression – Learning Behavior with Dataset Size
# 📌 Project Overview

This project demonstrates how XGBoost Regressor behaves when trained on a synthetic regression dataset and how dataset size impacts model learning, stability, and generalization.

The main goal is not just performance, but understanding:
- Overfitting on small datasets
- Stable learning on larger datasets
- Difference between *memorization and generalization*

# 🧠 Key Learning Insight

| On small datasets, the model can easily memorize patterns.
| On larger datasets, the model learns general trends instead of memorizing every data point.

This experiment helped me clearly observe that behavior.

# 🧪 Dataset Details

The dataset is generated using `*make_regression*` from `*sklearn*`.

**Parameters used:**
- `*n_samples = 20_000*`
- `*n_features = 40*`
- `*n_informative = 25*`
- `*noise = 0.1*`
- `*random_state = 42*`

This setup creates a moderately complex dataset with controlled noise.

⚙️ Model Used
- Model: `*XGBRegressor*`
- Library: `*xgboost*`
- Evaluation Metric: Mean Absolute Error (MAE)
- Train-Test Split:
    - 80% training
    - 20% testing

No heavy hyperparameter tuning was done intentionally, to observe default model behavior.

# 📊 Evaluation Metrics
The model is evaluated using:
- R² Score
- Mean Absolute Error (MAE)
- Mean Squared Error (MSE)

# 🔹 Results

| Metric	| Training	 | Testing  |
| --------- |------------|--------- |
| R² Score	| ~0.98	     | ~0.90    |
| MAE	    | ~27.56	 | ~67.27   |
| MSE	    | ~1265	     | ~7161    |


# 🔍 Observations
- Training performance is higher than testing, which is expected.
- The gap between training and testing metrics is reasonable, not extreme.
- This indicates good generalization, not overfitting.

# 📈 What I Learned
- On small datasets, XGBoost can easily overfit and memorize patterns.
- Increasing samples and feature diversity makes the model:
    - More stable
    - Less sensitive to noise
    - Better at generalizing unseen data
- Large datasets prevent the model from memorizing everything and force it to learn true relationships.

# ✅ Is This the Right Approach?
**Yes. Absolutely. ✔️**
You followed a solid ML learning path:
1. Start with small data → observe overfitting
2. Increase dataset size → observe stability
3. Compare training vs testing metrics
4. Draw conclusions from behavior, not just scores

This is exactly how real ML engineers learn models.

# 🚀 Next Improvements (Optional)
- Add early_stopping_rounds
- Tune max_depth, learning_rate, n_estimators
- Try even noisier datasets
- Visualize feature importance
- Compare with Linear Regression or Random Forest