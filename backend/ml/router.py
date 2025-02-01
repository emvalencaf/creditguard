from fastapi import APIRouter, Depends
from sklearn.discriminant_analysis import StandardScaler
from sklearn.ensemble import RandomForestClassifier

# Project directories
from ml.dependencies import get_model, get_scaler
from ml.schemas import LoanApplicationSchema
from ml.services import get_default_prediction

router = APIRouter(tags=['machine learning',
                         'artificial intelligence',
                         'ml', 'ai'])

@router.post('/loan_default')
def predict_default(loan_application: LoanApplicationSchema,
                          model: RandomForestClassifier = Depends(get_model),
                          scaler: StandardScaler = Depends(get_scaler)):
    """
    Predict if loan application will result in a default
    """
    
    prediction = get_default_prediction(model=model,
                                        loan_application=loan_application,
                                        scaler=scaler)
    
    return {
        "prediction": bool(prediction)
        }