import requests
import json
from config import keys


class APIException(Exception):
    pass


class Conv:
    @staticmethod
    def get_price(quote, base, amount):
        if quote == base:
            raise APIException(f'Лучше ввести разные валюты {base}')
        try:
            quote_ticker = keys[quote]
        except KeyError:
            raise APIException(f'Что-то не то с этой валютой {quote}')
        try:
            base_ticker = keys[base]
        except KeyError:
            raise APIException(f'Что-то не так с этой валютой {base}')
        try:
            amount = float(amount)
        except ValueError:
            raise APIException(f'Количество валюты лучше указать числом, например, 1 или 2.5, а не {amount}')

        r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={quote_ticker}&tsyms={base_ticker}')
        total_base = json.loads(r.content)[keys[base]]
        return float(total_base)*float(amount)
