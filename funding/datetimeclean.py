import csv
import os
from datetime import datetime

# Function to convert date string to formatted date
def convert_to_formatted_date(date_string):
    try:
        date_object = datetime.strptime(date_string, '%b %d, %Y')
        return date_object.strftime('%Y-%m-%d')
    except ValueError:
        return None  # Return None if date string is invalid

# Get the current directory
current_dir = os.getcwd()

# Define the file names relative to the current directory
csv_file = os.path.join(current_dir, "fund10.csv")
temp_file = os.path.join(current_dir, "temp_fund1.csv")

# Open input CSV file for reading and temporary file for writing with UTF-8 encoding
with open(csv_file, 'r', newline='', encoding='utf-8') as infile, open(temp_file, 'w', newline='', encoding='utf-8') as outfile:
    reader = csv.reader(infile)
    writer = csv.writer(outfile)
    
    # Process each row in the CSV
    for row in reader:
        # Check if index 3 (fourth column) exists and is not empty
        if len(row) > 3 and row[3].strip():  
            date_string = row[3]
            
            # Convert date string to formatted date
            formatted_date = convert_to_formatted_date(date_string)
            
            if formatted_date:
                # Append the formatted date to the row
                row.append(formatted_date)
            else:
                # Handle case where date conversion fails (optional)
                row.append("Invalid Date")  # Placeholder for invalid dates
        
        # Write the updated row to the temporary file
        writer.writerow(row)

# Replace the original CSV file with the temporary file
os.replace(temp_file, csv_file)

print(f"Conversion complete. Updated CSV file '{csv_file}'.")
