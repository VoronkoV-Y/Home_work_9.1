import json
import os
from unittest.mock import Mock, mock_open, patch

import pytest
from dotenv import load_dotenv

from src.external_api import exchange_fnc
from src.utils import transaction_amount, transactions_info

# @patch('builtins.open', new_callable=mock_open, read_data='[]')
# def test_transactions_info(mock_open):
#     mocked_data = json.load(mock_open)
#     assert transactions_info() == []


def test_transactions_info():
    with patch("builtins.open", new_callable=mock_open, read_data='[{"id": 1}]'):
        assert transactions_info("some_file.json") == [{"id": 1}]
        # mock_open.assert_called_once_with("some_file.json", encoding='utf-8')


def test_transactions_info_no_list():
    with patch("builtins.open", mock_open(read_data='{"id": 1}')):
        assert transactions_info("some_file.json") == []


def test_transactions_info_empty():
    with patch("builtins.open", mock_open(read_data="")):
        assert transactions_info("some_file.json") == []


# Тестируем функцию transaction_amount()
def test_transaction_amount_RUB(RUB_transaction_amount_fixture):
    assert transaction_amount(RUB_transaction_amount_fixture) == 48223.05


@patch("requests.get")
def test_transaction_amount_USD(mock_get):
    mock_get.return_value.json.return_value = {"result": 500}
    transaction = {
        "id": 142264268,
        "state": "EXECUTED",
        "date": "2019-04-04T23:20:05.206878",
        "operationAmount": {"amount": "50", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод со счета на счет",
        "from": "Счет 19708645243227258542",
        "to": "Счет 75651667383060284188",
    }

    load_dotenv()
    API_KEY = os.getenv("API_KEY_apilayer")
    payload = {"amount": "50", "from": "USD", "to": "RUB"}
    headers = {"apikey": API_KEY}

    assert transaction_amount(transaction) == 500
    mock_get.assert_called_once_with(
        "https://api.apilayer.com/exchangerates_data/convert", headers=headers, params=payload
    )
