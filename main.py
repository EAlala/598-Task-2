#Imports
import numpy as np
import pandas as pd
import os
import matplotlib

#User choice to start Reading the File
print("Type Ready to Start the Reading of the Data file")
user_choice = input("")

if user_choice == "Ready":

    #Read and show length of file
    data = pd.read_csv(r"C:\Users\yeai2_6rsknlh\Downloads\D598 Data Set.csv") # Path to read file
    print(f"Length of Data Set is {len(data)}") #Show length of data set

#User choice to start Looking for duplicates
print("\nType Ready to Start Looking for duplicates ")
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
print("\nType Ready to Start Grouping")

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