from selenium.webdriver.common.by import By
from HW7.constants import Shop_URL
import allure


class ShopmainPage:
    def __init__(self, browser):
        self.browser = browser

    @allure.step("Открываем главную страницу магазина")
    def open(self):
        self.browser.get(Shop_URL)

    @allure.step("Заполняем поля")
    def registration_fields(self):
        self._name = (By.ID, "user-name")
        self._pass = (By.ID, "password")
        self._log_button = (By.ID, "login-button")
        self.browser.find_element(*self._name).send_keys("standard_user")
        self.browser.find_element(*self._pass).send_keys("secret_sauce")
        self.browser.find_element(*self._log_button).click()

    @allure.step("Ищем кнопки добавления товаров в корзину")
    def buy_issue(self):
        self.Sauce_Labs_Backpack = (By.ID, "add-to-cart-sauce-labs-backpack")
        self.Sauce_Labs_Bolt_TShirt = (By.ID, "add-to-cart-sauce-labs-bolt-t-shirt")
        self.Sauce_Labs_Onesie = (By.ID, "add-to-cart-sauce-labs-onesie")

    @allure.step("Добавляем товары в корзину")
    def click_issue(self):
        self.browser.find_element(*self.Sauce_Labs_Backpack).click()
        self.browser.find_element(*self.Sauce_Labs_Bolt_TShirt).click()
        self.browser.find_element(*self.Sauce_Labs_Onesie).click()

    @allure.step("Переходим в корзину и оформляем заказ")
    def into_container(self):
        self.Container = (By.ID, "shopping_cart_container")
        self.browser.find_element(*self.Container).click()
