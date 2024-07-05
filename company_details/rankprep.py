import pandas as pd
import os

# Get the current directory
current_directory = os.path.dirname(os.path.abspath(__file__))

# Define the file paths
file1_path = os.path.join(current_directory, 'revenue-group.csv')
file2_path = os.path.join(current_directory, 'combined-companies.csv')

# Read the first CSV file into a DataFrame
file1 = pd.read_csv(file1_path)

# Convert the DataFrame to a dictionary for quick lookup
value_dict = file1.set_index('key')['value'].to_dict()

# Read the second CSV file into a DataFrame
file2 = pd.read_csv(file2_path)

# Define a function to perform the multiplication
def multiply_value(row):
    e_gp = row['RevGp']
    indtemp = row['indtemp2']
    value = value_dict.get(e_gp, None)
    if value is not None:
        return indtemp * value
    else:
        return None

# Apply the function to each row in file2 to create the 'indtemp2' column
file2['indtemp3'] = file2.apply(multiply_value, axis=1)

# Save the modified DataFrame back to the second CSV file
file2.to_csv(file2_path, index=False)

print("The values have been multiplied and the 'indtemp2' column has been added to combined-companies.csv.")
