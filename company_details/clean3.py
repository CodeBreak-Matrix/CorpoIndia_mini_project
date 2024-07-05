import os
import pandas as pd

# Get the path of the current script
script_dir = os.path.dirname(os.path.abspath(__file__))

# Define the input CSV file path
input_csv_path = os.path.join(script_dir, 'combined-companies.csv')

# Load the CSV file
df = pd.read_csv(input_csv_path)

# Define the range to exclude
exclude_range = [f'E-G{num}' for num in range(12, 63)]

# Filter out rows where 'E-Gp' column has values in the exclude range
filtered_df = df[~df['E-Gp'].isin(exclude_range)]

# Save the filtered DataFrame back to the same CSV file
filtered_csv_path = os.path.join(script_dir, 'combined-companies.csv')
filtered_df.to_csv(filtered_csv_path, index=False)
