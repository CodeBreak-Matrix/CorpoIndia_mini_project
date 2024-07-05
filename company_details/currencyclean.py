import pandas as pd
import os
import re

# Define the function to clean and convert currency strings to integers
def convert_currency(amount):
    amount = str(amount).strip().replace('$', '').replace(',', '')
    
    # Clean the amount string by removing non-numeric characters except for '.', '₹', and '€'
    amount = re.sub(r'[^\d.₹€]', '', amount)
    
    if amount == '—' or amount == '':  # Handle the case where amount is "—" or blank
        return 0
    
    # Handle specific currency symbols
    if '₹' in amount:  # Handle rupee symbol if present
        amount = amount.replace('₹', '').strip()
        amount = int(float(amount) * 0.014)  # Convert rupees to dollars (assuming 1 Rupee = 0.014 USD)
    elif '€' in amount:  # Handle euro symbol if present
        amount = amount.replace('€', '').strip()
        amount = int(float(amount) * 1.12)  # Convert euros to dollars (assuming 1 Euro = 1.12 USD)
    else:  # No currency symbol, convert directly
        try:
            amount = float(amount)
            amount = int(amount)
        except ValueError:
            return 0
    
    return amount

# Function to process the CSV file
def process_csv(input_file):
    # Read CSV into pandas DataFrame
    df = pd.read_csv(input_file)
    
    # Convert 'totfundamt' column to integers for both dollar, rupee, and euro amounts
    #df['tfa'] = df['totfundamt'].apply(convert_currency)
    df['lfa'] = df['lastfundamt'].apply(convert_currency)
    
    # Save back to the CSV file
    df.to_csv(input_file, index=False)

# Main script execution
if __name__ == "__main__":
    # Get current script directory
    script_dir = os.path.dirname(os.path.realpath(__file__))
    
    # Define input file path
    input_file = os.path.join(script_dir, 'combined-companies.csv')
    
    # Process the CSV file
    process_csv(input_file)
