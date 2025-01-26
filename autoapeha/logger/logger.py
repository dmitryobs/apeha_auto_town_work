import logging

from autoapeha.model.logger import LoggerConfig


import logging
from autoapeha.model.logger import LoggerConfig


def create_logger(name, logger_config: LoggerConfig):
    logger = logging.getLogger(name)
    logger.setLevel(logging.getLevelName(logger_config.log_level))

    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    console_handler.stream = open(1, mode="w", encoding="utf-8", closefd=False)
    logger.addHandler(console_handler)

    file_handler = logging.FileHandler(f"{name}.log", encoding="utf-8")
    file_handler.setFormatter(formatter)
    file_handler.setLevel(logging.getLevelName(logger_config.log_level))
    logger.addHandler(file_handler)

    return logger

