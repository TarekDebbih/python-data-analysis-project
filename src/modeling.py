from pathlib import Path

import pandas as pd


BASE_DIR = Path(__file__).resolve().parent.parent
PROCESSED_DATA_DIR = BASE_DIR / "data" / "processed"


def load_modeling_dataset(file_path: Path) -> pd.DataFrame:
    """Load the cleaned dataset for modeling."""
    return pd.read_csv(file_path, parse_dates=["date"])