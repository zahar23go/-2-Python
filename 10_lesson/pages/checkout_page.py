from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from typing import Any
from .base_page import BasePage


class CheckoutPage(BasePage):
    \"\"\"Page Object для страницы оформления заказа\"\"\"

    # Локаторы
    FIRST_NAME = (By.ID, "first-name")
    LAST_NAME = (By.ID, "last-name")
    POSTAL_CODE = (By.ID, "postal-code")
    CONTINUE_BUTTON = (By.ID, "continue")
    FINISH_BUTTON = (By.ID, "finish")
    CANCEL_BUTTON = (By.ID, "cancel")
    COMPLETE_HEADER = (By.CLASS_NAME, "complete-header")
    SUMMARY_TOTAL = (By.CLASS_NAME, "summary_total_label")

    def __init__(self, driver: Any) -> None:
        \"\"\"
        Инициализация страницы оформления заказа

        Args:
            driver (Any): WebDriver instance
        \"\"\"
        super().__init__(driver)

    def fill_checkout_info(self, first_name: str, last_name: str, postal_code: str) -> None:
        \"\"\"
        Заполнение информации для заказа

        Args:
            first_name (str): имя
            last_name (str): фамилия
            postal_code (str): почтовый индекс
        \"\"\"
        self.send_keys(self.FIRST_NAME, first_name)
        self.send_keys(self.LAST_NAME, last_name)
        self.send_keys(self.POSTAL_CODE, postal_code)

    def continue_checkout(self) -> None:
        \"\"\"Продолжить оформление заказа\"\"\"
        self.click(self.CONTINUE_BUTTON)

    def finish_checkout(self) -> None:
        \"\"\"Завершить оформление заказа\"\"\"
        self.click(self.FINISH_BUTTON)

    def cancel_checkout(self) -> None:
        \"\"\"Отменить оформление заказа\"\"\"
        self.click(self.CANCEL_BUTTON)

    def get_complete_header(self) -> str:
        \"\"\"
        Получение заголовка завершения заказа

        Returns:
            str: текст заголовка
        \"\"\"
        return self.get_text(self.COMPLETE_HEADER)

    def get_total_price(self) -> str:
        \"\"\"
        Получение итоговой суммы заказа

        Returns:
            str: текст с итоговой суммой
        \"\"\"
        return self.get_text(self.SUMMARY_TOTAL)

    def is_checkout_complete(self) -> bool:
        \"\"\"
        Проверка завершения оформления заказа

        Returns:
            bool: True если заказ оформлен, иначе False
        \"\"\"
        return self.is_element_present(self.COMPLETE_HEADER)
