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


def generate_synthetic_time_series_data(
    num_days: int = 180,
    random_seed: int = 42,
) -> pd.DataFrame:
    """Generate a synthetic multivariate time series dataset."""
    rng = np.random.default_rng(random_seed)

    dates = pd.date_range(start="2024-01-01", periods=num_days, freq="D")
    trend = np.linspace(50, 80, num_days)
    seasonality = 10 * np.sin(np.linspace(0, 3 * np.pi, num_days))
    noise = rng.normal(loc=0, scale=3, size=num_days)

    marketing_spend = rng.normal(loc=1000, scale=120, size=num_days)
    website_visits = 200 + 0.4 * marketing_spend + rng.normal(loc=0, scale=25, size=num_days)
    temperature = 15 + 10 * np.sin(np.linspace(0, 2 * np.pi, num_days)) + rng.normal(loc=0, scale=2, size=num_days)

    sales = trend + seasonality + 0.015 * marketing_spend + 0.05 * website_visits + noise

    return pd.DataFrame(
        {
            "date": dates,
            "marketing_spend": marketing_spend,
            "website_visits": website_visits,
            "temperature": temperature,
            "sales": sales,
        }
    )