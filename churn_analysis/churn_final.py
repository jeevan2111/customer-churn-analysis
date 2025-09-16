
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os
import sys


def load_and_clean_data(file_path='Customer Churn.csv'):
    try:
        # Load data
        print(f"Loading data from {file_path}...")
        df = pd.read_csv(file_path)
        print(f"Data loaded successfully. Shape: {df.shape}")
        
        # Clean TotalCharges column
        df["TotalCharges"] = df["TotalCharges"].replace(" ", "0")
        df["TotalCharges"] = df["TotalCharges"].astype("float")
        
        # Convert SeniorCitizen to readable format
        df['SeniorCitizen'] = df["SeniorCitizen"].apply(lambda x: "yes" if x == 1 else "no")
        
        # Check for duplicates
        duplicates = df["customerID"].duplicated().sum()
        if duplicates > 0:
            print(f"Warning: Found {duplicates} duplicate customer IDs")
        
        print("Data cleaning completed successfully!")
        return df
        
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found!")
        sys.exit(1)
    except Exception as e:
        print(f"Error loading data: {str(e)}")
        sys.exit(1)


def basic_data_info(df):
    """Display basic information about the dataset."""
    print("\n" + "="*50)
    print("DATASET OVERVIEW")
    print("="*50)
    
    print(f"Dataset shape: {df.shape}")
    print(f"Missing values: {df.isnull().sum().sum()}")
    
    # Churn rate
    churn_rate = (df['Churn'] == 'Yes').mean() * 100
    print(f"Overall churn rate: {churn_rate:.2f}%")
    
    return churn_rate


def churn_overview_analysis(df):
    
    """Create overview visualizations of churn patterns."""
    print("\n" + "="*50)
    print("CHURN OVERVIEW ANALYSIS")
    print("="*50)
    
    # Count plot
    plt.figure(figsize=(12, 5))
    
    plt.subplot(1, 2, 1)
    ax = sns.countplot(data=df, x='Churn')
    ax.bar_label(ax.containers[0])
    plt.title("Count of Customers by Churn Status")
    
    # Percentage pie chart
    plt.subplot(1, 2, 2)
    churn_counts = df['Churn'].value_counts()
    plt.pie(churn_counts, labels=churn_counts.index, autopct="%1.2f%%")
    plt.title("Percentage of Churned Customers")
    
    plt.tight_layout()
    plt.show()


def demographic_analysis(df):
    """Analyze churn patterns by demographic factors."""
    print("\n" + "="*50)
    print("DEMOGRAPHIC ANALYSIS")
    print("="*50)
    
    # Gender analysis
    plt.figure(figsize=(15, 5))
    
    plt.subplot(1, 3, 1)
    ax = sns.countplot(data=df, x="gender", hue="Churn")
    ax.bar_label(ax.containers[0])
    ax.bar_label(ax.containers[1])
    plt.title("Churn by Gender")
    
    # Senior Citizen analysis
    plt.subplot(1, 3, 2)
    ax = sns.countplot(data=df, x="SeniorCitizen")
    ax.bar_label(ax.containers[0])
    plt.title("Count by Senior Citizen Status")
    
    plt.subplot(1, 3, 3)
    # Senior citizen churn percentage
    senior_churn = pd.crosstab(df['SeniorCitizen'], df['Churn'], normalize='index') * 100
    senior_churn.plot(kind='bar', ax=plt.gca(), color=['#1f77b4', '#ff7f0e'])
    plt.title('Churn Rate by Senior Citizen Status')
    plt.xlabel('Senior Citizen')
    plt.ylabel('Percentage (%)')
    plt.xticks(rotation=0)
    plt.legend(title='Churn')
    
    plt.tight_layout()
    plt.show()
    
    # Print insights
    print("Key Demographics Insights:")
    gender_churn = df.groupby('gender')['Churn'].apply(lambda x: (x == 'Yes').mean() * 100)
    print(f"- Female churn rate: {gender_churn['Female']:.1f}%")
    print(f"- Male churn rate: {gender_churn['Male']:.1f}%")
    
    senior_churn_rate = df.groupby('SeniorCitizen')['Churn'].apply(lambda x: (x == 'Yes').mean() * 100)
    print(f"- Senior citizens churn rate: {senior_churn_rate['yes']:.1f}%")
    print(f"- Non-senior citizens churn rate: {senior_churn_rate['no']:.1f}%")


def tenure_contract_analysis(df):
    """Analyze churn patterns by tenure and contract type."""
    print("\n" + "="*50)
    print("TENURE & CONTRACT ANALYSIS")
    print("="*50)
    
    plt.figure(figsize=(15, 5))
    
    # Tenure analysis
    plt.subplot(1, 2, 1)
    sns.histplot(data=df, x="tenure", bins=30, hue="Churn", alpha=0.7)
    plt.title("Churn Distribution by Tenure (months)")
    
    # Contract analysis
    plt.subplot(1, 2, 2)
    ax = sns.countplot(data=df, x="Contract", hue="Churn")
    ax.bar_label(ax.containers[0])
    ax.bar_label(ax.containers[1])
    plt.title("Churn by Contract Type")
    plt.xticks(rotation=45)
    
    plt.tight_layout()
    plt.show()
    
    # Print insights
    print("Key Tenure & Contract Insights:")
    contract_churn = df.groupby('Contract')['Churn'].apply(lambda x: (x == 'Yes').mean() * 100)
    for contract, rate in contract_churn.items():
        print(f"- {contract} contract churn rate: {rate:.1f}%")


