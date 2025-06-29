import os

import requests
from dotenv import load_dotenv

url = "https://api.apilayer.com/exchangerates_data/convert"
load_dotenv()
API_KEY = os.getenv("API_KEY_apilayer")


def exchange_fnc(rate: str) -> float:
    """Функция конвертации валюты в рубли"""
    payload = {"amount": "1", "from": rate, "to": "RUB"}
    headers = {"apikey": API_KEY}

    response = requests.get(url, headers=headers, params=payload)

    status_code = response.status_code
    result_ = response.json()
    return float(result_["result"])
