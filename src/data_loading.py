from pathlib import Path

import pandas as pd


BASE_DIR = Path(__file__).resolve().parent.parent
RAW_DATA_DIR = BASE_DIR / "data" / "raw"


def load_power_demand_dataset(file_path: Path) -> pd.DataFrame:
    """Load the power demand dataset from a CSV file."""
    return pd.read_csv(file_path, parse_dates=["date"])