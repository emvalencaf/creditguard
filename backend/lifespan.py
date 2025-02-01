import asyncio
from contextlib import asynccontextmanager

from fastapi import FastAPI

from ml.ml_model import load_ml_model, load_scaler_model

@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    Manages the lifespan of the FastAPI application.
    Loads the ML model and scaler when the server starts.
    """

    print("🚀 Loading ML model and scaler...")

    # Carrega os modelos em paralelo
    ml_model, scaler_model = await asyncio.gather(
        load_ml_model(),
        load_scaler_model()
    )

    print("ml_model: ", ml_model)
    print("scaler_model: ", scaler_model)
    
    app.state.ml_model = ml_model
    app.state.scaler_model = scaler_model

    print("state.ml_model: ", app.state.ml_model)
    print("state.scaler_model: ", app.state.scaler_model)
    print("✅ Models loaded successfully!")

    # Continua a execução da aplicação
    yield  

    print("🛑 Shutting down FastAPI...")