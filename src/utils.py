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
        exchange_ = exchange_fnc(transaction)
        return exchange_
