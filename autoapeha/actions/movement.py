from selenium.common import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

from autoapeha.constants.place_constants import TO_SQUARE, TO_EDGE, TO_SAWMILL, TO_FOREST_CUTTING, START, \
    TO_EDGE_POSTFIX, TO_TOWN, TO_SHOP, TO_BUYING, SELL


def go_to_edge(config, logger, driver):
    press_button(config, logger, driver, TO_EDGE)


def go_to_sawmill(config, logger, driver):
    press_button(config, logger, driver, TO_SAWMILL)


def go_to_forest_cutting(config, logger, driver):
    press_button(config, logger, driver, TO_FOREST_CUTTING)


def start_work(config, logger, driver):
    press_button(config, logger, driver, START)


def go_back_to_edge(config, logger, driver):
    press_button(config, logger, driver, TO_EDGE_POSTFIX)


def go_to_town(config, logger, driver):
    press_button(config, logger, driver, TO_TOWN)


def go_to_shop(config, logger, driver):
    press_button(config, logger, driver, TO_SHOP)


def go_to_buying(config, logger, driver):
    press_button(config, logger, driver, TO_BUYING)


def sell(config, logger, driver):
    press_button(config, logger, driver, SELL)


def go_to_square(config, logger, driver):
    press_button(config, logger, driver, TO_SQUARE)


def press_button(config, logger, driver, name):
    try:
        play_button = WebDriverWait(driver, config.browser_config.driver_timeout).until(
            ec.element_to_be_clickable((By.XPATH, '//input[@value="{}"]'.format(name)))
        )
        play_button.click()
        logger.info(f"Button {name} pressed")
    except TimeoutException as e:
        logger.error(f"Timeout while waiting for button {name} to be clickable: {e}")
    except NoSuchElementException as e:
        logger.error(f"Cannot find button {name}: {e}")

def find_button(driver, config, name):
    try:
        play_button = WebDriverWait(driver, config.browser_config.driver_timeout).until(
            ec.element_to_be_clickable((By.XPATH, '//input[@value="{}"]'.format(name)))
        )
        return play_button
    except TimeoutException:
        return None
