import numpy as np
from datetime import datetime

def truncate(value: float, 
             decimal_places: int = 2) -> float:
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

def calculate_age(birthdate: str) -> int:
    """
    Calculate the age of a person based on their birthdate.

    :param birthdate: The birthdate in the format 'YYYY-mm-dd'.
    :return: The person's age as an integer.
    """
    # Convert the birthdate string to a datetime object
    birth_date_obj = datetime.strptime(birthdate, "%Y-%m-%d")
    
    # Get the current date
    current_date = datetime.now()
    
    # Calculate the preliminary age by subtracting the birth year from the current year
    age = current_date.year - birth_date_obj.year
    
    # Adjust the age if the birthday hasn't occurred yet this year
    if (current_date.month, current_date.day) < (birth_date_obj.month, birth_date_obj.day):
        age -= 1
    
    return age