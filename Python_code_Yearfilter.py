# -*- coding: utf-8 -*-
"""

@author: Vinoj
"""

import pandas as pd

# File paths
csv_file_path = r'C:\Users\Vinoj\OneDrive\Desktop\Ashoka_PEDP\Project 1\Workfile.csv'
excel_file_path = r'C:\Users\Vinoj\OneDrive\Desktop\Ashoka_PEDP\Project 1\Values_Year_2006.xlsx'

# Read only the rows with Year attribute equal to 2006
data_for_2006 = pd.read_csv(csv_file_path)
data_for_2006 = data_for_2006[data_for_2006['Year'] == 2006]

# Write the filtered data to the Excel file
data_for_2006.to_excel(excel_file_path, index=False, header=True)