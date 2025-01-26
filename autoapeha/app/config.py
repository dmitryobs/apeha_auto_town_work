import os
from dataclasses import dataclass

from dotenv import load_dotenv

from autoapeha.model.browser import BrowserConfig
from autoapeha.model.logger import LoggerConfig
from autoapeha.model.user import UserConfig


@dataclass
class Config:
    logger_config: LoggerConfig
    browser_config: BrowserConfig

    def __init__(self):
        load_dotenv()

        self.logger_config = LoggerConfig(
            log_level=os.getenv('LOG_LEVEL', 'DEBUG'),
        )

        self.browser_config = BrowserConfig(
            base_url=os.getenv("BASE_URL", "https://apeha.ru"),
            driver_timeout=int(os.getenv('DRIVER_TIMEOUT', 10)),
            user_agent=os.getenv('USER_AGENT',
                                 "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Edg/131.0.0.0"),
            headless=os.getenv('HEADLESS', 'False').lower() == 'true',
            proxy=os.getenv('PROXY', ''),
            disable_notifications=os.getenv('DISABLE_NOTIFICATIONS', 'True').lower() == 'true',
            disable_automatic_updates=os.getenv('DISABLE_AUTOMATIC_UPDATES', 'True').lower() == 'true'
        )
        self.user_config = UserConfig(
            login=os.getenv("LOGIN", ""),
            password=os.getenv("PASSWORD", "")
        )