def service_analysis(df):
    """Analyze churn patterns by various services."""
    print("\n" + "="*50)
    print("SERVICE ANALYSIS")
    print("="*50)
    
    service_columns = ['PhoneService', 'MultipleLines', 'InternetService', 
                      'OnlineSecurity', 'OnlineBackup', 'DeviceProtection', 
                      'TechSupport', 'StreamingTV', 'StreamingMovies']
    
    # Create subplots
    n_cols = 3
    n_rows = (len(service_columns) + n_cols - 1) // n_cols
    
    fig, axes = plt.subplots(n_rows, n_cols, figsize=(18, n_rows * 4))
    axes = axes.flatten()
    
    for i, col in enumerate(service_columns):
        sns.countplot(data=df, x=col, hue="Churn", ax=axes[i])
        axes[i].set_title(f'Churn by {col}')
        axes[i].tick_params(axis='x', rotation=45)
    
    # Remove empty subplots
    for j in range(len(service_columns), len(axes)):
        fig.delaxes(axes[j])
    
    plt.tight_layout()
    plt.show()
    
    # Print service insights
    print("Key Service Insights:")
    for service in ['InternetService', 'OnlineSecurity', 'TechSupport']:
        service_churn = df.groupby(service)['Churn'].apply(lambda x: (x == 'Yes').mean() * 100)
        print(f"\n{service} churn rates:")
        for category, rate in service_churn.items():
            print(f"  - {category}: {rate:.1f}%")


def payment_analysis(df):
    """Analyze churn patterns by payment method."""
    print("\n" + "="*50)
    print("PAYMENT METHOD ANALYSIS")
    print("="*50)
    
    plt.figure(figsize=(10, 6))
    ax = sns.countplot(data=df, x="PaymentMethod", hue="Churn")
    ax.bar_label(ax.containers[0])
    ax.bar_label(ax.containers[1])
    plt.title("Churn by Payment Method")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
    
    # Print payment insights
    print("Key Payment Method Insights:")
    payment_churn = df.groupby('PaymentMethod')['Churn'].apply(lambda x: (x == 'Yes').mean() * 100)
    for method, rate in payment_churn.items():
        print(f"- {method}: {rate:.1f}% churn rate")


def generate_summary_insights(df):
    """Generate comprehensive summary of key insights."""
    insights = {}
    
    # Overall churn rate
    insights['overall_churn_rate'] = (df['Churn'] == 'Yes').mean() * 100
    
    # High-risk segments
    high_risk = []
    
    # Senior citizens
    senior_churn = df[df['SeniorCitizen'] == 'yes']['Churn'].apply(lambda x: x == 'Yes').mean() * 100
    if senior_churn > 30:
        high_risk.append(f"Senior Citizens ({senior_churn:.1f}%)")
    
    # Month-to-month contracts
    monthly_churn = df[df['Contract'] == 'Month-to-month']['Churn'].apply(lambda x: x == 'Yes').mean() * 100
    if monthly_churn > 30:
        high_risk.append(f"Month-to-month contracts ({monthly_churn:.1f}%)")
    
    # Electronic check payments
    echeck_churn = df[df['PaymentMethod'] == 'Electronic check']['Churn'].apply(lambda x: x == 'Yes').mean() * 100
    if echeck_churn > 30:
        high_risk.append(f"Electronic check payments ({echeck_churn:.1f}%)")
    
    insights['high_risk_segments'] = high_risk
    
    print("\n" + "="*50)
    print("EXECUTIVE SUMMARY")
    print("="*50)
    print(f"Overall churn rate: {insights['overall_churn_rate']:.2f}%")
    print("\nHigh-risk customer segments:")
    for segment in high_risk:
        print(f"  • {segment}")
    
    print("\nKey Recommendations:")
    print("  • Focus retention efforts on month-to-month customers")
    print("  • Provide additional support for senior citizens")
    print("  • Encourage alternative payment methods over electronic checks")
    print("  • Improve fiber optic service quality and support")
    print("  • Promote add-on services (online security, tech support)")
    
    return insights


def analyze_churn_patterns(df):
    """Run complete churn analysis pipeline."""
    # Set up plotting style
    plt.style.use('default')
    sns.set_palette("husl")
    
    # Run all analyses
    basic_data_info(df)
    churn_overview_analysis(df)
    demographic_analysis(df)
    tenure_contract_analysis(df)
    service_analysis(df)
    payment_analysis(df)
    insights = generate_summary_insights(df)
    
    return insights


def main():
    """
    Main function to run the complete analysis.
    """
    print("Customer Churn Analysis Starting...")
    print("="*50)
    
    # Load and clean data
    df = load_and_clean_data('Customer Churn.csv')
    
    # Run analysis
    insights = analyze_churn_patterns(df)
    
    print("\n" + "="*50)
    print("Analysis Complete!")
    print("="*50)
    
    return df, insights


if __name__ == "__main__":
    df, insights = main()