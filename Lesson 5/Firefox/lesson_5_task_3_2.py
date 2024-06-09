from selenium import webdriver
from time import sleep

firefox = webdriver.Firefox()

try:
    count = 0
    firefox.get("http://uitestingplayground.com/dynamicid")
    # Кликаем на синюю кнопку
    blue_button = firefox.find_element(
        "xpath", '//button[text()="Button with Dynamic ID"]').click()
   
    # Кликаем на синюю кнопку 3 раза
    for _ in range(3):
        blue_button = firefox.find_element(
            "xpath", '//button[text()="Button with Dynamic ID"]').click()
        count = count + 1
        sleep(2)
        print(count)

except Exception as ex:
    print(ex)
finally:
    firefox.quit()
    

