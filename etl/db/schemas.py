from datetime import date
from typing import Optional

from pydantic import BaseModel


class ModelBase(BaseModel):
    model_alg: str
    model_scaler_id: Optional[int] = None
    model_features: str
    model_hyperparams: Optional[dict] = None
    model_path: str
    model_trained_features_dataset_partition: str
    model_trained_target_dataset_partition: str

class ModelCreate(ModelBase):
    pass

class ModelUpdate(BaseModel):
    model_alg: Optional[str] = None
    model_scaler_id: Optional[int] = None
    model_features: Optional[str] = None
    model_hyperparams: Optional[dict] = None
    model_path: Optional[str] = None
    model_trained_target_dataset_partition: Optional[str] = None
    model_trained_features_dataset_partition: Optional[str] = None
    updated_at: Optional[date] = None

class ModelResponse(ModelBase):
    model_id: int
    created_at: date
    updated_at: Optional[date]

    class Config:
        from_attributes = True