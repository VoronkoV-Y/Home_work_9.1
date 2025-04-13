from . import masks


def mask_account_card(info_card: str) -> str:
    """Функция возвращаeт строку с замаскированным номером"""
    info_card_list = info_card.split()
    if len(info_card_list[-1]) == 16:  # проверяем количество цифр и определяем счёт это или КАРТА
        info_card_list[-1] = masks.get_mask_card_number(info_card_list[-1])
        return " ".join(info_card_list)

    if len(info_card_list[-1]) == 20:  # проверяем количество цифр и определяем СЧЁТ это или карта
        info_card_list[-1] = masks.get_mask_account(info_card_list[-1])
        return " ".join(info_card_list)
    return ""


def get_date(date_data: str) -> str:
    """Функция преобразует время в формат ДД.ММ.ГГГГ"""
    date_without_time = date_data.split("T")  # разделяем строку на дату и время
    date_list = date_without_time[0].split("-")
    new_date_data = ".".join(date_list[::-1])
    return new_date_data
