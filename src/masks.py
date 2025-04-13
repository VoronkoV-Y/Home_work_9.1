def get_mask_card_number(card_number: str) -> str:
    """Функция маскирует номер банковской карты - номер карты отображается в формате XXXX XX** **** XXXX"""
    mask_card_number = card_number[:4] + " " + card_number[4:6] + "** **** " + card_number[-4:]
    return mask_card_number


def get_mask_account(account_number: str) -> str:
    """Функция маскирует номер банковского счета и отображает его в формате **XXXX"""
    mask_account = "**" + account_number[-4:]
    return mask_account
