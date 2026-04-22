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