import pandas as pd
import numpy as np

def truncate(value: float, decimal_places: int) -> float:
    """
    Truncate a value to a specific number of decimal places without rounding.

    :param value: The number to be truncated.
    :param decimal_places: Number of decimal places to keep.
    :return: Truncated float value.
    """
    factor = 10 ** decimal_places
    return np.floor(value * factor) / factor

def calculate_expected_loan_percent(df: pd.DataFrame, decimal_places: int = 2) -> pd.Series:
    """
    Calculate the expected `loan_percent_income` based on `loan_amnt` and `person_income`.

    :param df: Pandas DataFrame containing `loan_amnt` and `person_income`.
    :param decimal_places: Number of decimal places to keep in the calculation.
    :return: A Pandas Series with the expected `loan_percent_income` values.
    """
    expected_loan_percent = df['loan_amnt'] / df['person_income']
    
    return expected_loan_percent.apply(lambda x: truncate(x, decimal_places))