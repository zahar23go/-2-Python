from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from typing import Any
from .base_page import BasePage
import time


class CalculatorPage(BasePage):
    """Page Object для страницы калькулятора"""

    # Локаторы
    FIRST_NUMBER = (By.ID, "number1")
    SECOND_NUMBER = (By.ID, "number2")
    OPERATION = (By.ID, "selectOperation")
    CALCULATE_BUTTON = (By.ID, "calculateButton")
    RESULT = (By.ID, "numberAnswerField")
    INT_ONLY_CHECKBOX = (By.ID, "integerSelect")

    def __init__(self, driver: Any) -> None:
        """
        Инициализация страницы калькулятора

        Args:
            driver (Any): WebDriver instance
        """
        super().__init__(driver)

    def open(self) -> None:
        """Открыть страницу калькулятора"""
        self.driver.get("https://testsheepnz.github.io/BasicCalculator.html")
        time.sleep(2)  # Ждем загрузки страницы

    def calculate(self, num1: int, num2: int, operation: str = "0") -> str:
        """
        Выполнить вычисление

        Args:
            num1 (int): первое число
            num2 (int): второе число
            operation (str): операция (0 - +, 1 - -, 2 - *, 3 - /)

        Returns:
            str: результат вычисления
        """
        self.send_keys(self.FIRST_NUMBER, str(num1))
        self.send_keys(self.SECOND_NUMBER, str(num2))
        
        select = Select(self.find_element(self.OPERATION))
        select.select_by_value(operation)
        
        self.click(self.CALCULATE_BUTTON)
        time.sleep(1)  # Ждем вычисления
        
        return self.get_result()

    def get_result(self) -> str:
        """
        Получить результат вычисления

        Returns:
            str: результат
        """
        return self.get_text(self.RESULT)

    def set_integer_only(self, enable: bool = True) -> None:
        """
        Установить режим только целых чисел

        Args:
            enable (bool): True - включить, False - выключить
        """
        checkbox = self.find_element(self.INT_ONLY_CHECKBOX)
        if (enable and not checkbox.is_selected()) or (not enable and checkbox.is_selected()):
            self.click(self.INT_ONLY_CHECKBOX)