from src.loggers import logger_masks


def get_mask_card_number(card_number: str) -> str:
    """Функция маскирует номер банковской карты - номер карты отображается в формате XXXX XX** **** XXXX"""
    logger_masks.info("Запуск функции маскировки банковской карты get_mask_card_number")
    card_number_with_space = ""
    count = 0

    if not card_number:
        logger_masks.error("Ошибка: Отсутствует номер карты")
        raise Exception("Отсутствует номер карты")

    if type(card_number) is not str:  # преобразуем в строку в случае передачи номера карты числовым форматом
        logger_masks.info("преобразуем в строку номер карты - случай передачи номера карты числовым форматом")
        card_number = str(card_number)
    card_number = card_number.replace(" ", "")  # удаляем лишние пробелы в случае передачи номера карты с пробелами

    logger_masks.info("маскируем номер карты")
    for letter in card_number:  # создаем свой формат номера карты ХХХХ ХХХХ ХХХХ ХХХХ
        count += 1
        card_number_with_space += letter
        if count == 4:
            card_number_with_space += " "
            count = 0
    card_number_del_last_space = card_number_with_space[:-1]  # удаляем последний лишний пробел

    mask_card_number = card_number_del_last_space[:7] + "** **** " + card_number_del_last_space[15:]
    logger_masks.info("работы функции get_mask_card_number завершена\n")
    return mask_card_number


def get_mask_account(account_number: str) -> str:
    """Функция маскирует номер банковского счета и отображает его в формате **XXXX"""
    logger_masks.info("Запуск функции маскировки номер банковского счета get_mask_account")
    if len(str(account_number)) < 20:
        logger_masks.error("Ошибка! Длина номера счёта не соответствует ожиданиям.")
        raise Exception("Ошибка! Длина номера счёта не соответствует ожиданиям.")

    if type(account_number) is not str:  # преобразуем в строку в случае передачи номера счёта числовым форматом
        logger_masks.info("преобразуем в строку номер счёта - случай передачи номера счёта числовым форматом")
        account_number = str(account_number)

    mask_account = "**" + account_number[-4:]
    logger_masks.info("работы функции get_mask_account завершена\n")
    return mask_account
