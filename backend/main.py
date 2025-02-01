import asyncio
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# global modules
from ml.ml_model import load_ml_model, load_scaler_model
from cloud import get_google_drive_service
from config import global_settings
from router import api_router
from lifespan import lifespan

app = FastAPI(title='CreditGuard API',
              version='0.0.1',
              description="A API for predict wether a loan applicant most likely be a defaulter",
              lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[global_settings.FRONTEND_URL],
    allow_headers=["*"],
    allow_methods=["*"],
    allow_credentials=True,
)

app.include_router(api_router,
                   prefix=global_settings.API_V_STR)

if __name__ == "__main__":
    import uvicorn
    
    uvicorn.run("main:app",
                host=global_settings.BACKEND_HOST,
                port=global_settings.BACKEND_PORT,
                log_level='info', reload=True)

