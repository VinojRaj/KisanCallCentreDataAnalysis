# -*- coding: utf-8 -*-
"""

@author: Vinoj
"""

import pandas as pd

# Load the data from the CSV file
df = pd.read_csv('C:/Users/Vinoj/OneDrive/Desktop/Ashoka_PEDP/Project 1/KCC12-22_updated.csv')

# Filter the DataFrame for the specific 'QueryType' values
df_filtered = df[df['QueryType'].isin(['Nutrient Management', 'Fertilizer Use and Availability'])]

# Group by 'Month' and calculate the count for each month
monthly_counts = df_filtered['DistrictName'].value_counts()

# Display the result
print(monthly_counts)

# Export DataFrame to CSV
monthly_counts.to_csv('C:/Users/Vinoj/OneDrive/Desktop/Ashoka_PEDP/Project 1/Monthly2.csv', index=True)
