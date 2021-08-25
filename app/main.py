
from fastapi import FastAPI

# from .routers import job, user, authentication

app = FastAPI(
    title="Cuurency conversion API",
    description="Covert currencies.",
    version="0.0.1",
)

# app.include_router(authentication.router)
# app.include_router(user.router)
# app.include_router(job.router)