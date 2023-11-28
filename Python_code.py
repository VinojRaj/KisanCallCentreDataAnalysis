# -*- coding: utf-8 -*-
"""
@author: Vinoj
"""
import pandas as pd

# Assuming you've already read the CSV file into a DataFrame
read_file = pd.read_csv(r'C:\Users\Vinoj\OneDrive\Desktop\Ashoka_PEDP\Project 1\Workfile.csv')

# Create a new DataFrame with the first 100 rows
first_100_values = read_file.head(100)

# Write the new DataFrame to an Excel file
first_100_values.to_excel(r'C:\Users\Vinoj\OneDrive\Desktop\Ashoka_PEDP\Project 1\First_100_Values.xlsx', index=False)
