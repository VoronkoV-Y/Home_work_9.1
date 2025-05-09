import pytest

from src.widget import mask_account_card


@pytest.mark.parametrize("info_card_or_account, expected", [("Maestro 1596837868705199", "Maestro 1596 83** **** 5199"),
                                                            ("Счет 64686473678894779589", "Счет **9589"),
                                                            ("MasterCard 7158300734726758","MasterCard 7158 30** **** 6758"),
                                                            ("Счет 35383033474447895560", "Счет **5560")])
def test_mask_account_card_parametrize(info_card_or_account, expected):
    assert mask_account_card(info_card_or_account) == expected


# Тестирование функции на обработку некорректных входных данных и проверка ее устойчивости к ошибкам
def test_mask_account_card_incorrect_data():
    with pytest.raises(Exception) as exc_info:
        mask_account_card("7365")

    assert str(exc_info.value) == "Ошибка! Некорректные входные данные"

# Maestro 1596837868705199
# Счет 64686473678894779589
# MasterCard 7158300734726758
# Счет 35383033474447895560
# Visa Classic 6831982476737658
# Visa Platinum 8990922113665229
# Visa Gold 5999414228426353
# Счет 73654108430135874305