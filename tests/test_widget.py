import pytest

from src.widget import get_date, mask_account_card


@pytest.mark.parametrize(
    "info_card_or_account, expected",
    [
        ("Maestro 1596837868705199", "Maestro 1596 83** **** 5199"),
        ("Счет 64686473678894779589", "Счет **9589"),
        ("MasterCard 7158300734726758", "MasterCard 7158 30** **** 6758"),
        ("Счет 35383033474447895560", "Счет **5560"),
    ],
)
def test_mask_account_card_parametrize(info_card_or_account, expected):
    assert mask_account_card(info_card_or_account) == expected


# Тестирование функции на обработку некорректных входных данных и проверка ее устойчивости к ошибкам
def test_mask_account_card_incorrect_data():
    with pytest.raises(Exception) as exc_info:
        mask_account_card("7365")

    assert str(exc_info.value) == "Ошибка! Некорректные входные данные"


# Далее тестируем функцию get_date


def test_get_date(date_fixture):
    assert get_date(date_fixture) == "11.03.2024"


# Проверка, что функция корректно обрабатывает входные строки, где отсутствует дата
def test_get_date_no_date():
    with pytest.raises(Exception) as exc_info:
        get_date("")

    assert str(exc_info.value) == "Ошибка! Дата отсутствует"


# Проверка работы функции на различных входных форматах даты, включая граничные случаи и нестандартные строки с датами
def test_get_date_incorrect_format():
    with pytest.raises(Exception) as exc_info:
        get_date(20240412)

    assert str(exc_info.value) == "Ошибка! Неверный входной формат даты."
