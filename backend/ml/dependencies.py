from sklearn.discriminant_analysis import StandardScaler
from sklearn.ensemble import RandomForestClassifier

from lifespan import ml_model, scaler_model

def get_model() -> RandomForestClassifier:
    """
    Get model for prediction
    
    :return: Random Forest model
    """
    print("model: ",ml_model)
    
    return ml_model

def get_scaler() -> StandardScaler:
    """
    Get scalar for scale the inference input
    
    :return: StandardScaler model
    """
    print("scaler: ",scaler_model)
    
    return scaler_model