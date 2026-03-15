from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from typing import Any, Tuple, Optional
from selenium.common.exceptions import TimeoutException, NoSuchElementException


class BasePage:
    """Базовый класс для всех страниц"""

    def __init__(self, driver: Any) -> None:
        """
        Инициализация базовой страницы

        Args:
            driver (Any): WebDriver instance
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open(self, url: str = None) -> None:
        """
        Открыть страницу
        
        Args:
            url (str): URL для открытия (если None, используется базовый URL)
        """
        if url is None:
            url = "https://www.saucedemo.com/"
        self.driver.get(url)

    def find_element(self, locator: Tuple[By, str]) -> Any:
        """
        Поиск элемента на странице

        Args:
            locator (Tuple[By, str]): локатор элемента

        Returns:
            Any: найденный элемент
        """
        return self.wait.until(EC.presence_of_element_located(locator))

    def click(self, locator: Tuple[By, str]) -> None:
        """
        Клик по элементу

        Args:
            locator (Tuple[By, str]): локатор элемента
        """
        self.find_element(locator).click()

    def send_keys(self, locator: Tuple[By, str], text: str) -> None:
        """
        Ввод текста в элемент

        Args:
            locator (Tuple[By, str]): локатор элемента
            text (str): текст для ввода
        """
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)

    def get_text(self, locator: Tuple[By, str]) -> str:
        """
        Получение текста элемента

        Args:
            locator (Tuple[By, str]): локатор элемента

        Returns:
            str: текст элемента
        """
        return self.find_element(locator).text

    def is_element_present(self, locator: Tuple[By, str]) -> bool:
        """
        Проверка наличия элемента на странице

        Args:
            locator (Tuple[By, str]): локатор элемента

        Returns:
            bool: True если элемент присутствует
        """
        try:
            self.driver.find_element(*locator)
            return True
        except NoSuchElementException:
            return False

    def get_current_url(self) -> str:
        """
        Получение текущего URL

        Returns:
            str: текущий URL
        """
        return self.driver.current_url