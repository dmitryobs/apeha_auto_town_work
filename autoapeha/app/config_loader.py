# config.py

import os
from dotenv import load_dotenv
import json
import logging


class LoggerConfig:
    def __init__(self, config):
        self.log_level = config.get("LOG_LEVEL", "DEBUG")
        self.log_file = config.get("LOG_FILE", "app.log")


class BrowserConfig:
    def __init__(self, config):
        self.driver_timeout = config.get("DRIVER_TIMEOUT", 10)


class Config:
    def __init__(self):
        self._config = {}
        self._load_from_env()
        self._load_from_file()

        # Создаем вложенные конфигурационные объекты
        self.logger = LoggerConfig(self._config)
        self.browser = BrowserConfig(self._config)

    def _load_from_env(self):
        """Загружаем конфигурацию из .env."""
        load_dotenv()
        self._config = {
            "DRIVER_TIMEOUT": int(os.getenv('DRIVER_TIMEOUT', 10)),
            "LOG_LEVEL": os.getenv('LOG_LEVEL', 'DEBUG'),
            "LOG_FILE": os.getenv('LOG_FILE', 'app.log')
        }

    def _load_from_file(self):
        """Загружаем конфигурацию из JSON файла."""
        try:
            with open('config/config.json', 'r') as f:
                file_config = json.load(f)
                self._config.update(file_config)
        except FileNotFoundError:
            logging.warning("config.json не найден, используем только .env")

    def get_all(self):
        """Получаем всю конфигурацию."""
        return self._config

    def __repr__(self):
        """Показывает строковое представление конфигурации для отладки."""
        return f"<Config {self._config}>"
