# -*- coding: utf-8 -*-
"""

@author: Vinoj
"""
import pandas as pd

# Set the chunk size
chunk_size = 100000  # Adjust based on your system's capacity

# Read the CSV file in chunks
csv_file_path = r'C:/Users/Vinoj/OneDrive/Desktop/Ashoka_PEDP/Project 1/KCC12-22.csv'  # Replace with the path to your CSV file
output_excel_path = r'C:\Users\Vinoj\OneDrive\Desktop\Ashoka_PEDP\Project 1\MissingValues_Output.xlsx'  # Replace with the desired output path

missing_values_list = []

for chunk in pd.read_csv(csv_file_path, chunksize=chunk_size):
    print(f"Processing chunk {chunk.index[0] + 1}...")
    # Find rows with missing values in 'QueryType' and 'QueryText'
    missing_values_chunk = chunk[chunk[['QueryType', 'QueryText']].isnull().all(axis=1)]
    missing_values_list.append(missing_values_chunk)

# Concatenate all chunks into a single DataFrame
missing_values = pd.concat(missing_values_list)

# Export to Excel
missing_values.to_excel(output_excel_path, index=False)

print(f"Total number of rows with missing values for both 'QueryType' and 'QueryText': {len(missing_values)}")
print(f"Data exported to {output_excel_path}")

