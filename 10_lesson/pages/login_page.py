from selenium.webdriver.common.by import By
from typing import Any
from .base_page import BasePage


class LoginPage(BasePage):
    \"\"\"Page Object для страницы авторизации\"\"\"

    # Локаторы
    USERNAME_INPUT = (By.ID, "user-name")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")
    ERROR_MESSAGE = (By.CSS_SELECTOR, "h3[data-test='error']")
    MENU_BUTTON = (By.ID, "react-burger-menu-btn")
    LOGOUT_LINK = (By.ID, "logout_sidebar_link")

    def __init__(self, driver: Any) -> None:
        \"\"\"
        Инициализация страницы авторизации

        Args:
            driver (Any): WebDriver instance
        \"\"\"
        super().__init__(driver)

    def login(self, username: str, password: str) -> None:
        \"\"\"
        Выполнение входа в систему

        Args:
            username (str): имя пользователя
            password (str): пароль
        \"\"\"
        self.send_keys(self.USERNAME_INPUT, username)
        self.send_keys(self.PASSWORD_INPUT, password)
        self.click(self.LOGIN_BUTTON)

    def get_error_message(self) -> str:
        \"\"\"
        Получение текста сообщения об ошибке

        Returns:
            str: текст ошибки или пустая строка
        \"\"\"
        if self.is_element_present(self.ERROR_MESSAGE):
            return self.get_text(self.ERROR_MESSAGE)
        return ""

    def is_login_error_displayed(self) -> bool:
        \"\"\"
        Проверка отображения ошибки входа

        Returns:
            bool: True если ошибка отображается
        \"\"\"
        return self.is_element_present(self.ERROR_MESSAGE)

    def logout(self) -> None:
        \"\"\"Выход из системы\"\"\"
        self.click(self.MENU_BUTTON)
        self.click(self.LOGOUT_LINK)
