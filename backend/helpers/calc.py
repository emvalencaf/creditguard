import numpy as np

def truncate(value: float, 
             decimal_places: int) -> float:
    """
    Truncate a value to a specific number of decimal places without rounding.

    :param value: The number to be truncated.
    :param decimal_places: Number of decimal places to keep.
    :return: Truncated float value.
    """
    factor = 10 ** decimal_places
    return np.floor(value * factor) / factor

def get_loan_percent_income(applicant_income: float,
                            loan_amount: float):
    """
    Get the loan percent of the applicant yearly income
    
    :param applicant_income: float number
    :param loan_amount: float number
    :return: loan percent of the applicant yearly income
    """
    loan_percent_income = loan_amount / applicant_income
    
    return truncate(value=loan_percent_income)