import json
import os

from src.external_api import exchange_fnc


def transactions_info(path_: str) -> list[dict]:
    """Функция принимает на вход путь до JSON-файла и возвращает список словарей с данными о финансовых транзакциях"""
    try:
        with open(path_, encoding="utf-8") as file:
            try:
                data = json.load(file)
            except json.JSONDecodeError:
                return []
            if type(data) is not list:
                return []
        return data
    except FileNotFoundError:
        return []


def transaction_amount(transaction: dict) -> float:
    """Функция, которая возвращает сумму транзакции в рублях"""
    if transaction["operationAmount"]["currency"]["code"] == "RUB":
        return float(transaction["operationAmount"]["amount"])
    else:
        exchange_ = exchange_fnc(transaction["operationAmount"]["currency"]["code"])
        return float(transaction["operationAmount"]["amount"]) * exchange_


if __name__ == "__main__":
    # path_ = os.path.join(os.path.dirname(__file__), '..', 'data', 'operations.json')
    # print(transactions_info(path_))
    transaction = {
        "id": 441945886,
        "state": "EXECUTED",
        "date": "2019-08-26T10:50:58.294041",
        "operationAmount": {"amount": "1000", "currency": {"name": "руб.", "code": "USD"}},
        "description": "Перевод организации",
        "from": "Maestro 1596837868705199",
        "to": "Счет 64686473678894779589",
    }
    print(transaction_amount(transaction))
