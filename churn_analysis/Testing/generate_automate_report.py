# automated_report.py
from churn_final import *
import datetime

def generate_weekly_report():
    """Generate automated weekly churn report"""
    
    # Load data
    df = load_and_clean_data('Customer Churn.csv')
    
    # Create report
    report_date = datetime.datetime.now().strftime("%Y-%m-%d")
    
    with open(f'churn_report_{report_date}.txt', 'w') as f:
        f.write(f"CHURN ANALYSIS REPORT - {report_date}\n")
        f.write("="*50 + "\n\n")
        
        # Basic stats
        f.write(f"Total customers: {len(df):,}\n")
        f.write(f"Churn rate: {(df['Churn'] == 'Yes').mean() * 100:.1f}%\n")
        
        # High-risk customers
        high_risk = df[df['Contract'] == 'Month-to-month']
        f.write(f"High-risk customers: {len(high_risk):,}\n")
    
    print(f"Report saved as churn_report_{report_date}.txt")

if __name__ == "__main__":
    generate_weekly_report()