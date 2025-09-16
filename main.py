#Imports
import numpy as np
import pandas as pd
import os
import matplotlib

#User choice to start reading the file
print("Type Ready to Start the Reading of the Data file")
user_choice = input("")

if user_choice == "Ready":

    #Read and show length of file
    data = pd.read_csv(r"C:\Users\yeai2_6rsknlh\Downloads\D598 Data Set.csv") # Path to read file
    print(f"Length of Data Set is {len(data)}") #Show length of data set

#User choice to start Looking for duplicates
print("Type Ready to Start Looking for duplicates ")
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
print("Type Ready to Start Grouping")

user_choice = input("")

if user_choice == "Ready":

    # Group by State and Get Stats
    num_col = data.select_dtypes(include = 'number').columns #Looks for columns with number as values for calulation
    state_stats = data.groupby("Business State")[num_col].agg(["mean", "median", "min","max"]) # Group by Business State and show states
    print(state_stats.head())