from ..database import get_db
from ..database.models import CurrencyDatabaseModel

db = get_db()

items = db.query(CurrencyDatabaseModel).get()

def get_currencies():
    """Gagandeep"""
    currencyList = []
    for i in items:
        currencyList.append(i.name)
    return currencyList
    

def get_converted_amount():
    """Vaishnavi"""
    pass