# -*- coding: utf-8 -*-
"""

@author: Vinoj
"""

import pandas as pd

# File paths
csv_file_path = r'C:\Users\Vinoj\OneDrive\Desktop\Ashoka_PEDP\Project 1\Workfile.csv'
excel_file_path = r'C:\Users\Vinoj\OneDrive\Desktop\Ashoka_PEDP\Project 1\Yearwise\Values_Year_2012.xlsx'

# Chunk size
chunk_size = 10000

# Create Excel writer
with pd.ExcelWriter(excel_file_path, engine='xlsxwriter') as writer:

    # Iterate through chunks
    for i, chunk in enumerate(pd.read_csv(csv_file_path, chunksize=chunk_size)):
        
        # Filter rows where the "Year" attribute is equal to the year provided
        chunk_yearly = chunk[chunk['Year'] == 2012]

        # Write the chunk to the Excel file, specifying the start row
        chunk_yearly.to_excel(writer, sheet_name='Sheet1', index=False, header=False, startrow=i * chunk_size)

# The Excel file is now complete with all rows where "Year" is equal to year provided
print(f'Data written to: {excel_file_path}')
