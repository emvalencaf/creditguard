from os import getenv
from typing import List, Optional
from dotenv import load_dotenv
from pydantic_settings import BaseSettings

load_dotenv()

class GlobalConfig(BaseSettings):
    API_V_STR:str = '/api/v1'
    
    # Db envs vars
    DB_URL: str = str(getenv('DB_URL',
                             "localhost:5432/creditguard_db"))  
    
    # environment
    ENVIRONMENT: str = str(getenv("ENVIRONMENT",
                                  "DEVELOPMENT"))
    
    # Cloud env vars (prod env only)
    GOOGLE_API_PROJECT_ID: Optional[str] = getenv("GOOGLE_API_PROJECT_ID")
    GOOGLE_API_SERVICE_ID: Optional[str] = getenv("GOOGLE_API_SERVICE_ID")
    GOOGLE_API_SERVICE_EMAIL:Optional[str] = getenv("GOOGLE_API_SERVICE_EMAIL")
    GOOGLE_API_SERVICE_PRIVATE_KEY_ID:Optional[str] = getenv("GOOGLE_API_SERVICE_PRIVATE_KEY_ID")
    GOOGLE_API_SERVICE_PRIVATE_KEY:Optional[str] = getenv("GOOGLE_API_SERVICE_PRIVATE_KEY")
    
    if ENVIRONMENT == "PRODUCTION" and not (GOOGLE_API_SERVICE_EMAIL and
                                            GOOGLE_API_SERVICE_PRIVATE_KEY_ID and
                                            GOOGLE_API_SERVICE_PRIVATE_KEY and
                                            GOOGLE_API_PROJECT_ID and
                                            GOOGLE_API_SERVICE_ID):
        raise ValueError('In production environment you must provide your google credentials: service id, project id, service email,service secret key id and service secret key. Consulting the documentation.')
    
    # backend env vars
    BACKEND_PORT: int = int(getenv('BACKEND_PORT', 8080))
    BACKEND_HOST: str = str(getenv('BACKEND_HOST',
                                   'localhost'))
    
    # machine learning model
    MODEL_ARTIFACT_URI: str = str(getenv("MODEL_ARTIFACT_URI",
                                         "../ml/artifacts/models/rf-1.0.0-*.pkl"))
    SCALER_ARTIFACT_URI: str = str(getenv("SCALER_ARTIFACT_URI",
                                          "../ml/artifacts/utils/scaler.pkl"))
    
    # frotend env vars
    FRONTEND_URL: str = str(getenv("FRONTEND_URL",
                                   "http://localhost:8501")) # streamlit app
    
    class Config:
        case_sensitive = True
        
global_settings: GlobalConfig = GlobalConfig()