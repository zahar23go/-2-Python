from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementClickInterceptedException
import time


class CalculatorPage:
    """Page Object для страницы калькулятора"""

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 50)

    # Локаторы
    DELAY_INPUT = (By.CSS_SELECTOR, "#delay")
    RESULT_DISPLAY = (By.CSS_SELECTOR, ".screen")
    BUTTON_7 = (By.XPATH, "//span[text()='7']")
    BUTTON_8 = (By.XPATH, "//span[text()='8']")
    BUTTON_PLUS = (By.XPATH, "//span[text()='+']")
    BUTTON_EQUALS = (By.XPATH, "//span[text()='=']")

    def open(self):
        """Открыть страницу калькулятора"""
        self.driver.get(
            "https://bonigarcia.dev/selenium-webdriver-java/"
            "slow-calculator.html"
        )

    def set_delay(self, seconds):
        """Установить задержку"""
        delay_input = self.driver.find_element(*self.DELAY_INPUT)
        delay_input.clear()
        delay_input.send_keys(seconds)

    def click_button_7(self):
        """Нажать кнопку 7"""
        self._safe_click(self.BUTTON_7)

    def click_button_8(self):
        """Нажать кнопку 8"""
        self._safe_click(self.BUTTON_8)

    def click_button_plus(self):
        """Нажать кнопку +"""
        self._safe_click(self.BUTTON_PLUS)

    def click_button_equals(self):
        """Нажать кнопку = с ожиданием кликабельности"""
        time.sleep(1)  # Небольшая пауза перед кликом
        self._safe_click(self.BUTTON_EQUALS)

    def _safe_click(self, locator):
        """Безопасный клик по элементу с обработкой перехвата"""
        try:
            # Ждем, пока элемент станет кликабельным
            element = self.wait.until(
                EC.element_to_be_clickable(locator)
            )
            element.click()
        except ElementClickInterceptedException:
            # Если обычный клик не сработал, пробуем через JavaScript
            element = self.driver.find_element(*locator)
            self.driver.execute_script("arguments[0].click();", element)

    def get_result(self):
        """Получить результат вычисления"""
        self.wait.until(
            EC.text_to_be_present_in_element(self.RESULT_DISPLAY, "15")
        )
        return self.driver.find_element(*self.RESULT_DISPLAY).text
