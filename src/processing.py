def filter_by_state(user_info_list: list[dict], state="EXECUTED": str) -> list[dict]:
    filtered_user_info = []
    for user_info in user_info_list:
        if user_info["state"] == state:
            filtered_user_info.append(user_info)
    return filtered_user_info
