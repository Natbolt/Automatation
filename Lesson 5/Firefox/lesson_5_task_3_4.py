import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

firefox = webdriver.Firefox()

try:
    firefox.get("http://the-internet.herokuapp.com/entry_ad")
    # Ждем, пока модальное окно не появится и кнопка "Close" станет кликабельной
    wait = WebDriverWait(firefox, 10)
    modal_window = wait.until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, ".modal")))
    close_button = wait.until(EC.element_to_be_clickable(
        (By.CSS_SELECTOR, ".modal-footer")))
    time.sleep(3)
    # Нажимаем кнопку "Close" в модальном окне
    close_button.click()
    time.sleep(2)
except Exception as ex:
    print(ex)
finally:
    firefox.quit()