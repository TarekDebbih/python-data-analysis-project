from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

BASE_DIR = Path(__file__).resolve().parent.parent
PROCESSED_DATA_DIR = BASE_DIR / "data" / "processed"
OUTPUT_FIGURES_DIR = BASE_DIR / "outputs" / "figures"

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

def save_current_figure(filename: str) -> None:
    """Save the current matplotlib figure to the outputs/figures directory."""
    OUTPUT_FIGURES_DIR.mkdir(parents=True, exist_ok=True)
    plt.tight_layout()
    plt.savefig(OUTPUT_FIGURES_DIR / filename)
    plt.close()

def plot_power_demand_over_time(dataframe: pd.DataFrame) -> None:
    """Plot power demand over time."""
    plt.figure(figsize=(10, 5))
    plt.plot(dataframe["date"], dataframe["power_demand"])
    plt.title("Power Demand Over Time")
    plt.xlabel("Date")
    plt.ylabel("Power Demand")
    plt.xticks(rotation=45)
    save_current_figure("power_demand_over_time.png")

def plot_temperature_vs_power_demand(dataframe: pd.DataFrame) -> None:
    """Plot temperature against power demand."""
    plt.figure(figsize=(8, 5))
    plt.scatter(dataframe["temperature"], dataframe["power_demand"])
    plt.title("Temperature vs Power Demand")
    plt.xlabel("Temperature")
    plt.ylabel("Power Demand")
    save_current_figure("temperature_vs_power_demand.png")

def plot_average_power_demand_by_temperature(dataframe: pd.DataFrame) -> None:
    """Plot average power demand by rounded temperature."""
    temperature_summary = (
        dataframe.assign(rounded_temperature=dataframe["temperature"].round())
        .groupby("rounded_temperature", as_index=False)["power_demand"]
        .mean()
    )

    plt.figure(figsize=(8, 5))
    plt.plot(
        temperature_summary["rounded_temperature"],
        temperature_summary["power_demand"],
    )
    plt.title("Average Power Demand by Temperature")
    plt.xlabel("Rounded Temperature")
    plt.ylabel("Average Power Demand")
    save_current_figure("average_power_demand_by_temperature.png")

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
    plot_temperature_vs_power_demand(dataset)
    plot_average_power_demand_by_temperature(dataset)

if __name__ == "__main__":
    main()