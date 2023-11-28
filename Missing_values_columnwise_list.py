# -*- coding: utf-8 -*-
"""

@author: Vinoj
"""

import pandas as pd

# Set the chunk size
chunk_size = 100000  # Adjust based on your system's capacity

# Read the CSV file in chunks
csv_file_path = r'C:/Users/Vinoj/OneDrive/Desktop/Ashoka_PEDP/Project 1/KCC12-22.csv'  # Replace with the path to your CSV file
missing_values_list = []

for chunk in pd.read_csv(csv_file_path, chunksize=chunk_size):
    print(f"Processing chunk {chunk.index[0] + 1}...")
    # Find missing values in the current chunk
    missing_values_chunk = chunk[chunk.isnull().any(axis=1)]
    missing_values_list.append(missing_values_chunk)

# Concatenate all chunks into a single DataFrame
missing_values = pd.concat(missing_values_list)

# Get the names of columns with missing values and the number of missing values
columns_with_missing_values = missing_values.isnull().sum().reset_index()
columns_with_missing_values.columns = ['Column', 'MissingValues']

# Print the names of columns with missing values and the number of missing values
print("Columns with Missing Values and Number of Missing Values:")
for index, row in columns_with_missing_values.iterrows():
    print(f"{row['Column']}: {row['MissingValues']} missing values")
