# -*- coding: utf-8 -*-
"""

@author: Vinoj
"""

import pandas as pd

# File path
csv_file_path = r"C:\Users\Vinoj\OneDrive\Desktop\Ashoka_PEDP\Project 1\KCC12-22.csv"

# Chunk size
chunk_size = 100000

# Counter for unique query types
query_type_counter = {}

# Iterate through chunks
for chunk in pd.read_csv(csv_file_path, chunksize=chunk_size):
    print(f"Processing chunk {chunk.index[0] + 1}")
    
    # Count occurrences of each unique query type within the chunk
    chunk_counter = dict(chunk['Year'].astype(str).value_counts())

    # Update the overall counter with the counts from the current chunk
    for query_type, count in chunk_counter.items():
        query_type_counter[query_type] = query_type_counter.get(query_type, 0) + count

# Create a DataFrame from the results
results_df = pd.DataFrame(list(query_type_counter.items()), columns=['Year', 'TotalOccurrences'])

# Save the DataFrame to an Excel file
excel_file_path = r'C:\Users\Vinoj\OneDrive\Desktop\Ashoka_PEDP\Project 1\PythonAnalysis_output\YearlyCalls.xlsx'
results_df.to_excel(excel_file_path, index=False)

print(f"Results saved to {excel_file_path}")

