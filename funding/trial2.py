import pandas as pd
import re
import os

# Fixed exchange rate (1 USD = 75 INR)
fixed_exchange_rate = 75
csv_files = [f for f in os.listdir("F:\miniproject") if f.endswith('.csv')]
# Function to convert dollar amount to rupees using the fixed exchange rate
def convert_dollar_to_rupees(dollar_amount):
    # Remove alphabet characters from the beginning of the string (assuming they denote currency type)
    dollar_amount = re.sub(r'^[a-zA-Z]+', '', dollar_amount)
    
    # Remove '$' and commas from the dollar_amount string
    dollar_amount = dollar_amount.replace('$', '').replace(',', '')
    
    # Convert to float and then to integer (assuming dollar_amount is in decimal format)
    dollar_float = float(dollar_amount)  # Assuming dollar amount is in dollars
    rupees_int = int(dollar_float * fixed_exchange_rate)
    
    return rupees_int

# Function to clean and convert currency string to integer
def clean_currency_string(currency_str):
    # Remove rupee symbol and commas
    cleaned_str = currency_str.replace('₹', '').replace(',', '')
    # Convert to integer
    return int(cleaned_str)

# Function to convert any non-numeric string to integer 0
def convert_non_numeric_to_zero(amount):
    try:
        return int(amount)
    except ValueError:
        return 0
def convert_amount(amount):
    if '$' in amount or re.match(r'^[a-zA-Z]+', amount):
        return convert_dollar_to_rupees(amount)
    elif '₹' in amount:
        return clean_currency_string(amount)
    else:
        return convert_non_numeric_to_zero(amount)
# Determine the file path relative to the script location
script_dir = os.path.dirname(__file__)
for r in csv_files:
    file_path = os.path.join(script_dir, r)

    # Read the CSV file
    df = pd.read_csv(file_path)

    # Apply conversion functions based on currency symbol presence, alphanumeric start, or non-numeric strings


    # Apply conversion function to 'Amount' column and create a new 'RupeesAmount' column
    df['RupeesAmount'] = df['Amount'].apply(convert_amount)

    # Save the modified DataFrame back to the original CSV file
    df.to_csv(file_path, index=False)

    print(f"Conversion completed. Updated '{file_path}' with 'RupeesAmount' column.")
