import pytest
from src.generators import filter_by_currency, transaction_descriptions, card_number_generator


def test_filter_by_currency(transactions_fixture):
    gen = filter_by_currency(transactions_fixture, "USD")
    assert next(gen) == {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {
                "amount": "9824.07",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702"
        }
    assert next(gen) == {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {
                "amount": "79114.93",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188"
        }
    assert next(gen) == {
            "id": 895315941,
            "state": "EXECUTED",
            "date": "2018-08-19T04:27:37.904916",
            "operationAmount": {
                "amount": "56883.54",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод с карты на карту",
            "from": "Visa Classic 6831982476737658",
            "to": "Visa Platinum 8990922113665229"
        }

def test_filter_by_currency_no_currency(transactions_fixture):
    gen = filter_by_currency(transactions_fixture, "2")
    assert len(list(gen)) == 0


def test_filter_by_currency_empty_list():
    gen = filter_by_currency([], "2")
    assert len(list(gen)) == 0


# Далее проверяем работоспособность функции transaction_descriptions
def test_transaction_descriptions(transactions_fixture):
    gen = transaction_descriptions(transactions_fixture)
    assert next(gen) == "Перевод организации"
    assert next(gen) == "Перевод со счета на счет"


def test_transaction_descriptions_empty_list():
    gen = transaction_descriptions([])
    assert len(list(gen)) == 0


# Далее проверяем работоспособность функции card_number_generator
def test_card_number_generator():
    gen = card_number_generator(1, 4)
    assert next(gen) == "0000 0000 0000 0001"
    assert next(gen) == "0000 0000 0000 0002"
    assert next(gen) == "0000 0000 0000 0003"
    assert next(gen) == "0000 0000 0000 0004"


def test_card_number_generator_last_numbers():
    gen = card_number_generator(9999999999999998, 9999999999999999)
    assert next(gen) == "9999 9999 9999 9998"
    assert next(gen) == "9999 9999 9999 9999"


def test_card_number_generator_start_equals_stop():
    gen = card_number_generator(5, 5)
    assert next(gen) == "0000 0000 0000 0005"
    with pytest.raises(StopIteration) as exc_info:
        assert next(gen)