# -*- coding: utf-8 -*-
"""

@author: Vinoj
"""

import pandas as pd

# Set the path to your input CSV file
input_csv_path = r'C:\Users\Vinoj\OneDrive\Desktop\Ashoka_PEDP\Project 1\Workfile.csv'

# Set the path to your output CSV file
output_csv_path = r'C:\Users\Vinoj\OneDrive\Desktop\Ashoka_PEDP\Project 1\KCC12-22.csv'

# Set the range of years you want to filter (2012 to 2022 in this case)
start_year = 2012
end_year = 2022

# Set the chunk size based on your system's memory capacity
chunk_size = 50000  # You can adjust this based on your system's memory

# Specify the data types of columns to avoid DtypeWarning
column_data_types = {'Year': int}  # Adjust the column name and data type as needed

# Create a CSV reader object with specified data types
csv_reader = pd.read_csv(input_csv_path, chunksize=chunk_size, dtype=column_data_types)

# Create an empty DataFrame to store the filtered data
filtered_data = pd.DataFrame()

# Iterate over chunks
for chunk in csv_reader:
    # Filter rows based on the 'Year' attribute
    chunk_filtered = chunk[(chunk['Year'] >= start_year) & (chunk['Year'] <= end_year)]
    
    # Append the filtered chunk to the overall filtered data
    filtered_data = pd.concat([filtered_data, chunk_filtered], ignore_index=True)

# Save the filtered data to a new CSV file
filtered_data.to_csv(output_csv_path, index=False)

print(f"Filtered data saved to {output_csv_path}")
`
