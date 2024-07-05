import os
import pandas as pd

# Get the current directory of the script
script_dir = os.path.dirname(os.path.abspath(__file__))

# Construct the full path to your CSV file
file_path = os.path.join(script_dir, 'combined-companies.csv')

# Load the CSV file
df = pd.read_csv(file_path)

# Sort the dataframe based on the 'index' column in descending order
df_sorted = df.sort_values(by='index', ascending=False)

# Add a new column 'Rank' which contains the rank based on 'index' values
df_sorted['Rank'] = range(1, len(df_sorted) + 1)

# Save the updated dataframe back to CSV
df_sorted.to_csv(file_path, index=False)

print("Ranking assigned and saved to", file_path)
