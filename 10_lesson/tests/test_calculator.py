import allure
from pages.calculator_page import CalculatorPage

@allure.title("Тест калькулятора")
@allure.description("Проверка работы калькулятора")
@allure.feature("Калькулятор")
@allure.severity(allure.severity_level.CRITICAL)
def test_calculator(driver):
    with allure.step("Открыть страницу калькулятора"):
        calculator_page = CalculatorPage(driver)
        calculator_page.open()
    
    with allure.step("Выполнить вычисления"):
        # Добавьте здесь ваши шаги
        pass
    
    with allure.step("Проверить результат"):
        assert True
