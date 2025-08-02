import logging


logger_masks = logging.getLogger("masks_log")
file_handler_masks = logging.FileHandler("logs/masks.log", mode="w", encoding="UTF-8")
file_formatter_masks = logging.Formatter(
    "%(asctime)s - masks.py - %(levelname)s: %(message)s", datefmt="%Y-%m-%d %H:%M:%S"
)
file_handler_masks.setFormatter(file_formatter_masks)
logger_masks.addHandler(file_handler_masks)
logger_masks.setLevel(logging.DEBUG)


logger_utils = logging.getLogger("utils_log")
file_handler_utils = logging.FileHandler("logs/utils.log", mode="w", encoding="UTF-8")
file_formatter_utils = logging.Formatter(
    "%(asctime)s - utils.py - %(levelname)s: %(message)s", datefmt="%Y-%m-%d %H:%M:%S"
)
file_handler_utils.setFormatter(file_formatter_utils)
logger_utils.addHandler(file_handler_utils)
logger_utils.setLevel(logging.DEBUG)
