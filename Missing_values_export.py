# -*- coding: utf-8 -*-
"""

@author: Vinoj
"""

import pandas as pd

# Read the CSV file in chunks
csv_file_path = r'C:\Users\Vinoj\OneDrive\Desktop\Ashoka_PEDP\Project 1\Workfile.csv'  # Replace with the path to your CSV file
chunk_size = 10000  # Adjust the chunk size based on your system's capacity

missing_values_list = []

for chunk in pd.read_csv(csv_file_path, chunksize=chunk_size):
    # Find missing values in the current chunk
    missing_values_chunk = chunk[chunk.isnull().any(axis=1)]
    missing_values_list.append(missing_values_chunk)

# Concatenate all chunks into a single DataFrame
missing_values = pd.concat(missing_values_list)

# Export the missing values to an Excel file
excel_output_path = 'missing_values.xlsx'  # Replace with the desired output path
missing_values.to_excel(excel_output_path, index=False, engine='openpyxl')

print(f"Missing values exported to {excel_output_path}")
