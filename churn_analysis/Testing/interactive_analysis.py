# interactive_analysis.py
from churn_final import *

def menu_driven_analysis():
    """Let user choose what analysis to run"""
    
    # Load data once
    print("Loading data...")
    df = load_and_clean_data('Customer Churn.csv')
    
    while True:
        print("\n" + "="*50)
        print("CHURN ANALYSIS MENU")
        print("="*50)
        print("1. Demographic Analysis")
        print("2. Service Analysis") 
        print("3. Payment Analysis")
        print("4. Full Analysis")
        print("5. Quick Summary")
        print("6. Exit")
        
        choice = input("\nEnter your choice (1-6): ")
        
        if choice == '1':
            demographic_analysis(df)
        elif choice == '2':
            service_analysis(df)
        elif choice == '3':
            payment_analysis(df)
        elif choice == '4':
            analyze_churn_patterns(df)
        elif choice == '5':
            basic_data_info(df)
        elif choice == '6':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    menu_driven_analysis()