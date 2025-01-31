from helpers.logging import get_logging

logging = get_logging()

def get_hyperparameters() -> dict:
    """
    Returns the hyperparameters for the RandomForestClassifier.
    
    :returns:Dictionary containing hyperparameter settings.
    """
    logging.info("Retrieving hyperparameters for the model.")
    return {
        'max_depth': None,
        'max_features': 'sqrt',
        'min_samples_leaf': 1,
        'min_samples_split': 2,
        'n_estimators': 150
    }