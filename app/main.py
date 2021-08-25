
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .routers import currency

app = FastAPI(
    title="Currency conversion API",
    description="Covert currencies",
    version="0.0.1",
)

origins = [
    "http://localhost",
    "http://localhost:4200",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(currency.router)