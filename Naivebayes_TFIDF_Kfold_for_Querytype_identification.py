# -*- coding: utf-8 -*-
"""
@author: Vinoj
"""
import pandas as pd
from sklearn.model_selection import train_test_split, KFold
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, classification_report

# File path for the CSV file
csv_file_path = r'C:\Users\Vinoj\OneDrive\Desktop\Ashoka_PEDP\Project 1\KCC12-22.csv'

# Chunk size for reading the CSV file
read_chunk_size = 100000
# Chunk size for processing data (adjust based on memory constraints)
process_chunk_size = 100000
# K-fold cross-validation
k_folds = 10

# Initialize an empty DataFrame to append chunks
df_list = []

# Read the CSV file in chunks
for i, chunk in enumerate(pd.read_csv(csv_file_path, chunksize=read_chunk_size)):
    print(f"\Processing chunk {i + 1}")`
    # Process each chunk as needed
    non_numerical_data = chunk[~chunk['QueryType'].astype(str).str.isnumeric()]
    numerical_data = chunk[chunk['QueryType'].astype(str).str.isnumeric()]

    # Add QueryType missing values to numerical_data
    numerical_data = pd.concat([numerical_data, chunk[chunk['QueryType'].isnull()]])

    # Remove QueryText missing data from non_numerical_data
    non_numerical_data = non_numerical_data.dropna(subset=['QueryText', 'QueryType'])

    # Split the non-numerical data into training and testing sets
    train_data, test_data, train_labels, test_labels = train_test_split(
        non_numerical_data['QueryText'],
        non_numerical_data['QueryType'],
        test_size=0.2,
        random_state=42
    )

    # Text vectorization
    vectorizer = TfidfVectorizer()
    
    # Initialize k-fold cross-validation
    kf = KFold(n_splits=k_folds, shuffle=True, random_state=42)

    # Model training on non-numerical instances with k-fold cross-validation
    for fold, (train_index, val_index) in enumerate(kf.split(train_data), 1):
        train_fold, val_fold = train_data.iloc[train_index], train_data.iloc[val_index]
        train_labels_fold, val_labels_fold = train_labels.iloc[train_index], train_labels.iloc[val_index]

        # Text vectorization for the current fold
        train_vectors = vectorizer.fit_transform(train_fold)
        val_vectors = vectorizer.transform(val_fold)

        print(f"\nTraining Fold {fold} - Data shape: {train_fold.shape}")
        print(f"Validation Fold {fold} - Data shape: {val_fold.shape}")

        # Train the model only on the last fold
        if fold == k_folds:
            classifier = MultinomialNB()
            classifier.fit(train_vectors, train_labels_fold)

            # Evaluate the model on the validation fold
            val_predictions = classifier.predict(val_vectors)
            accuracy = accuracy_score(val_labels_fold, val_predictions)
            # Use the classification_report with zero_division parameter for validation
            report = classification_report(val_labels_fold, val_predictions, zero_division=1)
            
            print(f"\nValidation Metrics for Fold {fold}:")
            print(f"Accuracy: {accuracy:.2f}")

    # Use the trained model to predict QueryType for numerical instances (using chunks)
    predicted_query_types = []

    for start in range(0, len(numerical_data), process_chunk_size):
        end = start + process_chunk_size
        numerical_vectors = vectorizer.transform(numerical_data['QueryText'].iloc[start:end])
        numerical_predictions = classifier.predict(numerical_vectors)

        # Store the predictions for the current chunk
        predicted_query_types.extend(numerical_predictions)

    # Add the PredictedQueryType column to the numerical_data DataFrame
    numerical_data['PredictedQueryType'] = predicted_query_types

    # Append the processed chunk to the list
    df_list.append(numerical_data)

# Concatenate all chunks into a single DataFrame
df = pd.concat(df_list, ignore_index=True)

# Calculate accuracy on the test set
test_vectors = vectorizer.transform(test_data)
test_predictions = classifier.predict(test_vectors)
accuracy_test = accuracy_score(test_labels, test_predictions)

# Print accuracy and classification report
print("\nFinal Test Metrics:")
print(f"Accuracy: {accuracy_test:.2f}")
# Use the classification_report with zero_division parameter
report = classification_report(test_labels, test_predictions, zero_division=1)
print(f"Classification Report:\n{report}")

# Export the DataFrame with numerical instances and predictions to CSV
numerical_export_csv_path = 'numerical_instances_with_predictions.csv'
df.to_csv(numerical_export_csv_path, index=False)

# Print the total number of rows in the exported CSV
num_rows_exported_numerical = len(df)
print(f"\nTotal number of numerical rows exported: {num_rows_exported_numerical}")

print("Done.")
