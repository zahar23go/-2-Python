"""
Тест для проверки калькулятора с задержкой
Используется браузер Google Chrome
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


class TestCalculator:
    """Тест для проверки калькулятора с задержкой 45 секунд"""

    def setup_method(self):
        """Подготовка перед каждым тестом"""
        self.driver = webdriver.Chrome(
            service=ChromeService(ChromeDriverManager().install()))
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 10)

    def teardown_method(self):
        """Очистка после каждого теста"""
        if self.driver:
            self.driver.quit()

    def test_calculator_delay(self):
        """Тест проверки работы калькулятора с задержкой"""
        # Открываем страницу
        self.driver.get(
            "https://bonigarcia.dev/selenium-webdriver-java/"
            "slow-calculator.html")

        # Вводим значение задержки 45
        delay_input = self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "#delay")))
        delay_input.clear()
        delay_input.send_keys("45")

        # Нажимаем кнопки: 7 + 8 =
        self.driver.find_element(By.XPATH, "//span[text()='7']").click()
        self.driver.find_element(By.XPATH, "//span[text()='+']").click()
        self.driver.find_element(By.XPATH, "//span[text()='8']").click()
        self.driver.find_element(By.XPATH, "//span[text()='=']").click()

        # Ждем результат 15
        WebDriverWait(self.driver, 60).until(
            EC.text_to_be_present_in_element(
                (By.CSS_SELECTOR, ".screen"), "15")
        )

        # Проверяем результат
        result_text = self.driver.find_element(
            By.CSS_SELECTOR, ".screen").text
        assert result_text == "15", (
            f"Ожидался 15, получен {result_text}")
