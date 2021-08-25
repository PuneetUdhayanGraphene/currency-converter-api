from typing import List, Dict
from datetime import datetime

from .base_database_model import BaseDatabaseModel


class UserDatabaseModel(BaseDatabaseModel):

    container_name = "users"

    def __init__(self, id:str, email:str, hashed_password:str, api_key, **kwargs):
        self.id = id
        self.email = email
        self.hashed_password = hashed_password
        self.api_key = api_key


class JobParametersDatabaseModel(BaseDatabaseModel):

    container_name = None

    def __init__(self, name:str, description:str = None, default = None, type:str = None, accepted_values:List[str] = None, accepted_datatype:str = None, **kwargs):
        self.name = name
        self.description = description
        self.default = default
        self.type = type
        self.accepted_values = accepted_values
        self.accepted_datatype = accepted_datatype


class JobFormatDatabaseModel(BaseDatabaseModel):

    container_name = "job-formats"

    def __init__(self, id:str, name:str, type:str, queue:str, parameters:List[JobParametersDatabaseModel], **kwargs):
        self.id = id
        self.name = name
        self.type = type
        self.queue = queue
        if len(parameters) > 0:
            if isinstance(parameters[0], dict):
                self.parameters = [JobParametersDatabaseModel(**i) for i in parameters]
            else:
                self.parameters = parameters

    def dict(self):
        params = [i.__dict__ for i in self.parameters]
        data = self.__dict__
        data['parameters'] = params
        return data


class JobRequestDatabaseModel(BaseDatabaseModel):

    container_name = "scraping-job-requests"

    def __init__(self, id:str, user_id:str, date:str=datetime.now().strftime('%Y-%m-%d'), name:str=None, type:str=None, parameters:dict=None, **kwargs):
        self.id = id
        self.user_id = user_id
        self.date = date
        self.name = name
        self.type = type
        self.parameters = parameters


class ScrapingJobDatabaseModel(BaseDatabaseModel):

    container_name = "scraping-jobs"

    def __init__(self, id: str, name:str, queue:str, job_format_id:str,request_id:str, inserted_on: str, pop_receipt:str , content: Dict, status:str = "queued", **kwargs):
        self.id = id
        self.name = name
        self.queue = queue
        self.job_format_id = job_format_id
        self.request_id = request_id
        self.inserted_on = inserted_on
        self.pop_receipt = pop_receipt
        self.content = content
        self.status = status
