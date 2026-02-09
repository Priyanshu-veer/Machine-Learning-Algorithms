# XGBoost Binary Classification

This repository demonstrates a simple binary classification XGBoost and scikit-learn on a synthetic dataset.

## The project covers:
- Generating a dataset with make_classification
- Splitting data into training and testing sets
- Training an XGBClassifier
- Evaluating model performance using accuracy

# 📦 Requirements

Make sure you have the following installed:

    pip install xgboost scikit-learn numpy

# 📊 Dataset

The dataset is synthetically generated using `*sklearn.datasets.make_classification*` with the following parameters:
- Samples: 20,000
- Features: 40
- Informative features: 20
- Redundant features: 2
- Classes: 2 (binary classification)
- Random state: 42

This setup is useful for testing and benchmarking classification models.

# 🧠 Model

The model used is XGBoost’s XGBClassifier with these key hyperparameters:
- max_depth = 5
- learning_rate = 0.2
- eval_metric = "logloss"
- random_state = 42

The data is split as:
- 80% training
- 20% testing

# 🚀 How to Run

Clone the repository and run the script or notebook:

    git clone https://github.com/your-username/your-repo-name.git
    cd your-repo-name

Then execute the Python file or open the notebook and run all cells.

# 📈 Results

Model performance based on accuracy:
- Training Accuracy: 0.98375
- Testing Accuracy: 0.9505

This indicates strong performance with minimal overfitting.

# 📝 Notes
- The dataset is synthetic and intended for demonstration and experimentation.
- Hyperparameters can be tuned further to explore bias–variance tradeoffs.
- Accuracy is used as the evaluation metric, but others (precision, recall, F1-score) can easily be added.