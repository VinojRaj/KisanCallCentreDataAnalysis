# -*- coding: utf-8 -*-
"""

@author: Vinoj
"""

import pandas as pd

# File path
csv_file_path = r'C:\Users\Vinoj\OneDrive\Desktop\Ashoka_PEDP\Project 1\Workfile.csv'

# Chunk size
chunk_size = 10000

# Container for sample data for each target query type
sample_data_dict = {}

# Numeric query types for which to retrieve 10 rows of data
target_query_types = [0, 1, 10, 100, 102, 11, 12, 15, 16, 17, 18, 19, 2, 20, 21, 22, 26, 27, 29, 3, 31, 32, 33, 34, 36, 37, 38, 39, 40, 43, 44, 45, 46, 47, 48, 49, 5, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 6, 60, 61, 74, 75, 76, 78, 8, 83, 84, 85, 87, 88, 89, 9, 90, 91, 92, 93, 94, 95, 99, 9999]

# Iterate through chunks
for chunk in pd.read_csv(csv_file_path, chunksize=chunk_size):
    # Check if the current query type is in the list of target query types
    filtered_chunk = chunk[chunk['QueryType'].astype(str).isin(map(str, target_query_types))]

    # Retrieve 10 rows of data for each target query type
    for query_type in target_query_types:
        sample_data = filtered_chunk[filtered_chunk['QueryType'].astype(str) == str(query_type)].head(50)
        if not sample_data.empty:
            if query_type not in sample_data_dict:
                sample_data_dict[query_type] = sample_data

# Save the sample data for each target query type to separate sheets in an Excel file
excel_file_path = r'C:\Users\Vinoj\OneDrive\Desktop\Ashoka_PEDP\Project 1\SampleDataByQueryType.xlsx'
with pd.ExcelWriter(excel_file_path, engine='xlsxwriter') as writer:
    for query_type, sample_data in sample_data_dict.items():
        sample_data.to_excel(writer, sheet_name=f'SampleData_{query_type}', index=False)

print(f"Sample data saved to {excel_file_path}")
