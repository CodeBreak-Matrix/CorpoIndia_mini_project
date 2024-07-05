import pandas as pd
import os

# Conversion rate from Rupees to Dollars (adjust as needed)
conversion_rate = 0.012  # Example: 1 Rupee = 0.012 Dollars

# Get the directory of the current script
script_dir = os.path.dirname(os.path.abspath(__file__))

# Construct the file path
file_path = os.path.join(script_dir, 'fundscomb.csv')

# Read the CSV file
df = pd.read_csv(file_path)

# Define a function to convert Rupees to Dollars
def convert_to_dollars(rupees):
    return rupees * conversion_rate

# Apply the conversion function to the 'RupeesAmount' column and create a new column 'dollarAmt'
df['dollarAmt'] = df['RupeesAmount'].apply(convert_to_dollars)

# Overwrite the original CSV file with the updated DataFrame
df.to_csv(file_path, index=False)

print("Conversion completed and saved to 'fundscomb.csv'.")
