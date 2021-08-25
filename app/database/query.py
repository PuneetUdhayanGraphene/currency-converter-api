from .models import BaseDatabaseModel
from azure.cosmos import ContainerProxy


class Query:

    def __init__(self, model: BaseDatabaseModel, db_container: ContainerProxy):
        self.model = model
        self.db_container = db_container
        self.query = 'SELECT * FROM c'

    def _get_query(self, orderby: str = None, descending: bool = False, limit: int = None, offset: int = None):
        query = self.query
        if orderby:
            query = f"{query} ORDER BY c.{orderby}"
            if descending:
                query = f"{query} DESC"
            if limit is not None and offset is not None:
                query = f"{query} OFFSET {offset} LIMIT {limit}"
        return query

    def count(self):
        query = self.query.replace("*", "VALUE COUNT(1)", 1)
        return list(self.db_container.query_items(query=query, enable_cross_partition_query=True))[0]

    def get(self, orderby: str = None, descending: bool = False, limit: int = None, offset: int = None):
        query = self._get_query(orderby=orderby, descending=descending, limit=limit, offset=offset)
        return [self.model(**i) for i in list(self.db_container.query_items(query=query, enable_cross_partition_query=True))]

    def filter_by(self, **kwargs):
        query_copy = Query(self.model, self.db_container)
        query_copy.query = self.query
        if len(kwargs) > 0 and 'WHERE' not in query_copy.query:
            query_copy.query = query_copy.query + ' WHERE'
        for key, value in kwargs.items():
            query_copy.query = f"{query_copy.query} c.{key}='{value}' AND"
        if len(kwargs) > 0:
            query_copy.query = query_copy.query[:-4]
        return query_copy
