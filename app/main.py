
from fastapi import FastAPI

from .routers import currency

app = FastAPI(
    title="Currency conversion API",
    description="Covert currencies",
    version="0.0.1",
)

app.include_router(currency.router)