from selenium import webdriver
from time import sleep

chrome = webdriver.Chrome()


try:
    count = 0
    chrome.get("http://uitestingplayground.com/dynamicid")

    # Кликаем на синюю кнопку
    blue_button = chrome.find_element(
        "xpath", '//button[text()="Button with Dynamic ID"]').click()
    
    # Кликаем на синюю кнопку 3 раза
    for _ in range(3):
        blue_button = chrome.find_element(
            "xpath", '//button[text()="Button with Dynamic ID"]').click()
        
        count = count + 1
        sleep(2)
        print(count)

except Exception as ex:
    print(ex)
finally:
    chrome.quit()

