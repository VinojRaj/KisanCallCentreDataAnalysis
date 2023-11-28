# -*- coding: utf-8 -*-
"""

@author: Vinoj
"""

import pandas as pd

# Load the data from the CSV file
df = pd.read_csv('C:/Users/Vinoj/OneDrive/Desktop/Ashoka_PEDP/Project 1/KCC12-22_updated.csv')

# Ensure the 'Year' column is of type int
#df['StateName'] = df['StateName'].astype(str)

# Group by 'Year' and calculate the count for each year
yearly_counts = df['Month'].value_counts()

# Display the result
print(yearly_counts)

# Export DataFrame to CSV
yearly_counts.to_csv('C:/Users/Vinoj/OneDrive/Desktop/Ashoka_PEDP/Project 1/Monthly.csv', index=True)