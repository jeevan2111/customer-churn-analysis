# test_import.py
from churn_final import load_and_clean_data

# Test importing your function
df = load_and_clean_data('Customer Churn.csv')
print(f"Successfully loaded {len(df)} records!")
print(f"Columns: {list(df.columns)}")


# my_custom_analysis.py
from churn_final import (
    load_and_clean_data, 
    demographic_analysis, 
    payment_analysis
)

# Load data once
df = load_and_clean_data('Customer Churn.csv')

# Run only the analyses you want
print("Running demographic analysis...")
demographic_analysis(df)

print("Running payment analysis...")
payment_analysis(df)

print("Custom analysis complete!")