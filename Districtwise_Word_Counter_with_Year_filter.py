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
target_year = 2022

# Specific phrase to search for in 'QueryText'
specific_phrase = 'Blast'

# Container for counts for each district
phrase_counts_by_district = {}

# Iterate through chunks
for chunk in pd.read_csv(csv_file_path, chunksize=chunk_size):
    # Filter rows for the targeted year within the chunk
    year_filtered_chunk = chunk[chunk['Year'] == target_year]

    # Iterate through unique values of "DistrictName"
    for district_name, district_data in year_filtered_chunk.groupby('DistrictName'):
        # Counter for the number of occurrences
        phrase_count = district_data['QueryText'].str.contains(specific_phrase, case=False, na=False).sum()

        # Store the count for the current district
        if district_name not in phrase_counts_by_district:
            phrase_counts_by_district[district_name] = 0
        phrase_counts_by_district[district_name] += phrase_count

# Create a DataFrame from the dictionary
result_df = pd.DataFrame(list(phrase_counts_by_district.items()), columns=['DistrictName', 'OccurrenceCount'])

# Display counts for each district
for district, count in phrase_counts_by_district.items():
    print(f"The phrase '{specific_phrase}' occurred {count} times in the 'QueryText' for the district {district} in the year {target_year}.")

# Export the results to Excel with target year in the file name
export_file_name = f'Phrases_Occurrences_By_District_{target_year}.xlsx'
result_df.to_excel(export_file_name, index=False)
