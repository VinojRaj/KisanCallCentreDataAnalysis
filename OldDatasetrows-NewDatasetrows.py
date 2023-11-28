# -*- coding: utf-8 -*-
"""

@author: Vinoj
"""

import pandas as pd

# Replace with the path to your CSV file
csv_file_path = r'C:/Users/Vinoj/OneDrive/Desktop/Ashoka_PEDP/Project 1/KCC12-22.csv'

# Set the chunk size
chunk_size = 100000

# Initialize a counter for total rows
total_rows = 0

# Read the CSV file in chunks and update the total row count
for chunk in pd.read_csv(csv_file_path, chunksize=chunk_size):
    print(f"Processing chunk {chunk.index[0] + 1}...")
    total_rows += len(chunk)

print(f"Total number of rows in the dataset: {total_rows}")

# Replace with the path to your CSV file
csv_file_path2 = r'C:/Users/Vinoj/OneDrive/Desktop/Ashoka_PEDP/Project 1/KCC12-22_updated.csv'

# Initialize a counter for total rows
total_rows2 = 0

# Read the CSV file in chunks and update the total row count
for chunk2 in pd.read_csv(csv_file_path2, chunksize=chunk_size):
    print(f"Processing chunk {chunk.index[0] + 1}...")
    total_rows2 += len(chunk2)
    
print(f"Total number of rows in the dataset: {total_rows}")
print(f"Total number of rows in the dataset New: {total_rows2}")

# Print the difference between total_rows and total_rows2
difference = total_rows - total_rows2
print("The difference is:", difference)

# Check if the difference is 328 and print the corresponding message
if difference == 0:
    print("Success!")
else:
    print("Something went wrong!")
