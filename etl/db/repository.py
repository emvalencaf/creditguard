from sqlalchemy.orm import Session


from db.schemas import ModelBase
from db.models import Model
from helpers.logging import etl_logging

def create_model(db: Session,
                 model_details: ModelBase):
    """
    Adds a new model entry to the database.

    :param model_data: The model data to be added.
    :return: The created model instance.
    """
    etl_logging.info("Creating a new machine learning model entry into models table at database...")
    model = Model(**model_details.model_dump())
    
    db.add(model)
    
    db.commit()
    
    db.refresh(model)
    
    etl_logging.info("New machine learning's model entry was successfully registered at database")
    
    return model