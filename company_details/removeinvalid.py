import pandas as pd
import os

# Get the directory where the script is stored
script_dir = os.path.dirname(os.path.abspath(__file__))

# Construct the path to the CSV file
csv_file_path = os.path.join(script_dir, 'combined-companies.csv')

# Read the CSV file
df = pd.read_csv(csv_file_path)

# Define the range of values to be removed
values_to_remove = [f'G{i}' for i in range(10, 27)]

# Filter the DataFrame to exclude the rows with the specified values
filtered_df = df[~df['RevGp'].isin(values_to_remove)]

# Save the filtered DataFrame back to the CSV file
filtered_df.to_csv(csv_file_path, index=False)
