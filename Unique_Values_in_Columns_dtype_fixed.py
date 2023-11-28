# -*- coding: utf-8 -*-
"""

@author: Vinoj
"""

import pandas as pd

# Replace with the path to your CSV file
csv_file_path = r'C:/Users/Vinoj/OneDrive/Desktop/Ashoka_PEDP/Project 1/KCC12-22_updated.csv'

# Set the chunk size
chunk_size = 1000000

# Initialize a set to store unique values of the 'Crop' column
unique_crops = set()

# Read the CSV file in chunks and update unique values
for chunk in pd.read_csv(csv_file_path, usecols=['QueryType'], chunksize=chunk_size):
    print(f"Processing chunk {chunk.index[0] + 1}...")
    
    # Convert 'Crop' column to string, handling NaN values
    chunk['QueryType'] = chunk['QueryType'].apply(lambda x: str(x) if pd.notna(x) else 'NaN')
    
    unique_crops.update(chunk['QueryType'].unique())

# Print the unique values of the 'Crop' column
#print("Unique values in the 'QueryText' column:")
#print(sorted(unique_crops))

# Write unique values to a CSV file
unique_crops_df = pd.DataFrame(sorted(unique_crops), columns=['QueryType'])
unique_crops_df.to_csv(r'C:/Users/Vinoj/OneDrive/Desktop/Ashoka_PEDP/Project 1/UniqueQueryType_final.csv', index=False)
