# 🏦 Credit Limit Optimization System

## Project Overview

The Credit Limit Optimization System is a machine learning-based decision support system designed to help banks optimize customer credit limits based on historical financial behavior.

The system analyzes customer demographic, income, spending, and credit utilization patterns to:
- Predict optimal credit limit adjustment decisions.
- Identify high-risk and high-value customers.
- Segment customers into meaningful behavioral clusters.
- Support data-driven credit risk management.

This project simulates a real-world banking scenario using **synthetically generated financial data**.

## Business Problem

Banks must regularly adjust customer credit limits to:
- Reduce default risk.
- Improve capital efficiency.
- Increase profitability.
- Reward responsible customers.
- Control exposure to risky borrowers.

**Manual decision-making is inefficient and inconsistent.**
This system provides an automated, data-driven solution.

## 🛠️ Technologies Used
- Python
- Pandas & NumPy
- Scikit-learn
- Matplotlib & Seaborn
- K-Means Clustering
- Logistic Regression
- Cross Validation
- StandardScaler

## Dataset Description

The dataset includes financial and behavioral features such as:
- customer_id
- age
- gender
- employment_length_years
- annual_income
- income_growth_rate
- current_credit_limit
- avg_monthly_spend_6m
- credit_utilization_ratio
- revolving_balance
- payment_ratio
- min_payment_flag
- days_past_due_30_6m
- days_past_due_60_6m
- delinquencies_12m
- credit_score
- credit_score_trend_6m
- debt_to_income_ratio
- external_loans_count
- hard_inquiries_6m
- account_age_months
- interest_rate
- interest_income_6m
- interchange_income_6m
- annual_fee
- total_revenue_6m
- default_next_6m
- optimal_limit_change_pct
- limit_adjustment_decision

⚠️ Note: The dataset used in this project is **synthetically generated** for simulation purposes.

# 🧠 Supervised Learning: Credit Limit Decision Model
## Objective

Predict the optimal credit limit adjustment decision:
- 0 → **Decrease Limit**
- 1 → **No Change**
- 2 → **Increase Limit**

# Model Used
- Logistic Regression
- One-vs-Rest strategy (Multiclass classification)
- StandardScaler for feature scaling
- Train/Test split (80/20)
- 5-Fold Cross Validation

# Model Performance
- Training Accuracy: ~99.93%
- Testing Accuracy: ~99.94%
- Cross-Validation Accuracy: ~99.89%

The model shows strong generalization with no signs of overfitting.

# Evaluation Metrics
- Accuracy Score
- Classification Report (Precision, Recall, F1-score)
- Confusion Matrix
- Cross-Validation Score

# Unsupervised Learning: Customer Segmentation

To enhance business insight, K-Means clustering was applied.

## Process
- Used Elbow Method to determine optimal clusters
- Optimal K value: 4
- 2D and 3D visualization of clusters

# Machine Learning Pipeline Workflow
- Data Cleaning
- Feature Engineering
- Encoding Categorical Variables
- Feature Scaling
- Train/Test Split
- Model Training
- Evaluation
- Cross Validation
- Clustering Analysis
- Visualization

## Correlation Insights

A correlation heatmap was generated to understand relationships between financial, behavioral, and revenue variables.
**Key Observations:**

- Strong positive correlation between **revolving balance**, **credit utilization ratio**, and **interest income**, as interest revenue is directly derived from outstanding balances.
- **Interchange income** is strongly correlated with average monthly spending, reflecting transaction-driven revenue.
- **Total revenue** shows strong correlation with both interest income and interchange income, as expected from its composition.
- **Current credit** limit is positively correlated with annual income, reflecting income-based limit assignment logic.
- Default-related variables show positive correlation with high utilization and delinquency metrics.

This analysis validates internal consistency of the simulated financial model and helps identify key revenue and risk drivers.

## Customer Segmentation (Cluster Summary)
----------------------------------------------------
## K-Means Clustering Results

Customers were segmented into 4 behavioral clusters using K-Means clustering.
Cluster profiling was performed using **mean** feature values.

**Cluster Profiles:**
------------------------------------------------
**Cluster 2 – High-Value Segment**
- Highest annual income.
- Highest credit limit.
- Highest spending and revenue contribution.
- Suitable for premium card offerings and cross-selling.

**Cluster 0 – Upper-Mid Segment**
- Moderately high income and spending.
- Stable utilization.
- Potential candidates for controlled credit limit increase.

**Cluster 1 – Mid Segment**
- Medium income and spending behavior.
- Moderate revenue contribution.
- Suitable for targeted engagement strategies.

**Cluster 3 – Entry-Level Segment**
- Lowest income and credit limit.
- Lower spending capacity.
- Suitable for EMI offers and conservative risk strategies.

This segmentation enables banks to:
- Align credit limit decisions with customer risk and revenue profile.
- Identify high-value customers for premium product offerings.
- Apply risk-controlled strategies to vulnerable segments.
- Optimize portfolio profitability while managing default exposure.


------------------------------------------------------------------------
## Strategic Insights from Segmentation

Based on risk and revenue characteristics:
- High-value customers can be upgraded to premium offerings.
- Mid-segments can receive moderate credit optimization strategies.
- Lower-income segments require risk-controlled monetization strategies.
- High utilization with delinquency signals need limit tightening and monitoring.


# Business Impact

This system can help banks:
- Reduce credit default exposure.
- Optimize customer credit allocation.
- Improve portfolio profitability.
- Automate limit adjustment decisions.
- Identify risky behavioral patterns early.

# Future Improvements
- Implement SHAP for model explainability.
- Introduce class imbalance handling.
- Add real-world financial constraints.
- Deploy using Streamlit for interactive dashboard.
- Integrate real banking datasets.
- Convert into a real-time API service.

# Key Learnings
- End-to-end ML workflow implementation.
- Multiclass classification modeling.
- Model validation and overfitting detection.
- Customer segmentation using K-Means.
- Translating ML results into business insights.