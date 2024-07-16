from HW7.Calculator.Pages.Calcmainpage import CalcMain
import allure


@allure.epic("Calculator")
@allure.severity(severity_level='normal')
@allure.title("Работа калькулятора")
@allure.description("Поиск полей, ввод данных и вывод результата вычисления")
@allure.feature('Тест 2')
def test_calculator_assert(chrome_browser):
    delay = 45
    result = 15
    keys_press = '7+8='
    with allure.step("Открываем калькулятор, вводим значения и ожидаем результат"):
        calc = CalcMain(chrome_browser)
        calc.open()
        calc.set_delay(delay)
        calc.input_text(keys_press)
        calc.wait_result(delay, result)

    with allure.step("Сравниваем получившейся результат с ожидаемым"):
        assert calc.result_text() == str(result)