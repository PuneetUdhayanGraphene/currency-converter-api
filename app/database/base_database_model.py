import json

from pydantic import BaseModel


class BaseDatabaseModel:

    container_name : str

    def dict(self):
        return self.__dict__

    def json(self):
        return json.dumps(self.dict())


