# -*- coding: utf-8 -*-
"""

@author: Vinoj
"""

import pandas as pd

# Set the chunk size
chunk_size = 100000  # Adjust based on your system's capacity

# Read the CSV file in chunks
csv_file_path = r'C:\Users\Vinoj\OneDrive\Desktop\Ashoka_PEDP\Project 1\KCC12-22.csv'  # Replace with the path to your CSV file
output_csv_path = r'C:\Users\Vinoj\OneDrive\Desktop\Ashoka_PEDP\Project 1\KCC12-22_Final.csv'  # Replace with the desired output path

# Initialize an empty DataFrame to store the cleaned data
cleaned_data = pd.DataFrame()

for chunk in pd.read_csv(csv_file_path, chunksize=chunk_size):
    print(f"Processing chunk {chunk.index[0] + 1}...")
    # Drop rows with missing values in 'QueryType' and 'QueryText'
    cleaned_chunk = chunk.dropna(subset=['QueryType', 'QueryText'], how='all')
    cleaned_data = pd.concat([cleaned_data, cleaned_chunk])

# Export the cleaned data to a new CSV file
cleaned_data.to_csv(output_csv_path, index=False)

print("Rows with missing values for both 'QueryType' and 'QueryText' removed.")
print(f"Cleaned data exported to {output_csv_path}")
