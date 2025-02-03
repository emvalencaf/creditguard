from pydantic_settings import BaseSettings
from os import getenv

class ETLConfig(BaseSettings):
    DB_URL: str = getenv("DB_URL",
                         "postgresql+psycopg2://postgres:root@localhost/postgres")
    RAW_PARTITION: str = getenv("RAW_PARTITION",
                                "../dataset/raw/credit_risk_dataset.csv")
    TRUSTED_PARTITION:str = getenv("TRUSTED_PARTITION",
                                   "../dataset/trusted")
    FEATURE_PARTITION:str = getenv("FEATURE_PARTITION",
                                   "../dataset/features")
    
    TARGET_PARTITION:str = getenv("TARGET_PARTITION",
                                  "../dataset/features")
    
    ML_ARTIFACTS_DIRECTORY: str = getenv("ML_ARTIFACTS_DIRECTORY",
                                         "../ml/artifacts")
    
    LOG_DIRECTORY:str = getenv("LOG_DIRECTORY",
                               "../dataset/logs/etl")
    class Config:
        case_sensitive = True
        
etl_settings: ETLConfig = ETLConfig()