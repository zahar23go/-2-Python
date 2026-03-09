from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from typing import Tuple, Any


class BasePage:
    """Базовый класс для всех страниц"""

    def __init__(self, driver: Any) -> None:
        """
        Инициализация базовой страницы

        Args:
            driver: WebDriver instance
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def find_element(self, locator: Tuple[str, str], timeout: int = 10) -> Any:
        """
        Поиск элемента с ожиданием

        Args:
            locator: кортеж (By, value)
            timeout: время ожидания в секундах

        Returns:
            WebElement: найденный элемент
        """
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located(locator)
        )

    def click(self, locator: Tuple[str, str], timeout: int = 10) -> None:
        """
        Клик по элементу

        Args:
            locator: кортеж (By, value)
            timeout: время ожидания в секундах
        """
        self.find_element(locator, timeout).click()

    def send_keys(self, locator: Tuple[str, str], text: str, timeout: int = 10) -> None:
        """
        Ввод текста в элемент

        Args:
            locator: кортеж (By, value)
            text: текст для ввода
            timeout: время ожидания в секундах
        """
        self.find_element(locator, timeout).send_keys(text)

    def get_text(self, locator: Tuple[str, str], timeout: int = 10) -> str:
        """
        Получение текста элемента

        Args:
            locator: кортеж (By, value)
            timeout: время ожидания в секундах

        Returns:
            str: текст элемента
        """
        return self.find_element(locator, timeout).text
