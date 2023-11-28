# -*- coding: utf-8 -*-
"""

@author: Vinoj
"""

import pandas as pd
from wordcloud import WordCloud
import matplotlib.pyplot as plt

print('Start!')
# Load the data from the CSV file
df = pd.read_csv('C:/Users/Vinoj/OneDrive/Desktop/Ashoka_PEDP/Project 1/KCC12-22_updated.csv')
print('read')
# Define the 'QueryType' values you're interested in
query_types = ['Nutrient Management', 'Fertilizer Use and Availability']  # Replace this with your actual QueryType values
print('filter loaded')
# List of words to be removed
remove_words = ['NUTRIENT MANAGEMENT', 'nutrient management', 'Information regarding', 'information regarding', 'fertilizer management', 'FARMER ASKED', 'Farmer want', 'know', 'crop', 'asked','weather', 'FARMER ASKED', 'Farmer want', 'Information control' 'INFORMATION REGARDING']
#print('word filter loaded')
# Filter the DataFrame for the specific 'QueryType' values
df_filtered = df[df['QueryType'].isin(query_types)]
print('filter applied')
# Replace NaN values with an empty string
df_filtered.loc[:, 'QueryText'] = df_filtered['QueryText'].fillna('')
print('NaN filled')
# Convert 'QueryText' values to string and join
text = ' '.join(df_filtered['QueryText'].astype(str))
print('text ready')
# Remove the specified words
for word in remove_words:
    text = text.replace(' ' + word + ' ', ' ')
print('word filtered')
# Create a WordCloud object
wordcloud = WordCloud(width = 1000, height = 500).generate(text)
print('WordCloud Ready')
# Display the generated image
plt.figure(figsize=(15,8))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.savefig('C:/Users/Vinoj/OneDrive/Desktop/Ashoka_PEDP/Project 1/Nutrient_wordcloud.png')
print('Done')