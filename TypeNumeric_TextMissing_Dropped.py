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

    # Count and print the number of rows with 'QueryText' missing and 'QueryType' consisting of numbers before removal
    num_rows_before = len(chunk[(chunk['QueryText'].isnull()) & (chunk['QueryType'].astype(str).str.isnumeric())])
    print(f"Number of rows with 'QueryText' missing and 'QueryType' consisting of numbers before removal: {num_rows_before}")

    # Remove rows where 'QueryText' is missing and 'QueryType' consists of numbers
    cleaned_chunk = chunk[~((chunk['QueryText'].isnull()) & (chunk['QueryType'].astype(str).str.isnumeric()))]

    # Count and print the number of rows dropped
    num_rows_dropped = len(chunk) - len(cleaned_chunk)
    print(f"Number of rows dropped in this chunk: {num_rows_dropped}")

    cleaned_data = pd.concat([cleaned_data, cleaned_chunk])

# Export the cleaned data to a new CSV file
cleaned_data.to_csv(output_csv_path, index=False)

print("Rows where 'QueryText' is missing and 'QueryType' consists of numbers removed.")
print(f"Cleaned data exported to {output_csv_path}")
