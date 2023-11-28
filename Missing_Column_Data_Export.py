# -*- coding: utf-8 -*-
"""

@author: Vinoj
"""

import pandas as pd

Main_file = r'C:/Users/Vinoj/OneDrive/Desktop/Ashoka_PEDP/Project 1/KCC12-22.csv'


# Create an empty DataFrame to store missing rows
missing_rows_df = pd.DataFrame()

# Function to process chunks of data
def process_chunk(chunk):
    global missing_rows_df
    
    # Filter rows with missing values in 'QueryText' column
    missing_query_text_rows = chunk[chunk['QueryText'].isnull()]
    
    # Append missing rows to the DataFrame
    missing_rows_df = pd.concat([missing_rows_df, missing_query_text_rows])

# Set the chunk size based on your system's memory capacity
chunk_size = 100000

# Iterate over chunks
for chunk_number, chunk in enumerate(pd.read_csv(Main_file, chunksize=chunk_size)):
    print(f"Processing chunk {chunk_number + 1}")

    # Add debugging print for every chunk
    print(f"Number of rows in chunk: {len(chunk)}")

    # Process the current chunk
    process_chunk(chunk)

    print(f"Chunk {chunk_number + 1} processed successfully\n")

# Save the DataFrame with missing rows to a CSV file
missing_rows_df.to_csv('missing_query_text_rows.csv', index=False)

print("All chunks processed. Missing rows saved to 'missing_query_text_rows.csv'.")
