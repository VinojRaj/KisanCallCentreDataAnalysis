# -*- coding: utf-8 -*-
"""

@author: Vinoj
"""

import pandas as pd

# File paths
csv_file_path = r'C:\Users\Vinoj\OneDrive\Desktop\Ashoka_PEDP\Project 1\Workfile.csv'
excel_file_path = r'C:\Users\Vinoj\OneDrive\Desktop\Ashoka_PEDP\Project 1\Yearwise\Values_Year_2021.xlsx'

# Chunk size
chunk_size = 10000

# Create an empty DataFrame to store concatenated chunks
concatenated_df = pd.DataFrame()

# Iterate through chunks
for chunk in pd.read_csv(csv_file_path, chunksize=chunk_size):
    # Filter rows where the "Year" attribute is equal to the year provided
    chunk_yearly = chunk[chunk['Year'] == 2021]
    
    # Concatenate the current chunk to the DataFrame
    concatenated_df = pd.concat([concatenated_df, chunk_yearly], ignore_index=True)

# Create Excel writer
with pd.ExcelWriter(excel_file_path, engine='xlsxwriter') as writer:
    # Write the concatenated DataFrame to two separate sheets
    concatenated_df.iloc[:len(concatenated_df)//2].to_excel(writer, sheet_name='Sheet1', index=False)
    concatenated_df.iloc[len(concatenated_df)//2:].to_excel(writer, sheet_name='Sheet2', index=False)

# The Excel file is now complete with all rows where "Year" is equal to the provided year, divided into two sheets
print(f'Data written to: {excel_file_path}')
