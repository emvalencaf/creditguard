from pickle import dump
from datetime import datetime

# Project directories
from helpers.logging import ml_logging
from config import ml_settings
from helpers.makedir import ensure_dir

def save_model(model,
               model_alg: str,
               model_version: str = '1.0.0'):
    """
    Save model as artifact for later inference
    
    :param model:
    :param model_alg:
    :param model_version:
    """
    model_dir = ml_settings.MODEL_PARTITION
    ensure_dir(directory=model_dir)
    
    ml_logging.info(f"Saving model {model_alg} version {model_version} at {model_dir}...")
    timestamp = datetime.now().timestamp()
    
    filename = f'{model_alg}-{model_version}-{timestamp}.pkl'
    
    filepath = f'{model_dir}/{filename}'
    
    with open(filepath, 'wb') as f:
        dump(model, f)
        
    ml_logging.info(f"Model {filepath} was successfully saved")
    
    return filepath
 
