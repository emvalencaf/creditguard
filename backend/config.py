from os import getenv
from dotenv import load_dotenv
from pydantic_settings import BaseSettings

load_dotenv()

class GlobalConfig(BaseSettings):
    API_V1_STR:str = '/api/v1'
    
    # backend env vars
    BACKEND_PORT: int = int(getenv('BACKEND_PORT', 8080))
    BACKEND_HOST: str = str(getenv('BACKEND_HOST',
                                   'localhost'))
    
    # environment
    ENVIRONMENT: str = str(getenv("ENVIRONMENT",
                                  "DEVELOPMENT"))
    
    # machine learning model
    MODEL_ARTIFACT_URI: str = str(getenv("MODEL_ARTIFACT_URI",
                                         "../ml/artifacts/models/rf-1.0.0-1738355033.160973.pkl"))
    SCALER_ARTIFACT_URI: str = str(getenv("SCALER_ARTIFACT_URI",
                                          "../ml/artifacts/utils/scaler.pkl"))
    
    # frotend env vars
    FRONTEND_URL: str = str(getenv("FRONTEND_URL",
                                   "http://localhost:8501")) # streamlit app
    
    class Config:
        case_sensitive = True
        
global_settings: GlobalConfig = GlobalConfig()