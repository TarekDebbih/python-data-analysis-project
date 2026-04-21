from pathlib import Path

import pandas as pd


BASE_DIR = Path(__file__).resolve().parent.parent
RAW_DATA_DIR = BASE_DIR / "data" / "raw"


def load_power_demand_dataset(file_path: Path) -> pd.DataFrame:
    """Load the power demand dataset from a CSV file."""
    return pd.read_csv(file_path, parse_dates=["date"])

def main() -> None:
    """Load and display basic information about the power demand dataset."""
    file_path = RAW_DATA_DIR / "synthetic_power_demand.csv"
    dataset = load_power_demand_dataset(file_path)

    print(dataset.head())
    print()
    dataset.info()


if __name__ == "__main__":
    main()