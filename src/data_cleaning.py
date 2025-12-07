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