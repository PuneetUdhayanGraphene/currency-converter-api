from .database import CosmosDatabase

db = CosmosDatabase()


def get_db():
    return db
