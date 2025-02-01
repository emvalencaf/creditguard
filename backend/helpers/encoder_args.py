from typing import Dict


def encode_loan_grade(loan_grade: str) -> Dict[str, int]:
    """
    Encodes the loan grade into a one-hot encoded dictionary.
    
    :param loan_grade: The loan grade (risk classification)
    :return: A dictionary with one-hot encoded loan grade features
    """
    grades = ["A", "B", "C", "D", "E", "F", "G"]
    return {f"loan_grade_{g}": int(loan_grade == g) for g in grades}


def encode_loan_intent(loan_intent: str) -> Dict[str, int]:
    """
    Encodes the loan intent into a one-hot encoded dictionary.
    
    :param loan_intent: The applicant's intended use of the loan
    :return: A dictionary with one-hot encoded loan intent features
    """
    intents = ["Education", "Home Improvement", "Medical", "Personal", "Venture"]
    return {f"loan_intent_{intent.upper().replace(' ', '')}": int(loan_intent == intent) for intent in intents}


def encode_default_history(default_history: str) -> int:
    """
    Encodes the default history of the applicant as a binary value.
    
    :param default_history: "Yes" if the applicant has a default history, otherwise "No"
    :return: 1 if the applicant has a default history, 0 if not
    """
    return int(default_history == "Yes")