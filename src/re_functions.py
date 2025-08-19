import re
from collections import Counter


def process_bank_search(data: list[dict], search_str: str) -> list[dict]:
    """Функция принимает список словарей с данными о банковских операциях и строку поиска,
     а возвращает список словарей, у которых в описании есть данная строка"""
    pattern = search_str
    return [operation for operation in data if re.search(pattern, operation["description"])]


def process_bank_operations(data: list[dict], categories: list) -> dict:
    """Функция принимает список словарей с данными о банковских операциях и список категорий операций, а возвращает словарь,
    в котором ключи — это названия категорий, а значения — это количество операций в каждой категории."""
    return Counter(operation["description"] for operation in data if operation["description"] in categories)
