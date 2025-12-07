"""
This script loads raw sales data, performs cleaning steps such as fixing column names,
removing invalid rows, handling missing values, and saves a cleaned dataset.
"""

# This function loads the raw CSV file into a pandas DataFrame.
# Copilot should generate the basic structure for reading the file.
import pandas as pd
def load_raw_data(file_path):
    #read the CSV into a DataFrame
    df = pd.read_csv(file_path)
    return df

# This function standardizes column names by making them lowercase,
# removing spaces, and replacing them with underscores. Copilot should generate the structure.

def standardize_column_names(df):
    df.columns = (
        df.columns
        .str.string()
        .str.lower()
        .str.replace(' ', '_')
    )
    return df

# This function fills missing numeric values for price and quantity.
# Missing values can break calculations, so we replace them with 0 for consistency.

def handle_missing_values(df):
    df["price"] = df["price"].fillna(0)
    df["quantity"] = df["quantity"].fillna(0)
    return df

# This function removes rows with invalid values such as negative price or quantity.
# Negative numbers are data entry errors and should not be included.

def remove_invalid_rows(df):
    df = df[(df["price"] >= 0) & (df["quantity"] >= 0)]
    return df

