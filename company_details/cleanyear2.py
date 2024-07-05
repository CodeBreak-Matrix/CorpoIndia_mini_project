import os
import csv

def update_founded_year(csv_file):
    # Get the current directory of the script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Construct the full path to the CSV file
    csv_file_path = os.path.join(script_dir, csv_file)
    
    # Check if the CSV file exists
    if not os.path.isfile(csv_file_path):
        print(f"Error: File '{csv_file}' not found in '{script_dir}'.")
        return
    
    # Proceed with file processing
    with open(csv_file_path, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        rows = list(reader)
        
        for row in rows:
            founded_year = row['lastfundedyear'].strip()
            founded_date = row['last funding date'].strip()
            
            if founded_year == '':
                if founded_date:
                    # Extract last two digits of founded date
                    try:
                        last_two_digits = int(founded_date[-2:])
                        if last_two_digits > 24:
                            row['lastfundedyear'] = str(1900 + last_two_digits)
                        else:
                            row['lastfundedyear'] = str(2000 + last_two_digits)
                    except ValueError:
                        pass  # Handle if last two digits cannot be converted to int
            
        # Write back to the same file
        with open(csv_file_path, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=reader.fieldnames)
            writer.writeheader()
            writer.writerows(rows)

# Example usage:
update_founded_year('combined-companies.csv')
