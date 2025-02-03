from db.client import get_db
from db.respository import create_model, get_model_by_id
from model.train import training_model
from helpers.save_file import save_model
from helpers.model_testing import evaluate_model
from config import ml_settings
from db.schemas import ModelBase
from model.hyperparameters import get_hyperparameters
from helpers.logging import ml_logging

if __name__ == "__main__":
    session = next(get_db())
    
    scaler_model = get_model_by_id(db=session,
                                   model_id=ml_settings.MODEL_SCALER_ID)
    
    if not scaler_model or scaler_model.model_alg != "StandardScaler":
        raise ValueError("No scaler model were found it with MODEL_SCALER_ID.")
    
    model, X_test, y_test = training_model()
    
    metrics = evaluate_model(model=model,
                             X_test=X_test,
                             y_test=y_test)
    
    filepath = save_model(model=model,
                          model_alg=ml_settings.MODEL_ALG,
                          model_version=ml_settings.MODEL_VERSION)
    

    model_details = ModelBase(model_alg=ml_settings.MODEL_ALG,
                              model_scaler_id=scaler_model.model_id,
                              model_features=','.join(model.feature_names_in_),
                              model_hyperparams=get_hyperparameters(),
                              model_path=filepath,
                              model_trained_features_dataset_partition=ml_settings.FEATURE_PARTITION,
                              model_trained_target_dataset_partition=ml_settings.TARGET_PARTITION)
    
    model = create_model(db=session,
                         model_details=model_details)
    
    ml_logging.info("The training model was successfully done.")
    
    print("Trained Model id: ", model.model_id)