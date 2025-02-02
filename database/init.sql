CREATE DATABASE creditguard;

CREATE SCHEMA machine_learning_details;

CREATE SCHEMA loans_application;

CREATE TABLE machine_learning_details.models IF NOT EXISTS (
    model_id
    model_alg
    hyperparameters
    model_created_at
);

CREATE TABLE machine_learning_details.model_validation_inferences IF NOT EXISTS (
    inference_id
    model_id
    
)