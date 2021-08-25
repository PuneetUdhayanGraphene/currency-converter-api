from .base_database_model import BaseDatabaseModel


class CurrencyDatabaseModel(BaseDatabaseModel):

    container_name = "currency-ratios"

    def __init__(self, id:str, name:str, value:int, **kwargs):
        self.id = id
        self.name = name
        self.value = value
