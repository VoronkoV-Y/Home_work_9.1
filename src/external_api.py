import os

import requests
from dotenv import load_dotenv

url = "https://api.apilayer.com/exchangerates_data/convert"
load_dotenv()
API_KEY = os.getenv("API_KEY_apilayer")


def exchange_fnc(transaction: dict) -> float:
    """Функция конвертации валюты в рубли"""
    if type(transaction) == dict:
        payload = {
            "amount": transaction["operationAmount"]["amount"],
            "from": transaction["operationAmount"]["currency"]["code"],
            "to": "RUB"
            }
        headers = {"apikey": API_KEY}

        response = requests.get(url, headers=headers, params=payload)

        status_code = response.status_code
        result_ = response.json()
        result_amount_RUB = result_['result']
        return float(result_amount_RUB)
