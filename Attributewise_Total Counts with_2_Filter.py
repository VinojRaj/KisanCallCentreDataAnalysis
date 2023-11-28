# -*- coding: utf-8 -*-
"""

@author: Vinoj
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Nov 27 14:39:46 2023

@author: Vinoj
"""

import pandas as pd

# Load the data from the CSV file
df = pd.read_csv('C:/Users/Vinoj/OneDrive/Desktop/Ashoka_PEDP/Project 1/KCC12-22_updated.csv')

# Filter the DataFrame for the specific 'QueryType' values
df_filtered1 = df[df['QueryType'].isin(['Dairy Production', 'Animal Breeding', 'Livestock Products Processing and Packaging', 'Animal Production Piggery Goatery Sheep Farming etc', 'Animal Nutrition', 'Cattle shed Planning and Management', 'Poultry'])]

df_filtered2 = df_filtered1[df_filtered1['Year'].isin([2022])]

# Group by 'Month' and calculate the count for each month
monthly_counts = df_filtered2['StateName'].value_counts()

# Display the result
print(monthly_counts)

# Export DataFrame to CSV
monthly_counts.to_csv('C:/Users/Vinoj/OneDrive/Desktop/Ashoka_PEDP/Project 1/Monthly2.csv', index=True)
