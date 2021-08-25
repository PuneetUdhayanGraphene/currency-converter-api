from database import get_db
from database.models import CurrencyDatabaseModel


class DatabaseQuery:

    def __init__(self):
        self.db = get_db()

    def get_all_countries(self):
        items = self.db.query(CurrencyDatabaseModel).get()
        return [i.name for i in items]

    def get_converted_amount(self, amount, from_currency, to_currency):
        input_currency_rate = self.db.query(CurrencyDatabaseModel).filter_by(name=from_currency).get()[0].value
        output_currency_rate = self.db.query(CurrencyDatabaseModel).filter_by(name=to_currency).get()[0].value
        return (amount * output_currency_rate) / input_currency_rate
