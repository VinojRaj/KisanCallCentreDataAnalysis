# -*- coding: utf-8 -*-
"""

@author: Vinoj
"""

import pandas as pd
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import nltk
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk import pos_tag

# Load the data from the CSV file
df = pd.read_csv('C:/Users/Vinoj/OneDrive/Desktop/Ashoka_PEDP/Project 1/KCC12-22_updated.csv')
print('Read')
# Define the 'QueryType' values you're interested in
query_types = ['Plant Protection', 'Disease Management', 'Disease reporting', 'Disease']  # Replace this with your actual QueryType values
print('Filter defined')
# Filter the DataFrame for the specific 'QueryType' values
df_filtered = df[df['QueryType'].isin(query_types)]
print('Filtered')
# Replace NaN values with an empty string
df_filtered.loc[:, 'QueryText'] = df_filtered['QueryText'].fillna('')
print('NaN Filled')
# Convert 'QueryText' values to string and join
text = ' '.join(df_filtered['QueryText'].astype(str))
print('Joined')
# Tokenize the text (split it into individual words)
tokens = word_tokenize(text)
print('tokenized')
# Perform POS tagging
tagged = pos_tag(tokens)

# Filter for nouns
nouns = [word for word, pos in tagged if (pos == 'NN' or pos == 'NNS' or pos == 'NNP' or pos == 'NNPS')]
print('nouns filtered')
# Remove stopwords
stop_words = set(stopwords.words('english'))
print('stopwords filtered')
filtered_nouns = [w for w in nouns if not w in stop_words]
print('nouns and stopwords combined')
# Join the filtered nouns into a single string
filtered_nouns_text = ' '.join(filtered_nouns)
print('Starting word Cloud Creation')
# Create a WordCloud object
wordcloud = WordCloud(width = 1000, height = 500).generate(filtered_nouns_text)

# Display the generated image
plt.figure(figsize=(15,8))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")

# Save the image to a file
plt.savefig('disease_wordcloud2.png')
print('Done and Dusted!')