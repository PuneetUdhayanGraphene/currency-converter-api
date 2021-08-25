from ..database import get_db
from ..database.models import CurrencyDatabaseModel

db = get_db()

db.query(CurrencyDatabaseModel).get()

def get_currencies():
    """Gagandeep"""
    pass

def get_converted_amount():
    """Vaishnavi"""
    pass