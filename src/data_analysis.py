from pathlib import Path
import pandas as pd

BASE_DIR = Path(__file__).resolve().parent.parent
PROCESSED_DATA_DIR = BASE_DIR / "data" / "processed"

def load_cleaned_dataset(file_path: Path) -> pd.DataFrame:
    """Load the cleaned dataset from a CSV file."""
    return pd.read_csv(file_path, parse_dates=["date"])

def summarize_dataset(dataframe: pd.DataFrame) -> pd.DataFrame:
    """generate descriptive statistics for the numeric columns"""
    return dataframe;describe()