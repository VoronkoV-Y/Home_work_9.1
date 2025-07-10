import logging


logger_masks = logging.getLogger("masks_log")
file_Handler_masks = logging.FileHandler("../logs/masks.log", mode='w')
file_formatter_masks = logging.Formatter('%(asctime)s - masks.py - %(levelname)s: %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
file_Handler_masks.setFormatter(file_formatter_masks)
logger_masks.addHandler(file_Handler_masks)
logger_masks.setLevel(logging.DEBUG)


logger_utils = logging.getLogger("utils_log")
file_Handler_utils = logging.FileHandler("../logs/utils.log", mode='w')
file_formatter_utils = logging.Formatter('%(asctime)s - utils.py - %(levelname)s: %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
file_Handler_utils.setFormatter(file_formatter_utils)
logger_utils.addHandler(file_Handler_utils)
logger_utils.setLevel(logging.DEBUG)

### TESTING ###
logger_masks.info("TEST")
logger_utils.info("TEST-2")