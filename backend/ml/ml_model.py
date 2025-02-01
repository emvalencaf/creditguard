from os.path import join, exists
from pickle import load
from sklearn.discriminant_analysis import StandardScaler
from sklearn.ensemble import RandomForestClassifier

# Project directories
from config import global_settings
from helpers.download_file import download_google_drive_file, REMOTE_MODEL_FOLDER
from helpers.makedir import ensure_dir

async def load_ml_model() -> RandomForestClassifier:
    """
    Loads the machine learning model from a local file or Google Drive.

    :return: A trained RandomForestClassifier model.
    """
    ensure_dir(directory=REMOTE_MODEL_FOLDER)
    
    remote_model_path = join(REMOTE_MODEL_FOLDER, "model.pkl")

    if global_settings.ENVIRONMENT == "PRODUCTION":
        if not exists(remote_model_path):
            print(f"Model not found locally. Downloading from Google Drive...")
            remote_model_path = await download_google_drive_file(global_settings.MODEL_ARTIFACT_URI,
                                                                "model.pkl")
        
        return load(open(remote_model_path,'rb'))

    print("remote model path: ", remote_model_path)
    # For DEVELOPMENT(local) environment MODEL_ARTIFACT_URI will be the path for the file in your machine
    # For PRODUCTION environment MODEL_ARTIFACT_URI will be the object id in the google drive
    # So it needs to find the uri of the model in the deployed web server
    return load(open(global_settings.MODEL_ARTIFACT_URI,'rb'))

async def load_scaler_model() -> StandardScaler:
    """
    Loads the scaler model from a local file or Cloudinary storage.

    :return: A trained StandardScaler object.
    """
    ensure_dir(directory=REMOTE_MODEL_FOLDER)
    
    remote_model_path = join(REMOTE_MODEL_FOLDER, "scaler.pkl")

    if global_settings.ENVIRONMENT == "PRODUCTION":
        if not exists(remote_model_path):
            print(f"Model not found locally. Downloading from Google Drive...")
            remote_model_path = await download_google_drive_file(global_settings.SCALER_ARTIFACT_URI,
                                                                "scaler.pkl")
        
        return load(open(remote_model_path,'rb'))

    print("remote scaler path: ", remote_model_path)

    # For DEVELOPMENT(local) environment SCALER_ARTIFACT_URI will be the path for the file in your machine
    # For PRODUCTION environment SCALER_ARTIFACT_URI will be the object id in the google drive
    # So it needs to find the uri of the scaler in the deployed web server
    return load(open(global_settings.SCALER_ARTIFACT_URI,'rb'))