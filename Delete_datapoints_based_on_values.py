# -*- coding: utf-8 -*-
"""

@author: Vinoj
"""

import pandas as pd

# Set the path to your input CSV file
input_csv_path = r'C:\Users\Vinoj\OneDrive\Desktop\Ashoka_PEDP\Project 1\KCC12-22.csv'

# Set the path to your output CSV file
output_csv_path = r'C:\Users\Vinoj\OneDrive\Desktop\Ashoka_PEDP\Project 1\KCC12-22_1.csv'

# Set the range of years you want to remove (2006 to 2011 in this case)
years_to_remove = [2023]

# Set the chunk size based on your system's memory capacity
chunk_size = 100000  # You can adjust this based on your system's memory

# Columns to keep (include 'Year' and any other columns you want to keep)
columns_to_keep = ['Year', 'Month', 'Crop', 'DistrictName', 'QueryType', 'StateName', 'QueryText' ]

# Create a CSV reader object with specified columns and chunk size
csv_reader = pd.read_csv(input_csv_path, usecols=columns_to_keep, chunksize=chunk_size)

# Create an empty list to store the chunks after filtering
filtered_chunks = []

# Iterate over chunks
for i, chunk in enumerate(csv_reader):
    print(f"Processing chunk {i + 1}...")
    
    # Remove rows based on the 'Year' attribute
    chunk_filtered = chunk[~chunk['Year'].isin(years_to_remove)]
    
    # Append the filtered chunk to the list
    filtered_chunks.append(chunk_filtered)

# Concatenate the filtered chunks into a single DataFrame
filtered_data = pd.concat(filtered_chunks, ignore_index=True)

# Save the filtered data to a new CSV file
filtered_data.to_csv(output_csv_path, index=False)

print(f"Filtered data saved to {output_csv_path}")

