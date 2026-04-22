from pathlib import Path
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import pandas as pd
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score


BASE_DIR = Path(__file__).resolve().parent.parent
PROCESSED_DATA_DIR = BASE_DIR / "data" / "processed"


def load_modeling_dataset(file_path: Path) -> pd.DataFrame:
    """Load the cleaned dataset for modeling."""
    return pd.read_csv(file_path, parse_dates=["date"])

def select_features_and_target(dataframe: pd.DataFrame) -> tuple[pd.DataFrame, pd.Series]:
    """Split the dataset into input features and target variable."""
    feature_columns = [
    "temperature",
    "humidity",
    "is_weekend",
    "is_holiday",
    "month",
    "day_of_year",
]
    target_column = "power_demand"

    X = dataframe[feature_columns].copy()
    y = dataframe[target_column].copy()

    return X, y

def split_train_test(
    X: pd.DataFrame,
    y: pd.Series,
    test_size: float = 0.2,
    random_seed: int = 42,
) -> tuple[pd.DataFrame, pd.DataFrame, pd.Series, pd.Series]:
    """Split features and target into training and testing sets."""
    return train_test_split(X, y, test_size=test_size, random_state=random_seed)

def train_linear_regression_model(
    X_train: pd.DataFrame,
    y_train: pd.Series,
) -> LinearRegression:
    """Train a linear regression model on the training data."""
    model = LinearRegression()
    model.fit(X_train, y_train)
    return model

def predict_with_model(
    model: LinearRegression,
    X_test: pd.DataFrame,
) -> pd.Series:
    """Generate predictions from the trained model."""
    predictions = model.predict(X_test)
    return pd.Series(predictions, index=X_test.index, name="predicted_power_demand")

def evaluate_regression_model(
    y_true: pd.Series,
    y_pred: pd.Series,
) -> dict[str, float]:
    """Compute basic regression evaluation metrics."""
    mae = mean_absolute_error(y_true, y_pred)
    mse = mean_squared_error(y_true, y_pred)
    rmse = mse ** 0.5
    r2 = r2_score(y_true, y_pred)

    return {
        "mae": mae,
        "mse": mse,
        "rmse": rmse,
        "r2": r2,
    }

def add_time_features(dataframe: pd.DataFrame) -> pd.DataFrame:
    """Add simple time-based features for modeling."""
    enriched_dataframe = dataframe.copy()
    enriched_dataframe["month"] = enriched_dataframe["date"].dt.month
    enriched_dataframe["day_of_year"] = enriched_dataframe["date"].dt.dayofyear
    return enriched_dataframe

def main() -> None:
    """Run the full modeling pipeline."""
    file_path = PROCESSED_DATA_DIR / "clean_power_demand.csv"
    dataset = load_modeling_dataset(file_path)
    dataset = add_time_features(dataset)

    X, y = select_features_and_target(dataset)
    X_train, X_test, y_train, y_test = split_train_test(X, y)

    model = train_linear_regression_model(X_train, y_train)
    y_pred = predict_with_model(model, X_test)

    metrics = evaluate_regression_model(y_test, y_pred)

    print("Model evaluation metrics:")
    for metric_name, metric_value in metrics.items():
        print(f"{metric_name}: {metric_value:.4f}")


if __name__ == "__main__":
    main()