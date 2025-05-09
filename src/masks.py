def get_mask_card_number(card_number: str) -> str:
    """Функция маскирует номер банковской карты - номер карты отображается в формате XXXX XX** **** XXXX"""
    card_number_with_space = ""
    count = 0

    if not card_number:
        raise Exception("Отсутствует номер карты")

    if type(card_number) is not str:  # преобразуем в строку в случае передачи номера карты числовым форматом
        card_number = str(card_number)
    card_number = card_number.replace(" ", "")  # удаляем лишние пробелы в случае передачи номера карты с пробелами

    for letter in card_number:  # создаем свой формат номера карты ХХХХ ХХХХ ХХХХ ХХХХ
        count += 1
        card_number_with_space += letter
        if count == 4:
            card_number_with_space += " "
            count = 0
    card_number_del_last_space = card_number_with_space[:-1]  # удаляем последний лишний пробел

    mask_card_number = card_number_del_last_space[:7] + "** **** " + card_number_del_last_space[15:]
    return mask_card_number


def get_mask_account(account_number: str) -> str:
    """Функция маскирует номер банковского счета и отображает его в формате **XXXX"""
    if len(str(account_number)) < 20:
        raise Exception("Ошибка! Длина номера счёта не соответствует ожиданиям.")

    if type(account_number) is not str:  # преобразуем в строку в случае передачи номера счёта числовым форматом
        account_number = str(account_number)

    mask_account = "**" + account_number[-4:]
    return mask_account
