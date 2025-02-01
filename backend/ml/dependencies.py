import pickle
from sklearn.discriminant_analysis import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from config import global_settings

with open(global_settings.MODEL_ARTIFACT_URI, 'rb') as f:
    model = pickle.load(f)

with open(global_settings.SCALER_ARTIFACT_URI, "rb") as f:
    scaler = pickle.load(f)

print("scaler: ", scaler)
print("model: ", model)

# Para o scaler, vamos verificar quais colunas ele espera
if isinstance(scaler, StandardScaler):
    print("Scaler expected columns (features):")
    print(scaler.feature_names_in_)

# Para o modelo, vamos verificar as features que ele espera
if hasattr(model, 'feature_importances_'):
    print("Model expected columns (features):")
    # Exibir as features do modelo
    print(model.feature_names_in_)

def get_model() -> RandomForestClassifier:
    """
    Get model for prediction
    
    :return: Random Forest model
    """
    return model

def get_scaler() -> StandardScaler:
    """
    Get scalar for scale the inference input
    
    :return: StandardScaler model
    """
    return scaler