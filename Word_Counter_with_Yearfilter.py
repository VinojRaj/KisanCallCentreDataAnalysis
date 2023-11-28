# -*- coding: utf-8 -*-
"""

@author: Vinoj
"""

import pandas as pd

# File path
csv_file_path = r'C:\Users\Vinoj\OneDrive\Desktop\Ashoka_PEDP\Project 1\Workfile.csv'

# Chunk size
chunk_size = 10000

# Targeted year
target_year = 2012

# Specific phrase to search for in 'QueryText'
specific_phrase = 'Blast'

# Counter for the number of occurrences
phrase_count = 0

# Iterate through chunks
for chunk in pd.read_csv(csv_file_path, chunksize=chunk_size):
    # Filter rows for the targeted year within the chunk
    year_filtered_chunk = chunk[chunk['Year'] == target_year]

    # Count occurrences of the specific phrase in 'QueryText' within the chunk
    phrase_count += year_filtered_chunk['QueryText'].str.contains(specific_phrase, case=False, na=False).sum()

# Display the count of occurrences
print(f"The phrase '{specific_phrase}' occurred {phrase_count} times in the 'QueryText' for the year {target_year}.")
