from datetime import date

from sqlalchemy import Column, Integer, String, JSON, ForeignKey, Date
from sqlalchemy.orm import relationship

from db.client import DBBaseModel

# Model SQLAlchemy
class Model(DBBaseModel):
    __tablename__ = "models"
    
    model_id = Column(Integer, primary_key=True, index=True)
    model_alg = Column(String, nullable=False)
    model_scaler_id = Column(Integer, ForeignKey("models.model_id"), nullable=True)
    model_features = Column(String, nullable=False)
    model_hyperparams = Column(JSON, nullable=True)
    model_path = Column(String, nullable=False)
    model_trained_features_dataset_partition = Column(String, nullable=False)
    model_trained_target_dataset_partition = Column(String, nullable=False)
    created_at = Column(Date, default=date.today)
    updated_at = Column(Date, nullable=True)
    
    model_scaler = relationship("Model", remote_side=[model_id])