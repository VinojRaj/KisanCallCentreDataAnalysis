# -*- coding: utf-8 -*-
"""

@author: Vinoj
"""

import pandas as pd

# Assuming you've already read the CSV file into a DataFrame
df = pd.read_csv(r'C:\Users\Vinoj\OneDrive\Desktop\Ashoka_PEDP\Project 1\Workfile.csv')

# Check the current data type of the "Year" column
print("Current data type of 'Year':", df['Year'].dtype)

# Convert the "Year" column to a more memory-efficient data type
df['Year'] = df['Year'].astype('int16')  # or 'int32' if the values are larger

# Check the updated data type
print("Updated data type of 'Year':", df['Year'].dtype)

# Find all unique values in the "Year" attribute
unique_years = df['Year'].unique()

# Display the unique values
print("Unique values in 'Year':", unique_years)
