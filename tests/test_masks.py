import pytest

from src.masks import get_mask_account, get_mask_card_number


# Проверка стандартной работы функции test_get_mask_card_number, используя фикстуру
def test_get_mask_card_number(card_number_fixture):
    assert get_mask_card_number(card_number_fixture) == "1596 83** **** 5199"


# Проверка стандартной работы функции test_get_mask_card_number, используя параметризацию
@pytest.mark.parametrize(
    "card_number, expected",
    [
        ("7158300734726758", "7158 30** **** 6758"),
        ("6831982476737658", "6831 98** **** 7658"),
        ("8990922113665229", "8990 92** **** 5229"),
    ],
)
def test_get_mask_card_number_parametrize(card_number, expected):
    assert get_mask_card_number(card_number) == expected


# Проверка работы функции на различных входных форматах номеров карт, включая граничные случаи
# и нестандартные длины номеров
def test_get_mask_card_number_non_standart():
    assert get_mask_card_number("8990 9221 1366 5229") == "8990 92** **** 5229"  # номер карты с пробелами
    assert get_mask_card_number(8990922113665229) == "8990 92** **** 5229"  # формат входных данных int
    assert (
        get_mask_card_number("15968378687051991234") == "1596 83** **** 5199 1234"
    )  # нестандартная длина номера карты


# Проверка, что функция корректно обрабатывает входные строки, где отсутствует номер карты
def test_get_mask_card_number_empty():
    with pytest.raises(Exception) as exc_info:
        get_mask_card_number("")

    assert str(exc_info.value) == "Отсутствует номер карты"


# Далее тестируем функцию get_mask_account


# Проверка стандартной работы функции get_mask_account, используя фикстуру
def test_get_mask_account(account_fixture):
    assert get_mask_account(account_fixture) == "**9589"


# Проверка работы функции с различными форматами и длинами номеров счетов
@pytest.mark.parametrize(
    "account_number, expected",
    [("35383033474447895560", "**5560"), (73654108430135874305, "**4305"), ("736541084301358743051234", "**1234")],
)
def test_get_get_mask_account_non_standart_arg(account_number, expected):
    assert get_mask_account(account_number) == expected


# Проверка, что функция корректно обрабатывает входные данные, где номер счета меньше ожидаемой длины
def test_get_mask_account_too_short_length():
    with pytest.raises(Exception) as exc_info:
        get_mask_account("7365")

    assert str(exc_info.value) == "Ошибка! Длина номера счёта не соответствует ожиданиям."
