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
    
    # frotend env vars
    FRONTEND_URL: str = str(getenv("FRONTEND_URL",
                                   "http://localhost:8501")) # streamlit app
    
    class Config:
        case_sensitive = True
        
global_settings: GlobalConfig = GlobalConfig()