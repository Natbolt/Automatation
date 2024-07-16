from HW7.Swag_Labs_v2.Pages.Shopmain import ShopmainPage
from HW7.Swag_Labs_v2.Pages.Shopcontainer import ShopContainer
import allure


@allure.epic("Saucedemo")
@allure.severity(severity_level='normal')
@allure.title("Оформление заказа в магазине")
@allure.description("Оформление заказа с необходимыми товарами с последующим сравнением стоимости")
@allure.feature('Тест 3')
def test_shop(chrome_browser):
    expected_total = "58.29"
    with allure.step("Открываем форму регистрации поьзователя находязейся на главной странице магазина"):
        shopmain = ShopmainPage(chrome_browser)
        shopmain.open()
    with allure.step("Заполняем поля регистрации пользователя"):
        shopmain.registration_fields()
    with allure.step("Ищем кнопки добавления выбранных товаров в корзину и кликаем их"):
        shopmain.buy_issue()
        shopmain.click_issue()
    with allure.step("Переходим в корзину"):
        shopmain.into_container()
    with allure.step("Переходим к оформлению заказа, нажав кнопку checkout"):
        container = ShopContainer(chrome_browser)
        container.checkout()
    with allure.step("Вводим данные получателя"):
        container.info()
    with allure.step("Получаем итоговую сумму заказа и выводим ее в нужном формате"):
        container.price()
    with allure.step("Сравниваем итоговую сумму с ожидаемой"):
        assert expected_total in container.price()
        print(f"Итоговая сумма равна ${container.price()}")
