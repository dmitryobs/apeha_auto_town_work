from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

from autoapeha.constants.place_constants import TO_SQUARE, DRIVER_TIMEOUT
from autoapeha.logger.logger import logger


def go_to_square(driver):
    press_button(driver,TO_SQUARE)


def press_button(driver,name):
    try:
        play_button = WebDriverWait(driver, DRIVER_TIMEOUT).until(
            ec.element_to_be_clickable((By.XPATH, '//input[@value="{}"]'.format(name)))
        )
        play_button.click()
        logger.info(f"Button {name} pressed")
    except NoSuchElementException as e:
        logger.error(f"Cant find button {name} : {e}")
        raise