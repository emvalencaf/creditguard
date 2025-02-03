from sqlalchemy.orm import Session


from db.schemas import ModelBase
from db.models import Model
from helpers.logging import ml_logging

def get_model_by_id(db: Session,
                    model_id: int):
    """
    Get a model from database by id.
    
    :param model_id: The model unique identifier
    :return: returns model metadata
    """
    ml_logging.info("Getting scaler model metadata from database...")
    return db.query(Model).filter(Model.model_id == model_id).first()

def create_model(db: Session,
                 model_details: ModelBase):
    """
    Adds a new model entry to the database.

    :param model_data: The model data to be added.
    :return: The created model instance.
    """
    ml_logging.info("Creating a new machine learning model entry into models table at database...")
    model = Model(**model_details.model_dump())
    
    db.add(model)
    
    db.commit()
    
    db.refresh(model)
    
    ml_logging.info("New machine learning's model entry was successfully registered at database")
    
    return model