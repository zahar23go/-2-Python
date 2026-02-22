"""
Тест для проверки покупки в интернет-магазине
Используется браузер Mozilla Firefox
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager


class TestShop:
    """Тест для проверки покупки и итоговой суммы"""

    def setup_method(self):
        """Подготовка перед каждым тестом"""
        try:
            self.driver = webdriver.Firefox(
                service=FirefoxService(GeckoDriverManager().install()))
            self.driver.maximize_window()
            self.wait = WebDriverWait(self.driver, 10)
        except Exception as e:
            print(f"Ошибка при запуске Firefox: {e}")
            self.driver = webdriver.Firefox()
            self.driver.maximize_window()
            self.wait = WebDriverWait(self.driver, 10)

    def teardown_method(self):
        """Очистка после каждого теста"""
        if self.driver:
            self.driver.quit()

    def test_shopping_cart_total(self):
        """Тест проверки итоговой суммы"""
        try:
            # Открываем сайт
            self.driver.get("https://www.saucedemo.com/")

            # Авторизация
            username = self.wait.until(
                EC.presence_of_element_located((By.ID, "user-name")))
            username.send_keys("standard_user")

            password = self.driver.find_element(By.ID, "password")
            password.send_keys("secret_sauce")
            self.driver.find_element(By.ID, "login-button").click()

            # Ждем загрузку товаров
            self.wait.until(
                EC.presence_of_element_located(
                    (By.CLASS_NAME, "inventory_list")))

            # Добавляем товары
            items = [
                "sauce-labs-backpack",
                "sauce-labs-bolt-t-shirt",
                "sauce-labs-onesie"
            ]
            for item in items:
                btn = self.driver.find_element(
                    By.ID, f"add-to-cart-{item}")
                btn.click()

            # Переходим в корзину
            self.driver.find_element(
                By.CLASS_NAME, "shopping_cart_link").click()

            # Checkout
            checkout_btn = self.wait.until(
                EC.element_to_be_clickable((By.ID, "checkout")))
            checkout_btn.click()

            # Заполняем форму
            first_name = self.wait.until(
                EC.presence_of_element_located((By.ID, "first-name")))
            first_name.send_keys("Иван")

            last_name = self.driver.find_element(By.ID, "last-name")
            last_name.send_keys("Петров")

            postal = self.driver.find_element(By.ID, "postal-code")
            postal.send_keys("123456")

            continue_btn = self.driver.find_element(By.ID, "continue")
            continue_btn.click()

            # Проверяем итог
            self.wait.until(
                EC.presence_of_element_located(
                    (By.CLASS_NAME, "summary_total_label")))
            total = self.driver.find_element(
                By.CLASS_NAME, "summary_total_label").text
            amount = total.replace("Total: $", "")
            assert amount == "58.29", f"Ожидалось 58.29, получено {amount}"

        except Exception as e:
            self.driver.save_screenshot("error_screenshot.png")
            raise e
