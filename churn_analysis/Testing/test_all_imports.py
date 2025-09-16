# test_all_imports.py

def test_imports():
    """Test that all imports work correctly"""
    
    print("Testing imports...")
    
    try:
        # Test 1: Basic import
        import churn_final
        print("Basic import works")
        
        # Test 2: Specific function import
        from churn_final import load_and_clean_data
        print("Function import works")
        
        # Test 3: Load data
        df = load_and_clean_data('Customer Churn.csv')
        print(f"Data loading works ({len(df)} records)")
        
        # Test 4: Run a simple analysis
        churn_rate = (df['Churn'] == 'Yes').mean() * 100
        print(f"Analysis works (churn rate: {churn_rate:.1f}%)")
        
        print("\n All tests passed! Your code is reusable!")
        
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    test_imports()



# quick_analysis.py
from churn_final import load_and_clean_data, generate_summary_insights

# Quick insights for a meeting
df = load_and_clean_data('Customer Churn.csv')
insights = generate_summary_insights(df)

print("KEY INSIGHTS FOR MEETING:")
print(f"• Overall churn rate: {insights['overall_churn_rate']:.1f}%")
print("• High-risk segments:")
for segment in insights['high_risk_segments']:
    print(f"  - {segment}")