# my_analysis_tools.py
import churn_final as cf

def quick_churn_report(file_path):
    """Get a quick churn report"""
    df = cf.load_and_clean_data(file_path)
    
    total_customers = len(df)
    churn_rate = (df['Churn'] == 'Yes').mean() * 100
    
    print(f"QUICK REPORT for {file_path}")
    print(f"Total Customers: {total_customers:,}")
    print(f"Churn Rate: {churn_rate:.1f}%")
    
    return df

def find_high_risk_customers(df):
    """Find customers likely to churn"""
    high_risk = df[
        (df['Contract'] == 'Month-to-month') &
        (df['tenure'] < 12)
    ]
    
    print(f"Found {len(high_risk)} high-risk customers")
    return high_risk

# Usage
if __name__ == "__main__":
    df = quick_churn_report('Customer Churn.csv')
    high_risk = find_high_risk_customers(df)