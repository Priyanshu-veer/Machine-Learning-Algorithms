# Loan Approval System (Machine Learning)

An intelligent loan approval system that predicts whether a customer should be approved or rejected based on financial and demographic features. The model is optimized to reduce financial risk while minimizing rejection of eligible customers.

# Problem Statement
A mid-sized financial company named ApnaSapna Bank offers personal and home loans to customers across urban and rural regions of India. Every day, hundreds of customers apply for loans through online and branch applications.

Until now, ApnaSapna Bank has been using a manual verification process where loan officers evaluate applications by checking income proofs, employment details, credit history, and other documents. This process is time-consuming, biased & inconsistent.

As a result, the bank faces two major challenges:
1. Good customers sometimes get rejected, leading to loss of business.
2. High-risk customers sometimes get approved, leading to financial losses.

To solve this problem, the bank wants to introduce an system intelligent loan approval powered by Machine Learning that can automatically analyse applicant details and predict whether a loan should be Approved or Rejected human verification.

You are hired as a Machine Learning Engineer before final to design and develop this intelligent system using historical loan application data. The system must learn hidden patterns from previous customer records and provide accurate, fast, and unbiased loan approval decisions.


# Dataset Overview

|Column                  |   Description
| ---------------------- | ---------------------------------------
|Applicant_ID            |   Unique applicant ID
|Applicant_Income        |   Monthly income of applicant
|Coapplicant_Income      |   Monthly income of co-applicant
|Employment_Status       |   Salaried / Self-Employed / Business
|Age                     |   Applicant age
|Marital_Status          |   Married / Single
|Dependents              |   Number of dependents
|Credit_Score            |   Credit bureau score
|Existing_Loans          |   Number of already running loans
|DTI_Ratio               |   Debt-to-Income ratio
|Savings                 |   Savings balance
|Collateral_Value        |   Value of collateral provided
|Loan_Amount             |   Loan amount requested
|Loan_Term               |   Loan duration (months)
|Loan_Purpose            |   Home / Education / Personal / Business
|Property_Area           |   Urban / Semi-Urban / Rural
|Education_Level         |   Graduate / Postgraduate / Undergraduate
|Gender                  |   Male / Female
|Employer_Category       |   Govt / Private / Self
|Loan_Approved           |   (Target) 1 = Approved, 0 = Rejected

## Number of samples
    rows    ---> 1000
    columns ---> 20

**Class distribution** 
>**(70:30 imbalance)***

# Project Workflow
1. Data Collection
- Gathered loan applicant dataset.
- Identified target variable (`Loan_Approved`).

2. Data Preprocessing
- Handled missing values using appropriate imputation techniques.
- Cleaned inconsistent or irrelevant data.
- Performed feature encoding:
- Label Encoding (for ordinal features)
- One-Hot Encoding (for nominal features)

3. Exploratory Data Analysis (EDA)
- Analyzed class imbalance (70:30 ratio).
- Studied feature relationships with loan approval.
- Identified important patterns affecting approval decisions.

4. Feature Engineering
- Created meaningful features to improve predictive power.
- Removed redundant or low-importance variables.

5. Data Splitting
- Applied `train_test_split` with `stratify=y` to preserve class distribution.

6. Feature Scaling
- Applied scaling to numerical features where required.

7. Model Training & Comparison
Trained multiple models for performance comparison:
- Logistic Regression
- Decision Tree Classifier
- Support Vector Classifier (SVC)
- XGBoost Classifier

8. Model Evaluation
Evaluated models using:
- Accuracy
- Precision
- Recall
- F1-Score
- Confusion Matrix
- Classification Report

Special focus was given to Recall and F1-score for the minority class due to business risk sensitivity.

9. Handling Class Imbalance
- Applied SMOTE (Synthetic Minority Oversampling Technique) on the training data.
- Significantly reduced false negatives (risky customers incorrectly approved).
- Improved minority class F1-score from ~0.21 to ~0.84.

# Model Comparison

| Models                    | Accuracy  | Precision  | Recall  | F1 score  |Training Accuracy  | Testing Accuracy  
|---------------------------|-----------|------------|---------|---------- |-------------------| ------------------
| Logistic Regression       |   80.5    |    64.7    |  76.6   |   70.2    |       88.5        |       80.5
| Decision Tree Classifier  |   87      |    70.2    |  98.3   |   81.9    |       91.2        |       87
| Support Vector Classifier |   82      |    68.1    |  75     |   71.4    |       95.7        |       82
| XGBoost CLassifier        |   88      |    76      |  90     |   82.4    |       99.8        |       88.5
| XGBoost Classifier(SMOTE) |   89      |    76.7    |  93     |   84.2    |       100         |       89


After comparing multiple classification models, **XGBoost** with `SMOTE` was selected as the final model due to its superior **F1-score** and strong **recall** for high-risk applicants. While **Decision Tree** achieved the highest **recall**, **XGBoost** with `SMOTE` provided a better balance between **precision** and **recall**, reducing both financial risk and unnecessary rejection of eligible customers.


# CONCLUSION

This project successfully developed a machine learning-based Loan Approval System that addresses real-world financial risk challenges.

Since the dataset was imbalanced (70:30 ratio), relying solely on accuracy was not sufficient. Special focus was given to improving recall and F1-score for the minority class (high-risk applicants) to minimize financial losses caused by approving risky customers.

Multiple models were evaluated, including `Logistic Regression`, `Decision Tree`, `SVC`, and `XGBoost`. Among them, **XGBoost** with `SMOTE` provided the best overall performance, achieving:

**- Accuracy: 89%**

**- Recall (High-Risk Class): 93%**

**- F1-Score: 84%**

**- Significant reduction in false negatives (risky approvals)**

While the **Decision Tree Classifier** achieved slightly higher recall, **XGBoost** with **SMOTE** offered a better **balance** between precision and recall, making it more suitable for real-world deployment.

This project demonstrates:
- Effective handling of imbalanced datasets
- Risk-sensitive model evaluation
- Proper overfitting analysis
- Business-oriented decision making in model selection

The final model successfully reduces financial risk while maintaining fair approval decisions for eligible customers.
