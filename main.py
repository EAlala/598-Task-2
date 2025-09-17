#Imports
import numpy as np
import pandas as pd
import os
import matplotlib.pyplot as plt

#User choice to start Reading the File
print("Type Ready to Start the Reading of the Data file")
user_choice = input("")

if user_choice == "Ready":

    #Read and show length of file
    data = pd.read_csv(r"C:\Users\yeai2_6rsknlh\Downloads\D598 Data Set.csv") # Path to read file
    print(f"Length of Data Set is {len(data)}") #Show length of data set

#User choice to start Looking for Duplicates
print("\nType Ready to Start Looking for Duplicates ")
user_choice = input("")

if user_choice == "Ready":

    #Look for duplicates
    dup_rows = data.duplicated().sum() #Checks for duplicates in rows and adds them
    dup_id = data["Business ID"].duplicated().sum() #Check for duplicates in Business ID column and adds them

    #If statment for duplicates
    if dup_rows > 0: #If sum of duplicate rows is greather than 0
        print(f"There are duplicate rows {dup_rows}")
    elif dup_id > 0: #If sum of duplicate ID's is greather than 0
        print(f"There are duplicate ID's {dup_id}")
    else: #If both sums are 0 then there is no duplicates
        print("There are no duplicate rows or ID's")

#User choice to start Grouping
print("\nType Ready to Start Grouping")

user_choice = input("")

if user_choice == "Ready":

    # Group by State and Get Stats
    num_col = data.select_dtypes(include = 'number').columns #Looks for columns with number as values for calulation
    state_stats = data.groupby("Business State")[num_col].agg(["mean", "median", "min","max"]) # Group by Business State and show states
    print(state_stats.head()) # Show first 5 rows

#User choice to start Filtering Negative Debt
print("\nType Ready to Start Filtering Negative Debt")

user_choice = input("")

if user_choice == "Ready":

    # Check to see if Debt to Equity is less than zero fro debt
    negative_data = data[data["Debt to Equity"] < 0] 

    #If statment for negative Debt-to-Equity ratios
    if len(negative_data) > 0:
        print(f"There is {len(negative_data)} companies with debt negative Debt-to-Equity ratios")
        print(negative_data[['Business ID', 'Business State', 'Debt to Equity']].to_string(index=False)) #Selects columns with negative debt and formats for printing
    else:
        print("No companies with with debt negative Debt-to-Equity ratios")

#User choice to start Calculating New Ratio
print("\nType Ready to Calculate New Ratio")

user_choice = input("")

if user_choice == "Ready":

    # Calculate New ratio from every business
    debt_to_income_ratio = np.where(
    data['Total Revenue'] != 0,  # Check: Is Revenue NOT zero?
    data['Total Long-term Debt'] / data['Total Revenue'],  # If yes, calculate normally.
    np.nan  # If no (Revenue is zero), assign NaN (Not a Number) instead of crashing.
    )
    print("All New Ratios Complete")

#User choice to Create New DataFrame for New Ratios
print("\nType Ready to Create New DataFrame for New Ratios")

user_choice = input("")

if user_choice == "Ready":

    # Create new dataframe for new ratios
    debt_to_income_data = pd.DataFrame({
        "Business ID": data["Business ID"], # Column for Business ID
        "Debt to Income Ratio": debt_to_income_ratio # Column for debt to incom ratio
        })
    
    print (debt_to_income_data.head())

#User choice to Add New Column to Excel Copy and Save the Excel Copy
print("\nType Ready to Add New Column to Excel Copy and Save the Excel Copy")

user_choice = input("")

if user_choice == "Ready":

    # Add the new column to the original data
    final_data = data.copy() # Make a copy of the excel
    final_data['Debt to Income Ratio'] = debt_to_income_ratio # Add new column to copy

    # Save to a Excel copy file 
    final_data.to_csv("Excel Copy.csv", index = False)

# Sources Used
"""
Python Software Foundation. (2023). Python Language Reference (Version 3.12) [Computer software]. Retrieved from https://docs.python.org/3/reference/

"""

#User choice to See High-Risk Companies (Negative Equity) Chart
print("\nType Ready to See High-Risk Companies (Negative Equity) Chart")

user_choice = input("")

if user_choice == "Ready":

    # Visualizations 
    # Chart: High-Risk Companies (Negative Equity)
    plt.figure(figsize=(10, 4))
    negative_data = data[data['Debt to Equity'] < 0]
    plt.bar(negative_data['Business State'], negative_data['Debt to Equity'], color='red')
    plt.title('High-Risk Companies: Negative Debt-to-Equity')
    plt.xlabel('State')
    plt.ylabel('Debt-to-Equity Ratio')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

#User choice to See Profitability by State Chart
print("\nType Ready to See Profitability by State Chart")

user_choice = input("")

if user_choice == "Ready":

    # Chart: Profitability by State
    plt.figure(figsize=(10, 4))
    profit_by_state = data.groupby('Business State')['Profit Margin'].mean().sort_values(ascending=False)
    profit_by_state.plot(kind='bar', color='green')
    plt.title('Average Profit Margin by State')
    plt.xlabel('State')
    plt.ylabel('Average Profit Margin')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

#User choice to See Debt-to-Income Distributione Chart
print("\nType Ready to See Debt-to-Income Distribution Chart")

user_choice = input("")

if user_choice == "Ready":

    # Chart: Debt-to-Income Distribution
    plt.figure(figsize=(10, 4))
    plt.hist(debt_to_income_ratio, bins=20, color='orange', alpha=0.7)
    plt.title('Distribution of Debt-to-Income Ratios')
    plt.xlabel('Debt-to-Income Ratio')
    plt.ylabel('Number of Companies')
    plt.axvline(np.median(debt_to_income_ratio), color='red', linestyle='--', label='median')
    plt.legend()
    plt.tight_layout()
    plt.show()

#User choice to See Revenue vs. Debte Chart
print("\nType Ready to See Revenue vs. Debt Chart")

user_choice = input("")

if user_choice == "Ready":

    # Chart: Revenue vs. Debt
    plt.figure(figsize=(10, 4))
    plt.scatter(data['Total Revenue'], data['Total Long-term Debt'], alpha=0.5)
    plt.title('Revenue vs. Long-term Debt')
    plt.xlabel('Total Revenue')
    plt.ylabel('Total Long-term Debt')
    plt.tight_layout()
    plt.show()