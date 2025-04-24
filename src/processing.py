def filter_by_state(user_info_list: list[dict], state: str = "EXECUTED") -> list[dict]:
    """Функция фильтрует список словарей по ключу \'state\'"""
    filtered_user_info = []
    for user_info in user_info_list:
        if user_info["state"] == state:
            filtered_user_info.append(user_info)
    return filtered_user_info


def sort_by_date(user_info_list: list[dict], reverse_param: bool = True) -> list[dict]:
    sorted_user_info_list = sorted(user_info_list, key=lambda x: x["date"], reverse=reverse_param)
    return sorted_user_info_list
