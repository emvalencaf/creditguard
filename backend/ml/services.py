from sklearn.discriminant_analysis import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from fastapi.encoders import jsonable_encoder

# Project directories
from helpers.prepare_input import prepare_input_for_model
from ml.schemas import LoanApplicationFeaturesSchema, LoanApplicationSchema
from helpers.calc import get_loan_percent_income

def get_default_prediction(loan_application: LoanApplicationSchema,
                                 model:RandomForestClassifier,
                                 scaler: StandardScaler):
    """
    Get default prediction if true, the applicant will must likely default.
    :param loan_application:
    :param model:
    :param scaler:
    :return: boolean value
    """
    loan_percent_income = get_loan_percent_income(loan_amount=loan_application.loan_amount,
                                                  applicant_income=loan_application.applicant_yearly_income)

    loan_application_features = LoanApplicationFeaturesSchema(**loan_application.model_dump(),
                                                              loan_percent_income=loan_percent_income)
    
    input = prepare_input_for_model(loan_application=loan_application_features,
                               scaler=scaler)
    
    prediction = model.predict(input)
    
    return prediction[0]