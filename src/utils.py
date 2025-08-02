import json

from src.loggers import logger_utils
from src.external_api import exchange_fnc


def transactions_info(path_: str) -> list[dict]:
    """Функция принимает на вход путь до JSON-файла и возвращает список словарей с данными о финансовых транзакциях"""
    logger_utils.info("Запуск функции transactions_info")
    try:
        logger_utils.info("Открываем файл")
        with open(path_, encoding="utf-8") as file:
            try:
                data = json.load(file)
            except json.JSONDecodeError as e:
                logger_utils.error(f"Ошибка! {e}\n")
                return []
            if type(data) is not list:
                logger_utils.error("Ошибка! Данные не являются списком.\n")
                return []
        logger_utils.info("Заверщение работы функции transactions_info\n")
        return data
    except FileNotFoundError:
        logger_utils.error("Ошибка. Файл не найден.\n")
        return []


def transaction_amount(transaction: dict) -> float:
    """Функция, которая возвращает сумму транзакции в рублях"""
    logger_utils.info("Запуск функции transaction_amount")
    if transaction["operationAmount"]["currency"]["code"] == "RUB":
        logger_utils.info("Транзакция в рублях.")
        logger_utils.info("Заверщение работы функции transaction_amount.\n")
        return float(transaction["operationAmount"]["amount"])
    else:
        logger_utils.info("Запрос функции конвертации валюты в рубли exchange_fnc")
        exchange_ = exchange_fnc(transaction)
        logger_utils.info("Заверщение работы функции transaction_amount.\n")
        return exchange_
