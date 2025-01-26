import logging
import os


def create_logger(config):
    log_level = os.getenv('LOG_LEVEL', 'DEBUG').upper()
    log_file = os.getenv('LOG_FILE', 'app.log')

    logger = logging.getLogger("app_logger")
    logger.setLevel(config.)

    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    file_handler = logging.FileHandler(log_file)
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    return logger