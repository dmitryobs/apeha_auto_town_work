from autoapeha.actions.movement import go_to_square


def start_town_work(driver):
    go_to_square(driver)


# import time
#
# from selenium import webdriver
# from selenium.common.exceptions import NoSuchElementException
# from selenium.webdriver.common.by import By
# from selenium.webdriver.firefox.options import Options
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.ui import WebDriverWait
#
# user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Edg/131.0.0.0"
#
# firefox_options = Options()
# firefox_options.set_preference("general.useragent.override", user_agent)
#
# driver = webdriver.Firefox(options=firefox_options)
#
# try:
#     print("Открываем сайт...")
#     driver.get("https://apeha.ru")
#
#     print("Находим поле ввода для логина...")
#     input_field = WebDriverWait(driver, 10).until(
#         EC.presence_of_element_located((By.XPATH,
#                                         '//input[@type="text" and @name="login" and @style="background: transparent; border: 0px; font-weight: bold; width: 138px;"]'))
#     )
#     input_field.send_keys("obs_champion")
#
#     print("Находим поле ввода для пароля...")
#     input_field2 = WebDriverWait(driver, 10).until(
#         EC.presence_of_element_located((By.XPATH,
#                                         '//input[@type="password" and @name="pwd" and @style="width: 138px; background: transparent; border: 0px;"]'))
#     )
#     input_field2.send_keys("SerijSejf()8")
#
#     print("Находим и нажимаем кнопку входа...")
#     try:
#         button = WebDriverWait(driver, 10).until(
#             EC.element_to_be_clickable((By.XPATH, '//div[contains(@onclick, "#loginform")]'))
#         )
#         button.click()
#     except NoSuchElementException as e:
#         print(f"Ошибка: кнопка входа не найдена. Подробности: {e}")
#         driver.save_screenshot("login_button_not_found.png")
#         raise
#
#     print("Ждем появления нового окна...")
#     all_windows_before_click = driver.window_handles
#
#     print("Кликаем на кнопку для перехода на другую страницу...")
#     button = WebDriverWait(driver, 10).until(
#         EC.element_to_be_clickable((By.XPATH, '//div[contains(@onclick, "kovcheg2.apeha.ru/mbattle.html")]'))
#     )
#     button.click()
#
#     WebDriverWait(driver, 10).until(EC.new_window_is_opened(all_windows_before_click))
#
#     all_windows_after_click = driver.window_handles
#     new_window = [window for window in all_windows_after_click if window != driver.current_window_handle][0]
#     driver.switch_to.window(new_window)
#
#     print("Переключаемся на новое окно.")
#
#     try:
#         iframes = driver.find_elements(By.TAG_NAME, "frame")
#         print(f"Найдено {len(iframes)} фреймов на странице.")
#         for iframe in iframes:
#             print(f"Фрейм с атрибутом name: {iframe.get_attribute('name')}")
#
#         WebDriverWait(driver, 30).until(
#             EC.presence_of_element_located((By.NAME, "d_act"))
#         )
#         print("Фрейм с именем d_act найден.")
#         driver.switch_to.frame("d_act")
#         print("Перешли в фрейм с именем d_act.")
#
#     except NoSuchElementException as e:
#         print(f"Ошибка: не удалось найти фрейм с именем d_act. Подробности: {e}")
#         driver.save_screenshot("frame_d_act_not_found.png")
#         raise
#
#     print("Взаимодействуем с игрой внутри фрейма...")
#
#     while True:
#
#         try:
#             play_button = WebDriverWait(driver, 10).until(
#                 EC.element_to_be_clickable((By.XPATH, '//input[@value="Опушка"]'))
#             )
#             play_button.click()
#             print("Нажали на кнопку Опушка.")
#         except NoSuchElementException as e:
#             print(f"Ошибка при взаимодействии с элементами игры: {e}")
#             driver.save_screenshot("game_element_not_found.png")
#             raise
#
#         try:
#             play_button = WebDriverWait(driver, 10).until(
#                 EC.element_to_be_clickable((By.XPATH, '//input[@value="Лесопилка"]'))
#             )
#             play_button.click()
#             print("Нажали на кнопку Лесопилка.")
#         except NoSuchElementException as e:
#             print(f"Ошибка при взаимодействии с элементами игры: {e}")
#             driver.save_screenshot("game_element_not_found.png")
#             raise
#
#         try:
#             play_button = WebDriverWait(driver, 10).until(
#                 EC.element_to_be_clickable((By.XPATH, '//input[@value="Рубить лес"]'))
#             )
#             play_button.click()
#             print("Нажали на кнопку Рубить лес.")
#         except NoSuchElementException as e:
#             print(f"Ошибка при взаимодействии с элементами игры: {e}")
#             driver.save_screenshot("game_element_not_found.png")
#             raise
#
#         try:
#             play_button = WebDriverWait(driver, 10).until(
#                 EC.element_to_be_clickable((By.XPATH, '//input[@value="Приступить"]'))
#             )
#             play_button.click()
#             print("Нажали на кнопку Приступить.")
#         except NoSuchElementException as e:
#             print(f"Ошибка при взаимодействии с элементами игры: {e}")
#             driver.save_screenshot("game_element_not_found.png")
#             raise
#
#         time.sleep(24 * 60)
#
#         try:
#             play_button = WebDriverWait(driver, 10).until(
#                 EC.element_to_be_clickable((By.XPATH, '//input[@value="На опушку"]'))
#             )
#             play_button.click()
#             print("Нажали на кнопку На опушку.")
#         except NoSuchElementException as e:
#             print(f"Ошибка при взаимодействии с элементами игры: {e}")
#             driver.save_screenshot("game_element_not_found.png")
#             raise
#
#         try:
#             play_button = WebDriverWait(driver, 10).until(
#                 EC.element_to_be_clickable((By.XPATH, '//input[@value="Город"]'))
#             )
#             play_button.click()
#             print("Нажали на кнопку Город.")
#         except NoSuchElementException as e:
#             print(f"Ошибка при взаимодействии с элементами игры: {e}")
#             driver.save_screenshot("game_element_not_found.png")
#             raise
#
#         try:
#             play_button = WebDriverWait(driver, 10).until(
#                 EC.element_to_be_clickable((By.XPATH, '//input[@value="В Лавку"]'))
#             )
#             play_button.click()
#             print("Нажали на кнопку В Лавку.")
#         except NoSuchElementException as e:
#             print(f"Ошибка при взаимодействии с элементами игры: {e}")
#             driver.save_screenshot("game_element_not_found.png")
#             raise
#         try:
#             play_button = WebDriverWait(driver, 10).until(
#                 EC.element_to_be_clickable((By.XPATH, '//input[@value="Скупка"]'))
#             )
#             play_button.click()
#             print("Нажали на кнопку Скупка.")
#         except NoSuchElementException as e:
#             print(f"Ошибка при взаимодействии с элементами игры: {e}")
#             driver.save_screenshot("game_element_not_found.png")
#             raise
#
#         try:
#             play_button = WebDriverWait(driver, 10).until(
#                 EC.element_to_be_clickable((By.XPATH, '//input[@value="Продать"]'))
#             )
#             play_button.click()
#             print("Нажали на кнопку Продать.")
#         except NoSuchElementException as e:
#             print(f"Ошибка при взаимодействии с элементами игры: {e}")
#             driver.save_screenshot("game_element_not_found.png")
#             raise
#
#         try:
#             play_button = WebDriverWait(driver, 10).until(
#                 EC.element_to_be_clickable((By.XPATH, '//input[@value="На площадь"]'))
#             )
#             play_button.click()
#             print("Нажали на кнопку На площадь.")
#         except NoSuchElementException as e:
#             print(f"Ошибка при взаимодействии с элементами игры: {e}")
#             driver.save_screenshot("game_element_not_found.png")
#             raise
#
#         time.sleep(32 * 60)
#
# finally:
#     print("Закрываем браузер...")
#     ## driver.quit()
#