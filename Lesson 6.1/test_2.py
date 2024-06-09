from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from configuration import *

def test_calculator_form(chrome_browser):
    chrome_browser.get(URL_2)
    # Ввести значение 45 по локатору delay
    delay_input = chrome_browser.find_element(By.ID, "delay")
    delay_input.clear()
    delay_input.send_keys(45)
    # Нажимаем на кнопки:
    # 7
    chrome_browser.find_element(By.XPATH, "//span[text() = '7']").click()
    # +
    chrome_browser.find_element(By.XPATH, "//span[text() = '+']").click()
    # 8
    chrome_browser.find_element(By.XPATH, "//span[text() = '8']").click()
    # =
    chrome_browser.find_element(By.XPATH, "//span[text() = '=']").click()

    # Дождаться 45 секунд и вычислений
    WebDriverWait(chrome_browser, 46).until(EC.text_to_be_present_in_element((By.CLASS_NAME, "screen"), "15"))
    # Получение результата
    result_text = chrome_browser.find_element(By.CLASS_NAME, "screen").text

    # проверка отображения результата 15 через 45 секунд
    assert result_text == "15"
