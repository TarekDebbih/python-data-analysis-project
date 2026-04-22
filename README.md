# Python Power Demand Forecasting Project

## Project Overview
This project focuses on the simulation, analysis, and forecasting of electric power demand using Python.

The workflow includes:
- synthetic multivariate time series data generation
- data cleaning and preprocessing
- exploratory data analysis
- baseline forecasting with linear regression
- model evaluation and comparison of predictions

## Project Structure
- `src/data_generation.py`: generates the synthetic dataset
- `src/data_cleaning.py`: cleans and saves the processed dataset
- `src/data_analysis.py`: computes statistics, correlations, and plots
- `src/modeling.py`: trains and evaluates the forecasting model
- `data/raw/`: raw generated data
- `data/processed/`: cleaned data
- `outputs/figures/`: generated plots
- `outputs/reports/`: prediction comparison reports

## Technologies Used
- Python
- Pandas
- NumPy
- Matplotlib
- scikit-learn

## Methodology
The project follows a simple end-to-end forecasting workflow:

1. Generate a synthetic multivariate dataset related to electric power demand.
2. Clean and preprocess the dataset.
3. Explore the data with descriptive statistics, correlations, and visualizations.
4. Train a baseline linear regression model.
5. Evaluate predictions with regression metrics such as MAE, RMSE, and R².
6. Improve the model by adding a relevant time-based feature (`day_of_year`).

## Key Results
The baseline model was improved by adding a time-based feature to better capture seasonality.

Improved model results:
- MAE: 11.3016
- MSE: 180.8438
- RMSE: 13.4478
- R²: 0.8571

## How to Run the Project

### 1. Create and activate a virtual environment

```bash
python3 -m venv .venv
source .venv/bin/activate

python3 -m pip install -r requirements.txt
python3 src/data_generation.py
python3 src/data_cleaning.py
python3 src/data_analysis.py
python3 src/modeling.py
```