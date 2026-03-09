from selenium.webdriver.common.by import By
from .base_page import BasePage
from typing import Any


class LoginPage(BasePage):
    """Класс для страницы авторизации"""

    USERNAME_INPUT = (By.ID, "user-name")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")
    ERROR_MESSAGE = (By.CSS_SELECTOR, "[data-test='error']")

    def __init__(self, driver: Any) -> None:
        """Инициализация страницы авторизации"""
        super().__init__(driver)

    def open(self) -> None:
        """Открытие страницы авторизации"""
        self.driver.get("https://www.saucedemo.com/")

    def login(self, username: str, password: str) -> None:
        """
        Авторизация пользователя

        Args:
            username: имя пользователя
            password: пароль
        """
        self.send_keys(self.USERNAME_INPUT, username)
        self.send_keys(self.PASSWORD_INPUT, password)
        self.click(self.LOGIN_BUTTON)

    def get_error_message(self) -> str:
        """
        Получение сообщения об ошибке

        Returns:
            str: текст ошибки
        """
        return self.get_text(self.ERROR_MESSAGE)
