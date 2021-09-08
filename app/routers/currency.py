from fastapi import APIRouter

from ..currencyconverter import currency_converter

router = APIRouter()

@router.get('/currencies')
def get_currencies():
    """[Gets the currencies from database]

    Returns:
        [dictionary]: [Types of currencies available]
    """
    return {"currencies": currency_converter.get_currencies()}

@router.get('/getamount')
def get_amount(amount : int, from_currency : str, to_currency: str):
    """[Converts currencies from one form to another]

    Args:
        amount (int): [The amount value user wants to convert]
        from_currency (str): [The currency user wants to convert from]
        to_currency (str): [The currency user wants to convert to]

    Returns:
        [dictionary]: [The converted amount]
    """
    amount = currency_converter.get_converted_amount(amount = amount, from_currency = from_currency, to_currency = to_currency)
    return {"converted_amount": amount}