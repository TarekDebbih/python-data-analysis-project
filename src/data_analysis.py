from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

BASE_DIR = Path(__file__).resolve().parent.parent
PROCESSED_DATA_DIR = BASE_DIR / "data" / "processed"

def load_cleaned_dataset(file_path: Path) -> pd.DataFrame:
    """Load the cleaned dataset from a CSV file."""
    # Load the cleaned CSV file into a pandas DataFrame.
    # Parse the "date" column as real dates.
    return pd.read_csv(file_path, parse_dates=["date"])

def summarize_numeric_columns(dataframe: pd.DataFrame) -> pd.DataFrame:
    """Return descriptive statistics for numeric columns only."""
    # Keep only numeric columns and return basic statistics.
    numeric_dataframe = dataframe.select_dtypes(include=["number"])
    return numeric_dataframe.describe()

def compute_correlation_matrix(dataframe: pd.DataFrame) -> pd.DataFrame:
    """Compute correlations between numeric columns."""
    # Compute correlations between numeric features.
    numeric_dataframe = dataframe.select_dtypes(include=["number"])
    return numeric_dataframe.corr()

def plot_power_demand_over_time(dataframe: pd.DataFrame) -> None:
    """Plot power demand over time."""
    plt.figure(figsize=(10, 5))
    plt.plot(dataframe["date"], dataframe["power_demand"])
    plt.title("Power Demand Over Time")
    plt.xlabel("Date")
    plt.ylabel("Power Demand")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def plot_temperature_vs_power_demand(dataframe: pd.DataFrame) -> None:
    """Plot temperature against power demand."""
    plt.figure(figsize=(8, 5))
    plt.scatter(dataframe["temperature"], dataframe["power_demand"])
    plt.title("Temperature vs Power Demand")
    plt.xlabel("Temperature")
    plt.ylabel("Power Demand")
    plt.tight_layout()
    plt.show()

def main() -> None:
    """Load the cleaned dataset and display descriptive statistics."""
    # Main analysis flow:
    # load the dataset, show statistics, then show correlations.
    file_path = PROCESSED_DATA_DIR / "clean_power_demand.csv"
    dataset = load_cleaned_dataset(file_path)

    summary = summarize_numeric_columns(dataset)
    print(summary)

    correlation_matrix = compute_correlation_matrix(dataset)
    print()
    print(correlation_matrix)

    plot_power_demand_over_time(dataset)


if __name__ == "__main__":
    main()