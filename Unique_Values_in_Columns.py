# -*- coding: utf-8 -*-
"""

@author: Vinoj
"""
import pandas as pd

# Replace with the path to your CSV file
csv_file_path = r'C:/Users/Vinoj/OneDrive/Desktop/Ashoka_PEDP/Project 1/KCC12-22.csv'

# Set the chunk size
chunk_size = 1000000

# Specify the data type for the 'Year' column
dtype_dict = {'QueryType': str}

# Initialize a set to store unique values of the 'Year' column
unique_years = set()

# Read the CSV file in chunks and update unique values
for chunk in pd.read_csv(csv_file_path, usecols=['QueryType'], dtype=dtype_dict, chunksize=chunk_size):
    print(f"Processing chunk {chunk.index[0] + 1}...")
    unique_years.update(chunk['QueryType'].unique())

# Print the unique values of the 'Year' column
print("Unique values in the 'QueryType' column:")
print(sorted(unique_years))