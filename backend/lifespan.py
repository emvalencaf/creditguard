import asyncio
from contextlib import asynccontextmanager

from fastapi import FastAPI

from ml.ml_model import load_ml_model, load_scaler_model

# Variáveis globais para armazenar os modelos carregados
ml_model = None
scaler_model = None

@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    Manages the lifespan of the FastAPI application.
    Loads the ML model and scaler when the server starts.
    """
    global ml_model, scaler_model

    print("🚀 Loading ML model and scaler...")

    # Carrega os modelos em paralelo
    ml_model, scaler_model = await asyncio.gather(
        load_ml_model(),
        load_scaler_model()
    )

    print("✅ Models loaded successfully!")

    # Continua a execução da aplicação
    yield  

    print("🛑 Shutting down FastAPI...")