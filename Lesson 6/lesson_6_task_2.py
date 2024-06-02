from selenium import webdriver


driver = webdriver.Firefox()

try:
    driver.get("http://uitestingplayground.com/textinput")
    button_name = driver.find_element(
        "id", "newButtonName").send_keys("SkyPro")
    confirm_button_name = driver.find_element("id", "updatingButton").click()
    print(driver.find_element("id", "updatingButton").text)

except Exception as ex:
    print(ex)
finally:
    driver.quit()