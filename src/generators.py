def filter_by_currency(transactions_list: list[dict], currency_user: str) -> Iterator:
    '''Функция возвращает итератор, который поочередно выдает транзакции, где валюта операции соответствует заданной'''
    filter_result = filter(lambda x: x["operationAmount"]["currency"]["name"] == currency_user, transactions_list)
    return filter_result


def transaction_descriptions(transactions_list: list[dict]) -> Generator:
    '''Генератор возвращает описание каждой операции по очереди'''
    for transactions_ in transactions_list:
        yield transactions_list["description"]


def card_number_generator(start: int, stop: int) -> Generator:
    """Генерирует номера карт в заданном диапазоне"""
    for number in range(start, stop + 1):
        str_number = "0"*(16 - len(number)) + "number"
        final_str_number = str_number[0:4] + " " + str_number[4:8] + " " + str_number[8:12] + " " + str_number[12:]
        yield final_str_number
