"""
Contains CosmosDatabase class
"""
import os

from azure.cosmos import CosmosClient, exceptions
from azure.cosmos.container import ContainerProxy

from .base_database_model import BaseDatabaseModel
from .query import Query


class CosmosDatabase:
    """
    Used to perform CRUD opertions on Cosmos DB

    Attributes:
        database (DatabaseProxy) : Represnts database of cosmos DB
    """

    def __init__(self):
        """
        Constuctor of CosmosDatabase
        """
        url = os.environ['DATABASE_ACCOUNT_URI']
        key = os.environ['DATABASE_ACCOUNT_KEY']
        client = CosmosClient(url, credential=key)
        database_name = os.environ['DATABASE_NAME']
        try:
            self.database = client.create_database(database_name)
        except exceptions.CosmosResourceExistsError:
            self.database = client.get_database_client(database_name)

    def _get_container(self, container_name: str) -> ContainerProxy:
        return self.database.get_container_client(container_name)

    def insert(self, database_item: BaseDatabaseModel):
        """
        Used to insert item into database

        Parameters:
            database_item(BaseDatabaseModel) : Item that needs to be inserted.
                                               It is an object of a database model
        """
        container = self._get_container(database_item.container_name)
        container.upsert_item(database_item.dict())

    def query(self, database_model: BaseDatabaseModel):
        """
        Used to query the database

        Parameters:
            database_model(BaseDatabaseModel[class]) : Class representing container
                                                       from which data is to be retreived

        Returns:
            Query object
        """
        container = self._get_container(database_model.container_name)
        return Query(model=database_model, db_container=container)

    def delete(self, database_item: BaseDatabaseModel):
        """
        Used to delete an item from the database

        Parameters:
            database_item(BaseDatabaseModel): Item that needs to be deleted
        """
        container = self._get_container(database_item.container_name)
        container.delete_item(database_item.id, database_item.id)

    def update(self, database_item: BaseDatabaseModel):
        """
        Used to update an item in the database

        Parameters:
            database_item(BaseDatabaseModel): Item that needs to be updated
        """
        container = self._get_container(database_item.container_name)
        container.upsert_item(database_item.dict())
