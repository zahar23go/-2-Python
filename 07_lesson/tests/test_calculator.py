from pages.calculator_page import CalculatorPage


class TestCalculator:
    """Тесты для калькулятора"""

    def test_calculator_addition(self, chrome_browser):
        """Тест проверки сложения с задержкой"""
        # Создаем объект страницы
        calculator_page = CalculatorPage(chrome_browser)

        # Открываем страницу
        calculator_page.open()

        # Устанавливаем задержку
        calculator_page.set_delay("45")

        # Выполняем вычисление 7 + 8
        calculator_page.click_button_7()
        calculator_page.click_button_plus()
        calculator_page.click_button_8()
        calculator_page.click_button_equals()

        # Получаем результат
        result = calculator_page.get_result()

        # Проверяем результат
        assert result == "15", f"Ожидалось 15, получено {result}"
