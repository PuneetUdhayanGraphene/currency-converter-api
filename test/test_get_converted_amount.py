import pytest

from app.transactions import DatabaseQuery


@pytest.mark.parametrize("amount, from_currency, to_currency")
def test_get_converted_amount(self, amount, from_currency, to_currency, monkeypatch):
    monkeypatch.setattr(DatabaseQuery, "get_converted_amount", lambda *args: "Tested")