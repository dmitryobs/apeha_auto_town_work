from selenium import webdriver
from selenium.webdriver.firefox.options import Options

from autoapeha.app.config import Config
from autoapeha.services.game_service import start_town_work


def create_driver(config: Config):
    firefox_options = Options()
    firefox_options.set_preference("general.useragent.override", config.browser_config.user_agent)
    return webdriver.Firefox(options=firefox_options)


def start_app(logger, config):
    start_town_work(config, logger, create_driver(config))
