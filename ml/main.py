from model.train import training_model
from helpers.save_file import save_model
from helpers.model_testing import evaluate_model
from config import ml_settings

if __name__ == "__main__":
    model, X_test, y_test = training_model()
    
    metrics = evaluate_model(model=model,
                             X_test=X_test,
                             y_test=y_test)
    
    save_model(model=model,
               model_alg=ml_settings.MODEL_ALG,
               model_version=ml_settings.MODEL_VERSION)
    