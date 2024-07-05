import pandas as pd
import os

# Get the current directory where the script is located
current_dir = os.path.dirname(os.path.abspath(__file__))

# Input file path
input_file = os.path.join(current_dir, 'combined-companies.csv')

# Output file path
output_file = os.path.join(current_dir, 'revenue-group.csv')

# Read the CSV file
df = pd.read_csv(input_file)

# Get unique values from the 'revenue' column
unique_values = df['revenue'].unique()

# Create a mapping of unique values to keys
mapping = {value: f'G{i}' for i, value in enumerate(unique_values, 1)}

# Add a new column 'RevGp' to the DataFrame with mapped keys
df['RevGp'] = df['revenue'].map(mapping)

# Save the modified DataFrame (with 'RevGp' column) back to the input CSV file
df.to_csv(input_file, index=False)

# Create a new DataFrame with only unique values and their mapped keys
unique_df = pd.DataFrame({'revenue': unique_values, 'key': [mapping[value] for value in unique_values]})

# Write the new DataFrame to the output CSV file
unique_df.to_csv(output_file, index=False)

print(f"CSV file '{input_file}' updated with 'RevGp' column.")
print(f"CSV file '{output_file}' created successfully with unique values and keys.")
