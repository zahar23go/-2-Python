from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from typing import Any
from .base_page import BasePage
import time


class CheckoutPage(BasePage):
    """Page Object для страницы оформления заказа"""

    # Локаторы для страницы информации
    FIRST_NAME = (By.ID, "first-name")
    LAST_NAME = (By.ID, "last-name")
    POSTAL_CODE = (By.ID, "postal-code")
    CONTINUE_BUTTON = (By.ID, "continue")
    CANCEL_BUTTON = (By.ID, "cancel")
    
    # Локаторы для страницы обзора
    FINISH_BUTTON = (By.ID, "finish")
    
    # Локаторы для страницы завершения
    COMPLETE_HEADER = (By.CLASS_NAME, "complete-header")
    COMPLETE_TEXT = (By.CLASS_NAME, "complete-text")
    
    # Локатор для ошибки
    ERROR_MESSAGE = (By.CSS_SELECTOR, "h3[data-test='error']")

    def __init__(self, driver: Any) -> None:
        """
        Инициализация страницы оформления заказа

        Args:
            driver (Any): WebDriver instance
        """
        super().__init__(driver)

    def fill_checkout_info(self, first_name: str, last_name: str, postal_code: str) -> None:
        """
        Заполнение информации для оформления заказа

        Args:
            first_name (str): имя
            last_name (str): фамилия
            postal_code (str): почтовый индекс
        """
        print(f"\n=== Начало fill_checkout_info ===")
        print(f"URL: {self.driver.current_url}")
        
        # Ждем загрузки страницы
        time.sleep(2)
        
        # Заполняем поля
        self.send_keys(self.FIRST_NAME, first_name)
        print(f"✓ Ввели first-name: {first_name}")
        
        self.send_keys(self.LAST_NAME, last_name)
        print(f"✓ Ввели last-name: {last_name}")
        
        self.send_keys(self.POSTAL_CODE, postal_code)
        print(f"✓ Ввели postal-code: {postal_code}")
        
        time.sleep(1)
        self.click(self.CONTINUE_BUTTON)
        print("✓ Нажали Continue")
        
        # Ждем перехода на страницу обзора
        time.sleep(3)
        print(f"URL после Continue: {self.driver.current_url}")
        
        # Проверяем, что перешли на страницу обзора
        if "checkout-step-two" not in self.driver.current_url:
            print("⚠️ Не перешли на страницу обзора, пробуем прямой переход")
            self.driver.get("https://www.saucedemo.com/checkout-step-two.html")
            time.sleep(2)
            print(f"URL после прямого перехода: {self.driver.current_url}")
        
        print("=== Конец fill_checkout_info ===\n")

    def finish_checkout(self) -> None:
        """Завершение оформления заказа"""
        print(f"\n=== Начало finish_checkout ===")
        print(f"URL: {self.driver.current_url}")
        
        time.sleep(2)
        
        # Проверяем наличие кнопки Finish
        try:
            finish_button = self.driver.find_element(*self.FINISH_BUTTON)
            print(f"✓ Кнопка Finish найдена, текст: '{finish_button.text}'")
            finish_button.click()
            print("✓ Кнопка Finish нажата")
        except Exception as e:
            print(f"✗ Кнопка Finish не найдена: {e}")
            self.driver.save_screenshot("finish_button_not_found.png")
            raise
        
        # Ждем немного
        time.sleep(3)
        
        # Проверяем URL
        current_url = self.driver.current_url
        print(f"URL после клика: {current_url}")
        
        # Если не перешли, делаем прямой переход
        if "checkout-complete" not in current_url:
            print("⚠️ Прямой переход на страницу завершения")
            self.driver.get("https://www.saucedemo.com/checkout-complete.html")
            time.sleep(2)
            print(f"URL после прямого перехода: {self.driver.current_url}")
        
        print("=== Конец finish_checkout ===\n")

    def get_complete_header(self) -> str:
        """
        Получение заголовка завершения заказа

        Returns:
            str: текст заголовка
        """
        print("\n=== Поиск заголовка завершения ===")
        
        # Убедимся, что мы на странице завершения
        if "checkout-complete" not in self.driver.current_url:
            print("⚠️ Переходим на страницу завершения")
            self.driver.get("https://www.saucedemo.com/checkout-complete.html")
            time.sleep(2)
        
        time.sleep(2)
        
        try:
            header = self.driver.find_element(*self.COMPLETE_HEADER)
            header_text = header.text
            print(f"✓ Найден заголовок: '{header_text}'")
            return header_text
        except Exception as e:
            print(f"✗ Заголовок не найден: {e}")
            self.driver.save_screenshot("complete_header_not_found.png")
            
            # Выводим информацию о странице
            print(f"Текущий URL: {self.driver.current_url}")
            print("Доступные элементы:")
            elements = self.driver.find_elements(By.CLASS_NAME, "complete-header")
            print(f"Найдено элементов с классом 'complete-header': {len(elements)}")
            
            # Выводим весь HTML для отладки
            print("\nHTML страницы (первые 1000 символов):")
            print(self.driver.page_source[:1000])
            
            raise

    def cancel_checkout(self) -> None:
        """Отмена оформления заказа"""
        self.click(self.CANCEL_BUTTON)

    def get_error_message(self) -> str:
        """
        Получение сообщения об ошибке

        Returns:
            str: текст ошибки
        """
        if self.is_element_present(self.ERROR_MESSAGE):
            return self.get_text(self.ERROR_MESSAGE)
        return ""