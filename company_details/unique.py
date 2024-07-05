import os
import csv

# Function to generate a unique key in the format "C1", "C2", etc.
def generate_unique_key(index):
    return f'C{index}'

# Get the directory where the script is located
script_dir = os.path.dirname(os.path.realpath(__file__))

# Input and output file paths
input_file = os.path.join(script_dir, 'combined-companies.csv')
output_file = os.path.join(script_dir, 'company-map.csv')

# Function to read CSV safely with encoding detection
def read_csv_safe(file_path):
    with open(file_path, 'r', newline='', encoding='utf-8-sig') as csvfile:
        reader = csv.reader(csvfile)
        header = next(reader)  # Read the header
        rows = list(reader)  # Read all rows into a list
    return header, rows

# Function to write CSV safely with encoding specification
def write_csv_safe(file_path, header, rows):
    with open(file_path, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(header)
        writer.writerows(rows)

# Read the input CSV file
header, rows = read_csv_safe(input_file)

# Add unique keys to each row and update the CSV
key_map = []
new_rows = []
for index, row in enumerate(rows, start=1):
    unique_key = generate_unique_key(index)
    row.insert(0, unique_key)  # Insert unique key as the first element (CompID)
    new_rows.append(row)
    key_map.append([unique_key] + row[1:])  # Exclude the added CompID from key_map

# Write back to the input CSV file
write_csv_safe(input_file, ['CompID'] + header, new_rows)

# Write key-value map to a separate CSV file
write_csv_safe(output_file, ['CompID'] + header, key_map)

print(f"Unique keys added and saved to {input_file}")
print(f"Key-value map saved to {output_file}")
