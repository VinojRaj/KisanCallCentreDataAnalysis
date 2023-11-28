# -*- coding: utf-8 -*-
"""

@author: Vinoj
"""

import pandas as pd

# File path
csv_file_path = r'C:\Users\Vinoj\OneDrive\Desktop\Ashoka_PEDP\Project 1\Workfile.csv'

# Chunk size
chunk_size = 10000

# Specific phrase to search for in 'QueryText'
specific_phrase = 'blast'

# Set the start and end year
start_year = 2006
end_year = 2023

# Container for counts for each year
phrase_counts_by_year = {}

# Iterate through years
for target_year in range(start_year, end_year + 1):
    # Counter for the number of occurrences
    phrase_count = 0

    # Iterate through chunks
    for chunk in pd.read_csv(csv_file_path, chunksize=chunk_size):
        # Filter rows for the targeted year within the chunk
        year_filtered_chunk = chunk[chunk['Year'] == target_year]

        # Count occurrences of the specific phrase in 'QueryText' within the chunk
        phrase_count += year_filtered_chunk['QueryText'].str.contains(specific_phrase, case=False, na=False).sum()

    # Store the count for the current year
    phrase_counts_by_year[target_year] = phrase_count

# Display counts for each year
for year, count in phrase_counts_by_year.items():
    print(f"The phrase '{specific_phrase}' occurred {count} times in the 'QueryText' for the year {year}.")
