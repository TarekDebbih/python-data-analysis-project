from pathlib import Path


DATA_DIR = Path("data")
RAW_DATA_DIR = DATA_DIR / "raw"
PROCESSED_DATA_DIR = DATA_DIR / "processed"


def create_data_directories() -> None:
    """Create project directories if not already exist."""
    RAW_DATA_DIR.mkdir(parents=True, exist_ok=True)
    PROCESSED_DATA_DIR.mkdir(parents=True, exist_ok=True)

import numpy as np
import pandas as pd


def generate_synthetic_power_demand_data(
    num_days: int = 180,
    random_seed: int = 42,
) -> pd.DataFrame:
    """Generate a synthetic multivariate time series dataset for power demand forecasting."""
    rng = np.random.default_rng(random_seed)

    dates = pd.date_range(start="2024-01-01", periods=num_days, freq="D")
    day_of_year = np.arange(num_days)
    day_of_week = dates.dayofweek

    temperature = 12 + 10 * np.sin(2 * np.pi * day_of_year / 365) + rng.normal(0, 2, num_days)
    humidity = 65 - 0.4 * temperature + rng.normal(0, 5, num_days)

    is_weekend = (day_of_week >= 5).astype(int)
    is_holiday = np.zeros(num_days, dtype=int)

    holiday_indices = rng.choice(num_days, size=max(5, num_days // 30), replace=False)
    is_holiday[holiday_indices] = 1

    base_demand = 300
    yearly_seasonality = 40 * np.cos(2 * np.pi * day_of_year / 365)
    temperature_effect = np.maximum(0, 18 - temperature) * 6 + np.maximum(0, temperature - 22) * 4
    weekend_effect = -35 * is_weekend
    holiday_effect = -50 * is_holiday
    noise = rng.normal(0, 8, num_days)

    power_demand = (
        base_demand
        + yearly_seasonality
        + temperature_effect
        + weekend_effect
        + holiday_effect
        + noise
    )

    return pd.DataFrame(
        {
            "date": dates,
            "temperature": temperature,
            "humidity": humidity,
            "is_weekend": is_weekend,
            "is_holiday": is_holiday,
            "power_demand": power_demand,
        }
    )

def save_dataset_to_csv(dataframe: pd.DataFrame, output_path: Path) -> None:
    """Save a DataFrame to a CSV file."""
    output_path.parent.mkdir(parents=True, exist_ok=True)
    dataframe.to_csv(output_path, index=False)