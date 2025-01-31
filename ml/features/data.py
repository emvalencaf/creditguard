import pandas as pd

from config import ml_settings

def get_features()-> pd.DataFrame:
    """
    Get features data from dataset
    
    :return: pandas dataframe
    """
    return pd.read_csv(f"{ml_settings.FEATURE_PARTITION}/feature.csv")

def get_target() -> pd.DataFrame:
    """
    Get target data from dataset
    
    :return: pandas dataframe
    """
    return pd.read_csv(f"{ml_settings.TARGET_PARTITION}/target.csv")