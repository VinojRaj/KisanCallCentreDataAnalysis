# -*- coding: utf-8 -*-
"""

@author: Vinoj
"""

import pandas as pd

# Replace with the path to your CSV file
csv_file_path = r'C:/Users/Vinoj/OneDrive/Desktop/Ashoka_PEDP/Project 1/KCC12-22.csv'

# Set the chunk size
chunk_size = 1000000

# Specify the data types for columns (adjust as needed)
dtype_dict = {'Year': int, 'Month': int, 'Crop': str, 'DistrictName': str, 'QueryType': str, 'StateName': str, 'QueryText': str}

# Initialize a dictionary to store the count of unique values for each column
unique_values_count_per_column = {col: 0 for col in dtype_dict}

# Read the CSV file in chunks and update unique values count
for chunk in pd.read_csv(csv_file_path, dtype=dtype_dict, chunksize=chunk_size):
    print(f"Processing chunk {chunk.index[0] + 1}...")
    for col in unique_values_count_per_column:
        unique_values_count_per_column[col] += chunk[col].nunique()

# Print the total number of unique values for each column
for col, count in unique_values_count_per_column.items():
    print(f"Total unique values in column '{col}': {count}")
