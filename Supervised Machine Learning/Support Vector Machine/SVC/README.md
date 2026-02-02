# Iris Dataset Classification using Support Vector Machine (SVC)
## Introduction

This project demonstrates how to classify the famous Iris flower dataset using a Support Vector Classifier (SVC) from scikit-learn. The Iris dataset consists of 150 samples from three different species of Iris flowers, with four features each: sepal length, sepal width, petal length, and petal width.

The goal is to build a multiclass classification model that predicts the species of an Iris flower based on its features. The project covers:
- Data loading and inspection
- Train-test split with stratification to maintain class proportions
- Feature scaling with StandardScaler
- Training an SVC model
- Model evaluation using accuracy, classification report (precision, recall, F1-score), and confusion matrix
- Checking for overfitting or underfitting by comparing train and test performance

# Project Steps
1. Import Required Libraries

We import necessary modules for data handling, model training, scaling, and evaluation.

    from sklearn.model_selection import train_test_split
    from sklearn.svm import SVC
    from sklearn.preprocessing import StandardScaler
    from sklearn.metrics import accuracy_score, f1_score, classification_report, confusion_matrix
    from sklearn import datasets

2. Load and Inspect Dataset

The Iris dataset is loaded from sklearn.datasets. We check for missing values and view the first few rows.

    df = datasets.load_iris(as_frame=True).frame
    print(df.isnull().sum())
    print(df.head())
    print(df['target'].value_counts())


The dataset is balanced, with 50 samples in each of the 3 classes (0, 1, 2).

3. Prepare Features and Target

Split the dataset into features (X) and target labels (y).

    X = df.drop('target', axis=1)
    y = df['target']

4. Train-Test Split with Stratification

Split data into training and testing sets with a 70/30 ratio, using stratify=y to preserve class distributions in both splits.

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.3, random_state=42, stratify=y
    )

5. Feature Scaling

Scale the feature values using StandardScaler to standardize data, which is important for SVM performance.

    ss = StandardScaler()
    X_train_scaled = ss.fit_transform(X_train)
    X_test_scaled = ss.transform(X_test)

6. Train Support Vector Classifier

Train the SVC model on the scaled training data.

    svc = SVC()
    svc.fit(X_train_scaled, y_train)

7. Predict and Evaluate
Predict labels on the test set, then calculate and print:
- Accuracy score
- Classification report (precision, recall, F1-score per class)
- Confusion matrix

    y_pred = svc.predict(X_test_scaled)
    
    print(f"Accuracy Score : {accuracy_score(y_test, y_pred)}")
    print(f"Classification Report : \n{classification_report(y_test, y_pred)}")
    print(f"Confusion Matrix : \n{confusion_matrix(y_test, y_pred)}")

8. Check for Overfitting or Underfitting

Compare accuracy and F1 scores between training and test sets to identify overfitting or underfitting.

    X_train_pred = svc.predict(X_train_scaled)
    X_test_pred = svc.predict(X_test_scaled)
    
    print(f"Training Accuracy Score : {accuracy_score(y_train, X_train_pred)}")
    print(f"Testing Accuracy Score : {accuracy_score(y_test, X_test_pred)}")
    
    print(f"Training F1 Macro Score : {f1_score(y_train, X_train_pred, average='macro')}")
    print(f"Testing F1 Macro Score : {f1_score(y_test, X_test_pred, average='macro')}")
    
    print(f"Training F1 Weighted Score : {f1_score(y_train, X_train_pred, average='weighted')}")
    print(f"Testing F1 Weighted Score : {f1_score(y_test, X_test_pred, average='weighted')}")

# Results Summary
- Training Accuracy: ~97.1%
- Testing Accuracy: ~95.6%
- F1 Scores (macro and weighted) are similarly high on both train and test sets.
- The confusion matrix and classification report show good precision and recall across all three classes.
- The small gap between training and testing performance indicates the model generalizes well without significant overfitting or underfitting.

# Conclusion

This project successfully built a Support Vector Machine classifier for the multiclass Iris dataset with excellent performance metrics. Proper data splitting, scaling, and evaluation steps ensured reliable and interpretable results.