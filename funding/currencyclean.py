from pyspark.sql import SparkSession
from pyspark.sql.functions import udf
from pyspark.sql.types import IntegerType
import re
import os

# Initialize Spark session
spark = SparkSession.builder.appName("CurrencyConversion").getOrCreate()

try:
    # Path to the input CSV file (assuming it's in the same directory as the script)
    script_directory = os.path.dirname(os.path.abspath(__file__))
    input_csv_path = os.path.join(script_directory, "fund1.csv")

    # Read CSV file into DataFrame
    df = spark.read.csv(input_csv_path, header=True, inferSchema=True)

    # Define conversion rate
    conversion_rate_dollar_to_rupees = 75  # Example conversion rate: 1 dollar = 75 rupees

    # Define UDF to convert currency string to rupees
    def currency_conversion(currency_str):
        try:
            # Check if the value is '-'
            if currency_str.strip() == '-':
                return 0
            # Remove currency symbols and commas
            if currency_str.startswith('$'):
                clean_str = re.sub(r'[$,]', '', currency_str)
                dollar_amount = int(clean_str)
                rupees_amount = dollar_amount * conversion_rate_dollar_to_rupees
                return rupees_amount
            elif currency_str.startswith('₹'):
                clean_str = re.sub(r'[₹,]', '', currency_str)
                rupees_amount = int(clean_str)
                return rupees_amount
            else:
                return None
        except ValueError:
            return None

    # Register UDF
    currency_conversion_udf = udf(currency_conversion, IntegerType())

    # Apply UDF to DataFrame
    df_with_converted_amount = df.withColumn("RupeesAmount", currency_conversion_udf(df["Amount"]))

    # Show result
    df_with_converted_amount.show()

    # Path to the output CSV file (in the same directory as the script)
    output_csv_path = os.path.join(script_directory, "fund1_converted.csv")

    # Write transformed DataFrame to CSV
    df_with_converted_amount.write.csv(output_csv_path, header=True, mode="overwrite")

    print(f"Conversion successful. Output saved to {output_csv_path}")

except Exception as e:
    print(f"Error: {e}")

finally:
    # Stop Spark session
    if 'spark' in locals():
        spark.stop()
