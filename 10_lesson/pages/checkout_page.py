from selenium.webdriver.common.by import By
from .base_page import BasePage
from typing import Any


class CheckoutPage(BasePage):
    """Класс для страницы оформления заказа"""

    FIRST_NAME = (By.ID, "first-name")
    LAST_NAME = (By.ID, "last-name")
    POSTAL_CODE = (By.ID, "postal-code")
    CONTINUE_BUTTON = (By.ID, "continue")
    FINISH_BUTTON = (By.ID, "finish")
    COMPLETE_MESSAGE = (By.CLASS_NAME, "complete-header")

    def __init__(self, driver: Any) -> None:
        """Инициализация страницы оформления"""
        super().__init__(driver)

    def fill_info(self, first_name: str, last_name: str, postal_code: str) -> None:
        """
        Заполнение информации о покупателе

        Args:
            first_name: имя
            last_name: фамилия
            postal_code: почтовый индекс
        """
        self.send_keys(self.FIRST_NAME, first_name)
        self.send_keys(self.LAST_NAME, last_name)
        self.send_keys(self.POSTAL_CODE, postal_code)
        self.click(self.CONTINUE_BUTTON)

    def finish(self) -> None:
        """Завершение покупки"""
        self.click(self.FINISH_BUTTON)

    def get_complete_message(self) -> str:
        """
        Получение сообщения о завершении

        Returns:
            str: сообщение о завершении
        """
        return self.get_text(self.COMPLETE_MESSAGE)
