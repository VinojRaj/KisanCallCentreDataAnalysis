# -*- coding: utf-8 -*-
"""

@author: Vinoj
"""

import pandas as pd
import math

# Read the CSV file in chunks
csv_file_path = r'C:/Users/Vinoj/OneDrive/Desktop/Ashoka_PEDP/Project 1/KCC12-22.csv'  # Replace with the path to your CSV file
chunk_size = 100000  # Adjust the chunk size based on your system's capacity
values_per_sheet = 1000000  # Adjust the number of values per sheet as needed

missing_values_list = []

for chunk in pd.read_csv(csv_file_path, chunksize=chunk_size):
    print(f"Processing chunk {chunk.index[0] + 1}...")
    # Find missing values in the current chunk
    missing_values_chunk = chunk[chunk.isnull().any(axis=1)]
    missing_values_list.append(missing_values_chunk)

# Concatenate all chunks into a single DataFrame
missing_values = pd.concat(missing_values_list)

# Get the indices and columns with missing values
missing_indices_and_columns = missing_values.apply(lambda x: x.index.tolist() + [x.name], axis=1)

# Create a DataFrame with missing indices and columns
missing_indices_and_columns_df = pd.DataFrame(missing_indices_and_columns.tolist())

# Export the missing indices and columns to a single Excel file with multiple sheets
excel_output_path = 'missing_indices_and_columns.xlsx'  # Replace with the desired output path

with pd.ExcelWriter(excel_output_path, engine='openpyxl') as writer:
    num_sheets = math.ceil(len(missing_indices_and_columns_df) / values_per_sheet)

    for i in range(num_sheets):
        start_idx = i * values_per_sheet
        end_idx = (i + 1) * values_per_sheet
        current_sheet_df = missing_indices_and_columns_df.iloc[start_idx:end_idx, :]

        # Write the current sheet to the Excel file
        current_sheet_df.to_excel(writer, sheet_name=f'Sheet_{i+1}', index=False)

        print(f"Sheet {i+1} exported to {excel_output_path} - {f'Sheet_{i+1}'}")
        print(f"Processed rows: {start_idx + 1} to {end_idx} (out of {len(missing_indices_and_columns_df)})")
        print("-" * 30)


