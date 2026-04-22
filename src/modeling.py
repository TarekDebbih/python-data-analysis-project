from pathlib import Path

import pandas as pd


BASE_DIR = Path(__file__).resolve().parent.parent
PROCESSED_DATA_DIR = BASE_DIR / "data" / "processed"


def load_modeling_dataset(file_path: Path) -> pd.DataFrame:
    """Load the cleaned dataset for modeling."""
    return pd.read_csv(file_path, parse_dates=["date"])

def select_features_and_target(dataframe: pd.DataFrame) -> tuple[pd.DataFrame, pd.Series]:
    """Split the dataset into input features and target variable."""
    feature_columns = ["temperature", "humidity", "is_weekend", "is_holiday"]
    target_column = "power_demand"

    X = dataframe[feature_columns].copy()
    y = dataframe[target_column].copy()

    return X, y