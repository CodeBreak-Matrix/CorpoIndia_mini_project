import pandas as pd
import os

# Get the directory where the script is stored
script_dir = os.path.dirname(os.path.abspath(__file__))

# Construct the path to the CSV file
csv_file_path = os.path.join(script_dir, 'combined-companies.csv')

# Read the CSV file
df = pd.read_csv(csv_file_path)

# Replace the value of RevGp from G1 to G8
df.loc[df['RevGp'] == 'G1', 'RevGp'] = 'G8'

# Save the updated DataFrame back to the CSV file
df.to_csv(csv_file_path, index=False)
