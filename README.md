# underwriterpt1
check if someone will default on their loan (reuploaded, originally made in databricks on 3/5/2025)
i mainly made this project to test out the databricks notebook and also to work on a simple underwriter test for Credix (https://github.com/credix-lucrum/Credix_main) so that's why it's so simple and it doesn't have any complicated elements like hyperparameters, better feature engineering, under-/over-fitting checks, etc

# specs
inputs: "Age", "Income", "LoanAmount", "CreditScore", "MonthsEmployed", "InterestRate", "Education", "EmploymentType"
      + "Income_to_LoanRatio", "CreditScore_to_InterestRate"
outputs/targets: "Default"

# stats
88.63% accuracy
724 ms runtime
255,347 rows or 7.56 MB read
0B written
