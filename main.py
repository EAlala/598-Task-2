#Imports
import numpy as np
import pandas as pd
import os
import matplotlib

#Read and show length of file
data = pd.read_csv(r"C:\Users\yeai2_6rsknlh\Downloads\D598 Data Set.csv") # Path to read file
print("File Read")
print(f"Length of Data Set is {len(data)}") #Show length of data set

#Look for duplicates
dup_rows = data