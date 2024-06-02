from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

firefox = webdriver.Firefox()

try:
    firefox.get(" http://the-internet.herokuapp.com/login")
    input_name = firefox.find_element(By.ID, "username").send_keys("tomsmith")
    sleep(1)
    input_pass = firefox.find_element(
        By.ID, "password").send_keys("SuperSecretPassword!")
    sleep(1)
    button = firefox.find_element(By.TAG_NAME, "button").click()
    sleep(2)
except Exception as ex:
    print(ex)
finally:
    firefox.quit()