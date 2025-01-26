import time

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from autoapeha.actions.movement import go_to_square, go_to_edge, go_to_sawmill, go_to_forest_cutting, start_work, \
    go_back_to_edge, go_to_town, go_to_shop, go_to_buying, sell, find_button
from autoapeha.constants.place_constants import TO_HOUSE


def start_town_work(config, logger, driver):
    driver = login(config, logger, driver)
    driver = switch_driver(logger, driver)
    while True:
        at_square = check_location(driver, config)
        if at_square:
            go_to_edge(config, logger, driver)
            go_to_sawmill(config, logger, driver)
            go_to_forest_cutting(config, logger, driver)
            start_work(config, logger, driver)
            time.sleep(24 * 60)
            go_back_to_edge(config, logger, driver)
            go_to_town(config, logger, driver)
            go_to_shop(config, logger, driver)
            go_to_buying(config, logger, driver)
            sell(config, logger, driver)
            go_to_square(config, logger, driver)
            time.sleep(32 * 60)
        else:
            go_back_to_edge(config,logger,driver)
            go_to_town(config,logger,driver)
            go_to_square(config, logger, driver)


def check_location(driver, config):
    find = find_button(driver, config, TO_HOUSE)
    if find is not None:
        return True
    return False


def login(config, logger, driver):
    try:
        logger.info("Open site")
        driver.get(config.browser_config.base_url)
        logger.info("Entering username")
        input_field = WebDriverWait(driver, config.browser_config.driver_timeout).until(
            EC.presence_of_element_located((By.XPATH,
                                            '//input[@type="text" and @name="login" and @style="background: transparent; border: 0px; font-weight: bold; width: 138px;"]'))
        )
        input_field.send_keys(config.user_config.login)

        logger.info("Entering password")
        input_field2 = WebDriverWait(driver, config.browser_config.driver_timeout).until(
            EC.presence_of_element_located((By.XPATH,
                                            '//input[@type="password" and @name="pwd" and @style="width: 138px; background: transparent; border: 0px;"]'))
        )
        input_field2.send_keys(config.user_config.password)

        try:
            button = WebDriverWait(driver, config.browser_config.driver_timeout).until(
                EC.element_to_be_clickable((By.XPATH, '//div[contains(@onclick, "#loginform")]'))
            )
            button.click()
        except NoSuchElementException as e:
            logger.error(f"Cant find button to login: {e}")
            raise

        all_windows_before_click = driver.window_handles

        button = WebDriverWait(driver, config.browser_config.driver_timeout).until(
            EC.element_to_be_clickable((By.XPATH, '//div[contains(@onclick, "kovcheg2.apeha.ru/mbattle.html")]'))
        )
        button.click()

        WebDriverWait(driver, config.browser_config.driver_timeout).until(
            EC.new_window_is_opened(all_windows_before_click))

        all_windows_after_click = driver.window_handles
        new_window = [window for window in all_windows_after_click if window != driver.current_window_handle][0]
        driver.switch_to.window(new_window)

        return driver

    except NoSuchElementException as e:
        logger.error(f"Cant login: {e}")
        raise


def switch_driver(logger, driver):
    try:
        iframes = driver.find_elements(By.TAG_NAME, "frame")
        logger.info(f"Find {len(iframes)} frames on page.")

        for iframe in iframes:
            logger.info(f"Frame with attribute name: {iframe.get_attribute('name')}")

        WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.NAME, "d_act"))
        )

        driver.switch_to.frame("d_act")
        logger.info("Switched frame on d_act.")
        return driver

    except NoSuchElementException as e:
        logger.error(f"Cant find frame with name  d_act: {e}")
        raise
