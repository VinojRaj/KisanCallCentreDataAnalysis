# -*- coding: utf-8 -*-
"""

@author: Vinoj
"""

import pandas as pd

# Replace 'your_file_path.csv' with the actual path to your dataset
file_path = 'C:/Users/Vinoj/OneDrive/Desktop/Ashoka_PEDP/Project 1/KCC12-22.csv'

# Set the number of rows to read
nrows_to_read = 5

# Read the first nrows_to_read rows into a DataFrame
df = pd.read_csv(file_path, nrows=nrows_to_read)

# Get the column names
column_names = df.columns

# Print the column names
print("Column Names:")
for col in column_names:
    print(col)