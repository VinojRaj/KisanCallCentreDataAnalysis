# -*- coding: utf-8 -*-
"""

@author: Vinoj
"""
import pandas as pd

# File path
csv_file_path = r'C:\Users\Vinoj\OneDrive\Desktop\Ashoka_PEDP\Project 1\KCC12-22.csv'

# Chunk size
chunk_size = 1000000

# Unique values set
unique_years_set = set()

# Iterate through chunks
for chunk in pd.read_csv(csv_file_path, chunksize=chunk_size):
    print(f"Processing chunk {chunk.index[0] + 1}...")
    # Convert the "Year" column to a more memory-efficient data type
    chunk['Year'] = chunk['Year'].astype('int16')  # or 'int32' if the values are larger
    
    # Update the set of unique years
    unique_years_set.update(chunk['Year'].unique())

# Convert the set to a sorted list
unique_years_list = sorted(list(unique_years_set))

# Display the unique values
print("Unique values in 'Year':", unique_years_list)
