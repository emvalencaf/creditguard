from fastapi import APIRouter

# project routers
from ml.router import router as ml_router


api_router = APIRouter()

api_router.include_router(ml_router,
                          prefix="/ml")

@api_router.get("/health_check")
async def get_health_check():
    return "Server is running"