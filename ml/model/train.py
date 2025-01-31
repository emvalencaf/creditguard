import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import confusion_matrix, classification_report



# Project dependencies
from model.hyperparameters import get_hyperparameters
from helpers.split_train_data import get_training_data
from helpers.logging import get_logging
from features.data import get_features, get_target
from plot.cm import plot_confusion_matrix

logging = get_logging()

def training_model() -> tuple[RandomForestClassifier, 
                              pd.DataFrame, pd.Series]:
    """
    Trains a RandomForestClassifier model, evaluates it, and logs the process.
    
    :returns:Tuple containing the trained model, test feature set, and test target labels.
    """
    try:
        logging.info("Starting training process.")
        features = get_features()
        target = get_target()
        
        logging.info("Features and target loaded successfully.")
        X_train, X_test, y_train, y_test = get_training_data(features, 
                                                             target)
        
        hyperparameters = get_hyperparameters()
        model = RandomForestClassifier(**hyperparameters)
        logging.info("Configure model's hyperparameters.")
        logging.info(f"Model's hyperparameters:\n{hyperparameters}")
        
        logging.info("Training RandomForest model.")
        model.fit(X_train, y_train)
        logging.info("Model training completed successfully.")
        
        y_pred_model = model.predict(X_test)
        
        cm_model = confusion_matrix(y_test,
                                    y_pred_model)
        
        logging.info("Generating confusion matrix plot.")
        plot_confusion_matrix(cm=cm_model, 
                              model_name="Random Forest - CreditGuard")
        logging.info("Confusion matrix plot saved.")
        
        logging.info("Model evaluation report:")
        report = classification_report(y_test, 
                                       y_pred_model)
        logging.info(f"\n{report}")
        
        return model, X_test, y_test
    except Exception as e:
        logging.error(f"Error in model training process: {e}")
        raise