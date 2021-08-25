from fastapi import APIRouter
from ..currencyconverter import currency_converter

router = APIRouter()

@router.get('/currencies')
def get_currencies():
    currency_converter.get_currencies()

@router.get('/getamount')
def get_amount(amount : int, from_currency : str, to_currency: str):
    currency_converter.get_converted_amount(amount = amount, from_currency = from_currency, to_currency = to_currency)