import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import confusion_matrix, classification_report



# Project dependencies
from model.hyperparameters import get_hyperparameters
from helpers.split_train_data import get_training_data
from helpers.logging import ml_logging
from features.data import get_features, get_target
from plot.cm import plot_confusion_matrix

def training_model() -> tuple[RandomForestClassifier, 
                              pd.DataFrame, pd.Series]:
    """
    Trains a RandomForestClassifier model, evaluates it, and logs the process.
    
    :returns:Tuple containing the trained model, test feature set, and test target labels.
    """
    try:
        ml_logging.info("Starting training process.")
        features = get_features()
        target = get_target()
        
        ml_logging.info("Features and target loaded successfully.")
        X_train, X_test, y_train, y_test = get_training_data(features, 
                                                             target)
        
        hyperparameters = get_hyperparameters()
        model = RandomForestClassifier(**hyperparameters)
        ml_logging.info("Configure model's hyperparameters.")
        ml_logging.info(f"Model's hyperparameters:\n{hyperparameters}")
        
        ml_logging.info("Training RandomForest model.")
        model.fit(X_train, y_train)
        ml_logging.info("Model training completed successfully.")
        
        y_pred_model = model.predict(X_test)
        
        cm_model = confusion_matrix(y_test,
                                    y_pred_model)
        
        ml_logging.info("Generating confusion matrix plot.")
        plot_confusion_matrix(cm=cm_model, 
                              model_name="Random Forest - CreditGuard")
        ml_logging.info("Confusion matrix plot saved.")
        
        ml_logging.info("Model evaluation report:")
        report = classification_report(y_test, 
                                       y_pred_model)
        ml_logging.info(f"\n{report}")
        
        return model, X_test, y_test
    except Exception as e:
        ml_logging.error(f"Error in model training process: {e}")
        raise