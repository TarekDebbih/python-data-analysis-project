from pathlib import Path
import pandas as pd

BASE_DIR = Path(__file__).resolve().parent.parent
PROCESSED_DATA_DIR = BASE_DIR / "data" / "processed"

def load_cleaned_dataset(file_path: Path) -> pd.DataFrame:
    """Load the cleaned dataset from a CSV file."""
    return pd.read_csv(file_path, parse_dates=["date"])

def summarize_numeric_columns(dataframe: pd.DataFrame) -> pd.DataFrame:
    """Return descriptive statistics for numeric columns only."""
    numeric_dataframe = dataframe.select_dtypes(include=["number"])
    return numeric_dataframe.describe()

def compute_correlation_matrix(dataframe: pd.DataFrame) -> pd.DataFrame:
    """Compute correlations between numeric columns."""
    numeric_dataframe = dataframe.select_dtypes(include=["number"])
    return numeric_dataframe.corr()

def main() -> None:
    """Load the cleaned dataset and display descriptive statistics."""
    file_path = PROCESSED_DATA_DIR / "clean_power_demand.csv"
    dataset = load_cleaned_dataset(file_path)

    summary = summarize_numeric_columns(dataset)
    print(summary)


if __name__ == "__main__":
    main()
