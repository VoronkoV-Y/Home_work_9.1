import csv
# from csv import DictReader

import pandas as pd


def csv_reader_fnc(path_csv: str) -> list[dict]:
    """Функция для считывания финансовых операций из CSV - выдает список словарей с транзакциями"""
    try:
        data = pd.read_csv(path_csv, delimiter=';').to_dict(orient="records")
        return data
    except FileNotFoundError:
        return f"Ошибка! Файл {path_csv} не найден!"


def excel_reader_fnc(path_excel: str) -> list[dict]:
    """Функция для считывания финансовых операций из Excel - выдает список словарей с транзакциями."""
    try:
        data = pd.read_excel(path_excel).to_dict(orient="records")
        return data
    except FileNotFoundError:
        return f"Ошибка! Файл {path_excel} не найден!"
