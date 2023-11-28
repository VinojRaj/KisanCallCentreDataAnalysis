import pandas as pd
from collections import Counter
import re

# File path
csv_file_path = r'C:\Users\Vinoj\OneDrive\Desktop\Ashoka_PEDP\Project 1\Workfile.csv'

# Chunk size
chunk_size = 10000

# Numeric query types for which to retrieve data
target_query_types = [0, 1, 10, 100, 102, 11, 12, 15, 16, 17, 18, 19, 2, 20, 21, 22, 26, 27, 29, 3, 31, 32, 33, 34, 36, 37, 38, 39, 40, 43, 44, 45, 46, 47, 48, 49, 5, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 6, 60, 61, 74, 75, 76, 78, 8, 83, 84, 85, 87, 88, 89, 9, 90, 91, 92, 93, 94, 95, 99, 9999]

# Container for sample data for each target query type
sample_data_dict = {}

# Counter for word occurrences
word_counts_dict = {}

# Iterate through chunks
for chunk in pd.read_csv(csv_file_path, chunksize=chunk_size):
    # Check if the current query type is in the list of target query types
    filtered_chunk = chunk[chunk['QueryType'].astype(str).isin(map(str, target_query_types))]

    # Process "QueryText" for each target query type in the chunk
    for query_type in target_query_types:
        sample_data = filtered_chunk[filtered_chunk['QueryType'].astype(str) == str(query_type)]
        if not sample_data.empty:
            # Combine "QueryText" for all rows into a single string
            all_query_text = ' '.join(sample_data['QueryText'].astype(str))

            # Tokenize the combined text into words
            words = re.findall(r'\b\w+\b', all_query_text.lower())  # Convert to lowercase for case-insensitivity

            # Update the word occurrences counter for each query type
            if query_type not in word_counts_dict:
                word_counts_dict[query_type] = Counter()
            word_counts_dict[query_type].update(words)

# Create a Pandas Excel writer
excel_writer = pd.ExcelWriter(r'C:\Users\Vinoj\OneDrive\Desktop\Ashoka_PEDP\Project 1\PythonAnalysis_output\MostCommonWords.xlsx', engine='xlsxwriter')

# Process "QueryText" for each target query type and write most common words to separate sheets
for query_type, word_counts in word_counts_dict.items():
    # Get the most common words for each query type
    most_common_words = word_counts.most_common(25)  # Adjust the number as needed

    # Create a DataFrame for the most common words
    most_common_words_df = pd.DataFrame(most_common_words, columns=['Word', 'Count'])

    # Write the most common words DataFrame to the Excel file
    most_common_words_df.to_excel(excel_writer, sheet_name=f'MostCommonWords_{query_type}', index=False)

# Save the Excel file
excel_writer.close()
print('Done')
