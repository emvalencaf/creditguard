from sklearn.model_selection import train_test_split
import pandas as pd
from imblearn.over_sampling import SMOTE

# Project dependencies
from helpers.logging import get_logging

logging = get_logging()

def get_smote_data(X_train: pd.DataFrame, 
                   y_train: pd.Series) -> tuple[pd.DataFrame, pd.Series]:
    """
    Applies SMOTE (Synthetic Minority Over-sampling Technique) to balance the dataset.

    :param X_train: Training feature set.
    :param y_train: Training target labels.
    :return: Tuple containing resampled training features and target labels.
    """
    logging.info("Checking class distribution before applying SMOTE.")
    class_counts = y_train.value_counts()
    logging.info(f"Class distribution before SMOTE:\n{class_counts}")
    
    y_train = y_train.values.ravel()

    if class_counts.min() / class_counts.max() >= 0.8:
        logging.info("Dataset is already balanced. Skipping SMOTE.")
        return X_train, y_train

    try:
        logging.info("Applying SMOTE to balance dataset.")
        
        smote = SMOTE(random_state=42)
        
        X_train_resampled, y_train_resampled = smote.fit_resample(X_train, y_train)
        print(f"Class distribution after SMOTE:\n{pd.Series(y_train_resampled).value_counts()}")
        
        logging.info("SMOTE applied successfully.")
        
        return X_train_resampled, y_train_resampled

    except Exception as e:
        logging.error(f"Error while applying SMOTE: {e}")
        
        return X_train, y_train  # Retorna os dados originais em caso de erro

def get_training_data(features: pd.DataFrame,
                      target: pd.Series) -> tuple[pd.DataFrame, pd.DataFrame, pd.Series, pd.Series]:
    """
    Splits dataset into training and testing sets, and applies SMOTE to balance training data.

    :param features: Feature set.
    :param target: Target labels.
    :return: Tuple containing resampled training features, test features, resampled training labels, and test labels.
    """
    logging.info("Splitting dataset into training and testing sets.")
    target = target.round().astype(int)
    logging.info(f'Features size: {features.shape}')
    logging.info(f"Target size:{target.shape}")
    
    try:
        X_train, X_test, y_train, y_test = train_test_split(features, target,
                                                            test_size=0.2, random_state=42)
        logging.info(f"Training set size: {X_train.shape[0]}, Test set size: {X_test.shape[0]}")
    except Exception as e:
        logging.error(f"Error during train-test split: {e}")
        raise 
    logging.info(f"X_train size:\n{X_train.shape}")
    logging.info(f"Y_train size:\n{y_train.shape}")

    logging.info(f"Features cols:\n{X_train.columns.tolist()}")
    logging.info(f"Features cols datatype:\n{X_train.dtypes}")

    X_train_resampled, y_train_resampled = get_smote_data(X_train, y_train)

    return X_train_resampled, X_test, y_train_resampled, y_test
