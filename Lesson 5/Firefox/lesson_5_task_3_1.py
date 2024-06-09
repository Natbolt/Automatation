from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

firefox = webdriver.Firefox()

try:
    firefox.get(" http://the-internet.herokuapp.com/add_remove_elements/")

    # Нажимаем на кнопку Add Element 5 раз
    for _ in range(5):
        add_button = firefox.find_element(
            By.XPATH, '//button[text()="Add Element"]').click()
        sleep (1)
    # Собираем список кнопок Delete
        firefox_delete_buttons = firefox.find_elements(
            "xpath", '//button[text()="Delete"]')
        
    # Выводим на экран размер списка
    print(
        f"Размер списка кнопок Delete в Firefox: {len(firefox_delete_buttons)}")
    
except Exception as ex:
    print(ex)
finally:
    firefox.quit()