# -*- coding: utf-8 -*-
"""

@author: Vinoj
"""

import pandas as pd

# File path
csv_file_path = r'C:\Users\Vinoj\OneDrive\Desktop\Ashoka_PEDP\Project 1\Workfile.csv'

# Chunk size
chunk_size = 10000

# Unique values set
unique_query_types_set = set()

# Iterate through chunks
for chunk in pd.read_csv(csv_file_path, chunksize=chunk_size):
    # Update the set of unique query types
    unique_query_types_set.update(chunk['QueryType'].astype(str).unique())

# Convert the set to a sorted list
unique_query_types_list = sorted(list(unique_query_types_set))

# Display the unique values
print("Unique values in 'QueryType':", unique_query_types_list)
