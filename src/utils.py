import json
import os


def transactions_info(path_: str) -> list[dict]:
    """ Функция принимает на вход путь до JSON-файла и возвращает список словарей с данными о финансовых транзакциях"""
    try:
        with open (path_, encoding='utf-8') as file:
            try:
                data = json.load(file)
            except json.JSONDecodeError:
                return []
            if type(data) is not list:
                    return []
        return data
    except FileNotFoundError:
        return []


if __name__ == "__main__":
    path_ = os.path.join(os.path.dirname(__file__), '..', 'data', 'operations.json')
    print(transactions_info(path_))