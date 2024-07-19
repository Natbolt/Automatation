from HW7.Data_types_v2.Pages.Mainpage import MainPage
from HW7.Data_types_v2.Pages.Datafildes import DataFild
import allure


@allure.epic("Data_types - registration form")
@allure.severity(severity_level='noemal')
@allure.title("Заполнение формы")
@allure.description("Заполнение формы различными данными и проверка валидности")
@allure.feature('Тест 1')
def test_assertion(chrome_browser):
    with allure.step("Открываем форму, находим и заполняем поля, подтверждаем заполнение формы"):
          main_page = MainPage(chrome_browser)
          main_page.open()
          main_page.find_fields()
          main_page.filling_in_the_fields()
          main_page.click_submit_button()

    with allure.step("Получаем заполненные поля"):
        data_fild = DataFild(chrome_browser)
        data_fild.find_fields()
        data_fild.get_class_zipcode()
        data_fild.get_class_first_name()
        data_fild.get_class_last_name()
        data_fild.get_class_address()
        data_fild.get_class_email()
        data_fild.get_class_phone()
        data_fild.get_class_city()
        data_fild.get_class_country()
        data_fild.get_class_jobposition()
        data_fild.get_class_company()

    with allure.step("Проверяем, что в классах есть ожидаемый результат"):
        assert "success" in data_fild.get_class_first_name()
        assert "success" in data_fild.get_class_last_name()
        assert "success" in data_fild.get_class_address()
        assert "success" in data_fild.get_class_email()
        assert "success" in data_fild.get_class_phone()
        assert "success" in data_fild.get_class_city()
        assert "success" in data_fild.get_class_country()
        assert "success" in data_fild.get_class_jobposition()
        assert "success" in data_fild.get_class_company()
        assert "danger" in data_fild.get_class_zipcode()
    