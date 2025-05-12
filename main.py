from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from core.config import ALLOWED_ORIGINS
from routes import user_router, entity_router

app = FastAPI(
    title="FastAPI BoilerPlate",
    version="1.0.0",
    description="This is a fastapi boilerplate.",
)

# CORS configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(user_router, prefix="/api/v1/user", tags=["User"])
app.include_router(entity_router, prefix="/api/v1/entity", tags=["Entity"])

if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="localhost", port=8000)
