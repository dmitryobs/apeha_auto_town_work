from selenium import webdriver
from selenium.webdriver.firefox.options import Options

from autoapeha.app.config import Config
from autoapeha.services.game_service import start_town_work


def create_driver(config: Config):
    firefox_options = Options()

    firefox_options.set_preference("general.useragent.override", config.browser_config.user_agent)

    if config.browser_config.headless:
        firefox_options.add_argument("--headless")

    if config.browser_config.disable_notifications:
        firefox_options.set_preference("dom.webnotifications.enabled", False)
        firefox_options.set_preference("dom.push.enabled", False)

    if config.browser_config.disable_automatic_updates:
        firefox_options.set_preference("app.update.enabled", False)

    if config.browser_config.proxy:
        firefox_options.set_preference("network.proxy.type", 1)
        firefox_options.set_preference("network.proxy.http", config.browser_config.proxy)
        firefox_options.set_preference("network.proxy.http_port", int(config.browser_config.proxy.split(":")[1]))

    return webdriver.Firefox(options=firefox_options)


def start_app(logger, config):
    start_town_work(config, logger, create_driver(config))
