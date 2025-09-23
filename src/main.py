import re

from src.CSV_Excel import csv_reader_fnc, excel_reader_fnc
from src.masks import get_mask_account, get_mask_card_number
from src.utils import transactions_info
from src.processing import filter_by_state, sort_by_date
from src.re_functions import process_bank_search

while True:
    print("""Привет! Добро пожаловать в программу работы с банковскими транзакциями.
    Выберите необходимый пункт меню:
    1. Получить информацию о транзакциях из JSON-файла
    2. Получить информацию о транзакциях из CSV-файла
    3. Получить информацию о транзакциях из XLSX-файла\n""")

    user_input_file_format = input()

    if user_input_file_format in ["1", "2", "3"]:
        break

if user_input_file_format == '1':
    print("Для обработки выбран JSON-файл\n")
    user_data = transactions_info("data/operations.json")
elif user_input_file_format == '2':
    user_data = csv_reader_fnc("data/transactions.csv")
    print("Для обработки выбран CSV-файл\n")
elif user_input_file_format == '3':
    user_data = excel_reader_fnc("data/transactions_excel.xlsx")
    print("Для обработки выбран XLSX-файл\n")


while True:
    print("""Введите статус, по которому необходимо выполнить фильтрацию.
    Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING\n""")

    user_input_status = input().upper()
    if user_input_status in ["EXECUTED", "CANCELED", "PENDING"]:
        break
    else:
        print(f"Статус операции {user_input_status} недоступен.")

print(f"Операции отфильтрованы по статусу {user_input_status}\n")


user_data_status_filter = filter_by_state(user_data, user_input_status)


while True:
    print("Отсортировать операции по дате? Да/Нет\n")
    user_sort_date_input = input().lower()
    if user_sort_date_input == "да":
        while True:
            print("Отсортировать по возрастанию или по убыванию?\n")
            user_sort_increase_input = input().lower()
            if user_sort_increase_input == "по возрастанию":
                reverse_param = False
                break
            if user_sort_increase_input == "по убыванию":
                reverse_param = True
                break
        user_sort_date_data = sort_by_date(user_data_status_filter, reverse_param)
        break
    if user_sort_date_input == "нет":
        user_sort_date_data = user_data_status_filter
        break


while True:
    print("Выводить только рублевые транзакции? Да/Нет\n")
    user_transaction_RUB_input = input().lower()
    if user_transaction_RUB_input == "да":
        if user_input_file_format == '1':
            user_data_RUB = [operation for operation in user_sort_date_data if operation['operationAmount']['currency']['code'] == 'RUB']
        else:
            user_data_RUB = [operation for operation in user_sort_date_data if operation['currency_code'] == 'RUB']
        break
    if user_transaction_RUB_input == "нет":
        user_data_RUB = user_sort_date_data
        break


while True:
    print("Отфильтровать список транзакций по определенному слову в описании? Да/Нет\n")
    user_filter_word_input = input().lower()
    if user_filter_word_input == "да":
        print("Введите слово")
        pattern = input()
        user_data_filter_word = process_bank_search(user_data_RUB, pattern)
        break
    if user_filter_word_input == "нет":
        user_data_filter_word = user_data_RUB
        break


print("Распечатываю итоговый список транзакций...\n")
print(user_data_filter_word)

if len(user_data_filter_word) == 0:
    print('Не найдено ни одной транзакции, подходящей под ваши условия фильтрации')
else:
    print(f'Всего банковских операций в выборке: {len(user_data_filter_word)}\n')

    for operation in user_data_filter_word:
        print(operation['date'][:10].replace("-", ".") + " " + operation['description'])
        # ЕСЛИ ПЕРЕВОД
        if "Перевод" in operation['description']:
            # откуда перевод
            info_transaction_from = operation['from']
            if re.search(r'сч[её]т', info_transaction_from, flags=re.IGNORECASE):
                info_transaction_from = (re.search(r'\D+', info_transaction_from).group()) + get_mask_account(
                    re.search(r'\d+', info_transaction_from).group())
            else:
                info_transaction_from = (re.search(r'\D+', info_transaction_from).group()) + get_mask_card_number(
                    re.search(r'\d+', info_transaction_from).group())
            # куда перевод
            info_transaction_TO = operation['to']
            if re.search(r'сч[её]т', info_transaction_TO, flags=re.IGNORECASE):
                info_transaction_TO = (re.search(r'\D+', info_transaction_TO).group()) + get_mask_account(
                    re.search(r'\d+', info_transaction_TO).group())
            else:
                info_transaction_TO = (re.search(r'\D+', info_transaction_TO).group()) + get_mask_card_number(
                    re.search(r'\d+', info_transaction_TO).group())
            print(f'{info_transaction_from} -> {info_transaction_TO}')

        # ЕСЛИ НЕ ПЕРЕВОД
        else:
            info_transaction_TO = operation['to']
            if re.search(r'сч[её]т', info_transaction_TO, flags=re.IGNORECASE):
                info_transaction_TO = (re.search(r'\D+', info_transaction_TO).group()) + get_mask_account(
                    re.search(r'\d+', info_transaction_TO).group())
            else:
                info_transaction_TO = (re.search(r'\D+', info_transaction_TO).group()) + get_mask_card_number(
                    re.search(r'\d+', info_transaction_TO).group())
            print(info_transaction_TO)

        if user_input_file_format == '1':
            print(f"Сумма: {operation['operationAmount']['amount']} {operation['operationAmount']['currency']['code']}\n")
        else:
            print(f"Сумма: {operation['amount']} {operation['currency_code']}\n")

# THE END =)
# Made by VoronkoV_Y =)
