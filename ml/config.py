from os import getenv
from pydantic_settings import BaseSettings

class MachineLearningConfig(BaseSettings):

    FEATURE_PARTITION:str = getenv("FEATURE_PARTITION",
                                   "../dataset/features/*/*/*/feature-*.csv")
    
    TARGET_PARTITION:str = getenv("TARGET_PARTITION",
                                  "../dataset/features/*/*/*/target-*.csv")
    
    MODEL_PARTITION:str = getenv('MODEL_PARTITION',
                                 "./artifacts/models")
    MODEL_ALG:str = getenv('MODEL_ALG',
                           'rf')
    MODEL_VERSION:str = getenv('MODEL_VERSION',
                               '1.0.0')
    LOG_DIRECTORY:str = getenv("LOG_DIRECTORY",
                               "../dataset/logs/training")
    class Config:
        case_sensitive = True
        
ml_settings: MachineLearningConfig = MachineLearningConfig()