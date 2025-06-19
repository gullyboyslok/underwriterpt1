# 3/5/2025 Shlok Jaiswal in databricks notebook
# dataset created by nikhil1e9 on Kaggle @ https://www.kaggle.com/datasets/nikhil1e9/loan-default

from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import pandas as pd

# load from the databricks thing
df = spark.sql("SELECT * FROM `workspace`.`default`.`loan_default`").toPandas()

# input/target
input_cols = ["Age", "Income", "LoanAmount", "CreditScore", "MonthsEmployed", "InterestRate", "Education", "EmploymentType"]
target_col = "Default"

# feature engineering
df['Income_to_LoanRatio'] = df['Income'] / (df['LoanAmount'] + 1)
df['CreditScore_to_InterestRate'] = df['CreditScore'] / (df['InterestRate'] + 1)

# add feature engineered features (ik this is extra code, i was to lazy to fix it </3)
input_cols.extend(['Income_to_LoanRatio', 'CreditScore_to_InterestRate'])

# cat/num
categorical_cols = ['Education', 'EmploymentType']
numerical_cols = [col for col in input_cols if col not in categorical_cols]

# preprocessor
preprocessor = ColumnTransformer(
    transformers=[
        ('num', SimpleImputer(strategy='mean'), numerical_cols),
        ('cat', Pipeline([
            ('imputer', SimpleImputer(strategy='most_frequent')),
            ('onehot', OneHotEncoder(handle_unknown='ignore'))
        ]), categorical_cols)
    ]
)

# pipeline
model_pipeline = Pipeline(steps=[
    ('preprocessor', preprocessor),
    ('classifier', RandomForestClassifier())
])

# X/y
X = df[input_cols]
y = df[target_col]

# tts
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1)

# fit+predict
model_pipeline.fit(X_train, y_train)
y_pred = model_pipeline.predict(X_test)

# accuracy
accuracy = accuracy_score(y_test, y_pred)
accuracy
