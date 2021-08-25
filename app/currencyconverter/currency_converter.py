from ..transactions import DatabaseQuery


database_query = DatabaseQuery()


def get_currencies():
    return database_query.get_all_countries()
    

def get_converted_amount(amount, from_currency, to_currency):
    return database_query.get_converted_amount(amount, from_currency, to_currency)
