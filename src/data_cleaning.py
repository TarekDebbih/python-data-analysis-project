from pathlib import Path

import pandas as pd

BASE_DIR = Path(__file__).resolve().parent.parent
RAW_DATA_DIR = BASE_DIR /"data"/"raw"
PROCESSED_DATA_DIR = BASE_DIR /"data"/"processed"

def load_raw_dataset(file_path: Path)-> pd.DataFrame:
    """Load the raw dataset from a CSV file."""
    return pd.read_csv(file_path, parse_dates=["date"])

def remove_duplicate_rows(dataframe: pd.DataFrame) -> pd.DataFrame:
    """Remove duplicate rows from the DataFrame."""
    return dataframe.drop_duplicates().copy()

def fill_missing_numeric_values(dataframe: pd.DataFrame) -> pd.DataFrame:
    """Fill missing values in numeric columns with the mean."""
    cleaned_dataframe = dataframe.copy()
    numeric_columns = cleaned_dataframe.select_dtypes(include=["number"]).columns
    cleaned_dataframe[numeric_columns] = cleaned_dataframe[numeric_columns].fillna(cleaned_dataframe[numeric_columns].median())
    return cleaned_dataframe