import os
import pandas as pd
import re

# Get the current script's directory
script_dir = os.path.dirname(os.path.abspath(__file__))

# Construct the file path
file_path = os.path.join(script_dir, 'combined-companies.csv')

# Read the CSV file
df = pd.read_csv(file_path)

# Function to extract a four-digit number from a string
def extract_year_from_string(date_str):
    try:
        year = re.search(r'\b\d{4}\b', date_str).group(0)
        return int(year)
    except AttributeError:
        return None

# Add a new column 'founded year' with extracted years
#df['founded year'] = df['founded date'].apply(lambda x: extract_year_from_string(x) if isinstance(x, str) else None)
df['lastfundedyear'] = df['last funding date'].apply(lambda x: extract_year_from_string(x) if isinstance(x, str) else None)
# Print the first few rows to debug
print(df.head())

# Save the modified DataFrame back to the CSV file
df.to_csv(file_path, index=False)
