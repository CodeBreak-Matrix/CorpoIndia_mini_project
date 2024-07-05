import csv
import os

def add_unique_id(input_csv, output_csv, company_mapping_csv):
    try:
        # Read the input CSV file with UTF-8 encoding
        with open(input_csv, 'r', newline='', encoding='utf-8') as infile:
            reader = csv.DictReader(infile)
            fieldnames = reader.fieldnames + ['CID']
            
            rows = list(reader)
            
        # Create a list to store company mappings
        company_mappings = []

        # Add unique IDs to each row
        for i, row in enumerate(rows):
            cid = f'CID{i+1}'
            row['CID'] = cid
            company_mappings.append({'CID': cid, 'Company': row['Company']})
        
        # Write the updated rows to the output CSV file with UTF-8 encoding
        with open(output_csv, 'w', newline='', encoding='utf-8') as outfile:
            writer = csv.DictWriter(outfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(rows)
        
        # Write the company mappings to the company mapping CSV file with UTF-8 encoding
        with open(company_mapping_csv, 'w', newline='', encoding='utf-8') as mappingfile:
            fieldnames = ['CID', 'Company']
            writer = csv.DictWriter(mappingfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(company_mappings)
        
        # Success message
        print("CSV files processed successfully.")

    except Exception as e:
        print(f"Error occurred: {str(e)}")

# Define your input and output file names
current_directory = os.path.dirname(os.path.abspath(__file__))
input_csv = os.path.join(current_directory, 'fundscomb.csv')
output_csv = os.path.join(current_directory, 'fundcombv2.csv')
company_mapping_csv = os.path.join(current_directory, 'company_mapping.csv')

# Run the function
add_unique_id(input_csv, output_csv, company_mapping_csv)
