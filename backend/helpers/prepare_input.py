
import pandas as pd
from sklearn.discriminant_analysis import StandardScaler


from ml.schemas import LoanApplicationFeaturesSchema
from helpers.calc import calculate_age
from helpers.encoder_args import encode_default_history, encode_loan_grade, encode_loan_intent


def prepare_input_for_model(loan_application: LoanApplicationFeaturesSchema,
                            scaler: StandardScaler) -> pd.DataFrame:
    """
    Prepares the input data for the model in DataFrame format.
    :param loan_application: The loan application details.
    :param scaler: The trained StandardScaler instance.
    :return: A DataFrame with the features formatted correctly for the model.
    """
    
    # Dictionary with features the model expects
    loan_grade_dict = encode_loan_grade(loan_application.loan_grade)
    loan_intent_dict = encode_loan_intent(loan_application.applicant_loan_intent)
    default_history = encode_default_history(loan_application.applicant_has_default_history)
    person_age = calculate_age(loan_application.applicant_birthdate)
    
    # List of numerical features expected by the model
    numerical_values_name = ['person_age', 'person_income', 
                             'loan_amnt', 'loan_int_rate',
                             'loan_percent_income', 'person_emp_length']
    
    # Numerical feature values to be scaled
    numerical_values = {
        'person_age': person_age,
        'person_income': loan_application.applicant_yearly_income,
        'loan_amnt': loan_application.loan_amount,
        'loan_int_rate': loan_application.loan_int_rate,
        'loan_percent_income': loan_application.loan_percent_income,
        'person_emp_length': loan_application.applicant_employement_hist
    }
    
    # Create a DataFrame with the numerical values to apply scaling
    numerical_values_df = pd.DataFrame([numerical_values], columns=numerical_values_name)
    
    # Scale the numerical values using the provided StandardScaler
    scaled_values = scaler.transform(numerical_values_df)
    
    # Map the scaled values into the input dictionary
    # Use the feature names that the model expects
    mapped_scaled_values = dict(zip(numerical_values_name, scaled_values[0]))
    
    # Construct the input dictionary with all necessary features
    input_dict = {
        **loan_grade_dict,  # One-hot encoded loan_grade columns
        **mapped_scaled_values,  # Mapped scaled numerical values
        'cb_person_default_on_file_Y': default_history,
        **loan_intent_dict,  # One-hot encoded loan_intent columns
    }
    
    # List of feature names expected by the model in the same order
    feature_names = [
        'loan_grade_A', 'loan_grade_B', 'loan_grade_C', 'loan_grade_D', 'loan_grade_E', 'loan_grade_F', 'loan_grade_G',
        'loan_amnt', 'loan_int_rate', 'loan_percent_income', 'cb_person_default_on_file_Y',
        'loan_intent_EDUCATION', 'loan_intent_HOMEIMPROVEMENT', 'loan_intent_MEDICAL', 'loan_intent_PERSONAL', 'loan_intent_VENTURE',
        'person_emp_length'
    ]
    
    # Ensure the input dictionary is in the same order as the model expects
    input_df = pd.DataFrame([input_dict], columns=feature_names)
    
    return input_df