"""
This script loads raw sales data, performs cleaning steps such as fixing column names,
removing invalid rows, handling missing values, and saves a cleaned dataset.
"""

# This function loads the raw CSV file into a pandas DataFrame.
# Copilot should generate the basic structure for reading the file.
import pandas as pd
def load_data(file_path):
    #read the CSV into a DataFrame
    df = pd.read_csv(file_path)
    return df

# This function standardizes column names by making them lowercase,
# removing spaces, and replacing them with underscores. Copilot should generate the structure.

def clean_column_names(df):
    df.columns = (
        df.columns
        .str.strip()
        .str.lower()
        .str.replace(' ', '_')
    )
    return df

# This function fills missing numeric values for price and quantity.
# Missing values can break calculations, so we replace them with 0 for consistency.

def handle_missing_values(df):
    df["price"] = df["price"].fillna(0)
    df["qty"] = df["qty"].fillna(0)

    return df

# This function removes rows with invalid values such as negative price or quantity.
# Negative numbers are data entry errors and should not be included.

def remove_invalid_rows(df):
    # Convert price and qty to numeric, turning invalid values into NaN
    df["price"] = pd.to_numeric(df["price"], errors="coerce")
    df["qty"] = pd.to_numeric(df["qty"], errors="coerce")

    # Replace any NaNs with 0 (or drop them if you prefer)
    df["price"] = df["price"].fillna(0)
    df["qty"] = df["qty"].fillna(0)

    # Now remove negative rows safely
    df = df[(df["price"] >= 0) & (df["qty"] >= 0)]
    return df


if __name__ == "__main__":
    raw_path = "data/raw/sales_data_raw.csv"
    cleaned_path = "data/processed/sales_data_clean.csv"

    # Load the raw dataset
    df_raw = load_data(raw_path)

    # Clean column names
    df_clean = clean_column_names(df_raw)

    # Handle missing values
    df_clean = handle_missing_values(df_clean)

    # Remove invalid rows
    df_clean = remove_invalid_rows(df_clean)

    # Save cleaned dataset
    df_clean.to_csv(cleaned_path, index=False)

    print("Cleaning complete. First few rows:")
    print(df_clean.head())

