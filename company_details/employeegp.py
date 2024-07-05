import pandas as pd
import os

# Get the current directory where the script is located
current_dir = os.path.dirname(os.path.abspath(__file__))

# Input file path
input_file = os.path.join(current_dir, 'combined-companies.csv')

# Output file path for employee mapping
output_employee_file = os.path.join(current_dir, 'employee-map.csv')

# Read the CSV file
df = pd.read_csv(input_file)

# Get unique values from the 'employee' column
unique_values = df['employee'].unique()

# Create a mapping of unique values to keys
mapping = {value: f'E-G{i}' for i, value in enumerate(unique_values, 1)}

# Add a new column 'E-Gp' to the DataFrame with mapped keys
df['E-Gp'] = df['employee'].map(mapping)

# Save the unique values and their mapped keys to a new CSV file
unique_df = pd.DataFrame({'employee': unique_values, 'E-Gp': [mapping[value] for value in unique_values]})
unique_df.to_csv(output_employee_file, index=False)

# Save the modified DataFrame back to the input CSV file
df.to_csv(input_file, index=False)

print(f"CSV file '{input_file}' updated with 'E-Gp' column.")
print(f"CSV file '{output_employee_file}' created successfully with unique values and keys.")
