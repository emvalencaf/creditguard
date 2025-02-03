# CreditGuard- ETL Module - Credit Risk Dataset

## Overview
This module is responsible for extracting, cleaning, transforming, and saving data from the Kaggle dataset: [Credit Risk Dataset](https://www.kaggle.com/datasets/laotse/credit-risk-dataset). It also selects features, normalizes them, saves the scaler model, and stores the processed features and target.

## Project Structure
```
|__ helpers/
|     |__ calc.py
|     |__ datetime_partition.py
|     |__ logging.py
|     |__ makedir.py
|__ config.py
|__ main.py
|__ requirements.txt
```

## Installation
Ensure you have Python installed. Then, install the required dependencies:
```sh
pip install -r requirements.txt
```

## Module Details

### `helpers`
#### `helpers/calc.py`
This module provides functions for mathematical operations:
- `truncate(value: float, decimal_places: int) -> float`: Truncates a float value to the specified decimal places without rounding.
- `calculate_expected_loan_percent(df: pd.DataFrame, decimal_places: int = 2) -> pd.Series`: Computes the expected `loan_percent_income` based on `loan_amnt` and `person_income`.

#### `helpers/datetime_partition.py`
Provides utility functions for timestamp management:
- `get_datetime_partition() -> str`: Returns a directory partition based on the current date (`yyyy/mm/dd`).
- `get_timestamp() -> float`: Returns the current timestamp.

#### `helpers/logging.py`
Handles logging configuration:
- `get_logging() -> logging.Logger`: Configures and returns a logging instance that stores logs in dynamically created directories.

#### `helpers/makedir.py`
Ensures directory existence:
- `ensure_dir(directory: str)`: Creates the specified directory if it does not exist.

### `config.py`
Manages environment configurations using `pydantic_settings`:
- Defines paths for raw, trusted, feature, and target data partitions.
- Sets directories for ML artifacts and logs.

### `main.py`
Executes the ETL process:
1. Loads the dataset from the raw partition.
2. Cleans data inconsistencies:
   - Fixes `loan_percent_income` inconsistencies.
   - Replaces invalid `person_age` values.
3. Transforms categorical data using `OneHotEncoder`.
4. Handles missing values using `KNNImputer`.
5. Saves the trusted dataset.
6. Normalizes numerical features using `StandardScaler`, then saves the scaler model.
7. Selects relevant features and separates the target variable.
8. Saves processed features and target datasets.

## Running the ETL Pipeline
Execute the ETL process by running:
```sh
python main.py
```

## Output Files
- **Trusted dataset**: Saved in `TRUSTED_PARTITION`.
- **Feature set**: Saved in `FEATURE_PARTITION`.
- **Target set**: Saved in `TARGET_PARTITION`.
- **Scaler model**: Stored in `ML_ARTIFACTS_DIRECTORY/utils/scaler.pkl`.

## Logging
Logs are generated dynamically and stored in `LOG_DIRECTORY` following the date-based partition format.

## License
This project is licensed under the MIT License.
