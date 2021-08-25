from ..transactions import DatabaseQuery


def get_currencies():
    """Gagandeep"""
    currencyList = []
    for i in items:
        currencyList.append(i.name)
    return currencyList
    


def get_converted_amount(amount, from_currency, to_currency):

    database_query = DatabaseQuery()
    return database_query.get_converted_amount(amount, from_currency, to_currency)
