from src.CSV_Excel import csv_reader_fnc, excel_reader_fnc
from src.utils import transactions_info
from src.processing import filter_by_state, sort_by_date

while True:
    print("""Привет! Добро пожаловать в программу работы с банковскими транзакциями.
    Выберите необходимый пункт меню:
    1. Получить информацию о транзакциях из JSON-файла
    2. Получить информацию о транзакциях из CSV-файла
    3. Получить информацию о транзакциях из XLSX-файла""")

    user_input_file_format = input()

    if user_input_file_format in ["1", "2", "3"]:
        break

if user_input_file_format == '1':
    print("Для обработки выбран JSON-файл")
    user_data = transactions_info("data/operations.json")
    # print(user_data)
elif user_input_file_format == '2':
    user_data = csv_reader_fnc("data/transactions.csv")
    print("Для обработки выбран CSV-файл")
    print(user_data)
elif user_input_file_format == '3':
    user_data = excel_reader_fnc("data/transactions_excel.xlsx")
    print("Для обработки выбран XLSX-файл")
    # print(user_data)


while True:
    print("""Введите статус, по которому необходимо выполнить фильтрацию.
    Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING""")

    user_input_status = input().upper()
    if user_input_status in ["EXECUTED", "CANCELED", "PENDING"]:
        break
    else:
        print(f"Статус операции {user_input_status} недоступен.")

print(f"Операции отфильтрованы по статусу {user_input_status}")


user_data_status_filter = filter_by_state(user_data, user_input_status)
print(user_data_status_filter)

# while True:
#     print("Отсортировать операции по дате? Да/Нет")
#     user_sort_date_input = input().lower()
#     if user_sort_date_input == ["да"]:
#         pass
#     break
#     if user_sort_date_input == ["нет"]:
#         pass
#     break
#
# while True:
#     print("Отсортировать по возрастанию или по убыванию?")
#     user_sort_increase_input = input().lower()
#     if user_sort_increase_input == ["по возрастанию"]:
#         pass
#     break
#     if user_sort_increase_input == ["по убыванию"]:
#         pass
#     break
#
#
# while True:
#     print("Выводить только рублевые транзакции? Да/Нет")
#     user_transaction_RUB_input = input().lower()
#     if user_transaction_RUB_input == ["да"]:
#         pass
#     break
#     if user_transaction_RUB_input == ["нет"]:
#         pass
#     break
#
#
# while True:
#     print("Отфильтровать список транзакций по определенному слову в описании? Да/Нет")
#     user_filter_word_input = input().lower()
#     if user_filter_word_input == ["да"]:
#         print("Введите слово") !!!
#         pass
#     break
#     if user_filter_word_input == ["нет"]:
#         pass
#     break
#
#
# print("Распечатываю итоговый список транзакций...")
#
# Программа:
# Всего банковских операций в выборке: 4
#
# 08.12.2019 Открытие вклада
# Счет **4321
# Сумма: 40542 руб.
#
# 12.11.2019 Перевод с карты на карту
# MasterCard 7771 27** **** 3727 -> Visa Platinum 1293 38** **** 9203
# Сумма: 130 USD
#
# 18.07.2018 Перевод организации
# Visa Platinum 7492 65** **** 7202 -> Счет **0034
# Сумма: 8390 руб.
#
# 03.06.2018 Перевод со счета на счет
# Счет **2935 -> Счет **4321
# Сумма: 8200 EUR
#
# Если выборка оказалась пустой, программа выводит сообщение:
#
# Программа: Не найдено ни одной транзакции, подходящей под ваши
# условия фильтрации
