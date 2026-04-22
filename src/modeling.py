from pathlib import Path
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
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