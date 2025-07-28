import pandas as pd
import csv


def csv_reader_fnc(path_csv: str) -> list[dict]:
    """Функция для считывания финансовых операций из CSV - выдает список словарей с транзакциями"""
    data = []
    with open(path_csv) as file:
        reader = csv.DictReader(file)
        for row in reader:
            data.append(row)
    return data

