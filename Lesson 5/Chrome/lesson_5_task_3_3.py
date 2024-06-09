from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

chrome = webdriver.Chrome()

try:
    chrome.get("http://uitestingplayground.com/classattr")
    
    # Запускаем скрипт 3 раза
    for _ in range(3):
        # Кликаем на синюю кнопку
        blue_button = chrome.find_element(
            By.CSS_SELECTOR, 'button.btn-primary')
        blue_button.click()
        sleep(5)
    # Кликаем на ок в модальном окне
        chrome.switch_to.alert.accept()      


except Exception as ex:
    print(ex)
finally:
    chrome.quit()