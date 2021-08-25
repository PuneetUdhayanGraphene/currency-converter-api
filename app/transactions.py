from database import get_db
from database.models import CurrencyDatabaseModel


class DatabaseQuery:

    def get_converted_amount(self, amount, from_currency, to_currency):
        db = get_db()
        input_currency_rate = db.query(CurrencyDatabaseModel).filter_by(name=from_currency).get()[0].value
        output_currency_rate = db.query(CurrencyDatabaseModel).filter_by(name=to_currency).get()[0].value
        return (amount * output_currency_rate) / input_currency_rate
