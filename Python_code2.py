# -*- coding: utf-8 -*-
"""
@author: Vinoj
"""

import pandas as pd

# File paths
csv_file_path = r'C:\Users\Vinoj\OneDrive\Desktop\Ashoka_PEDP\Project 1\Workfile.csv'
excel_file_path = r'C:\Users\Vinoj\OneDrive\Desktop\Ashoka_PEDP\Project 1\First_100_Values.xlsx'

# Read only the first 100 rows
first_100_values = pd.read_csv(csv_file_path, nrows=100)

# Write the first 100 rows to the Excel file
first_100_values.to_excel(excel_file_path, index=False, header=True)