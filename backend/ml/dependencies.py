from fastapi import Request
from sklearn.discriminant_analysis import StandardScaler
from sklearn.ensemble import RandomForestClassifier

def get_model(request: Request) -> RandomForestClassifier:
    """
    Get model for prediction
    
    :return: Random Forest model
    """
    return request.app.state.ml_model

def get_scaler(request: Request) -> StandardScaler:
    """
    Get scalar for scale the inference input
    
    :return: StandardScaler model
    """

    return request.app.state.scaler_model 