from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webelement import WebElement
from typing import Tuple, Any, List, Optional


class BasePage:
    \"\"\"Базовый класс для всех страниц\"\"\"

    def __init__(self, driver: Any) -> None:
        \"\"\"
        Инициализация базовой страницы

        Args:
            driver (Any): WebDriver instance
        \"\"\"
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def find_element(self, locator: Tuple[str, str], timeout: int = 10) -> WebElement:
        \"\"\"
        Поиск элемента с ожиданием

        Args:
            locator (Tuple[str, str]): кортеж (By, value)
            timeout (int): время ожидания в секундах

        Returns:
            WebElement: найденный элемент
        \"\"\"
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located(locator)
        )

    def find_elements(self, locator: Tuple[str, str], timeout: int = 10) -> List[WebElement]:
        \"\"\"
        Поиск всех элементов с ожиданием

        Args:
            locator (Tuple[str, str]): кортеж (By, value)
            timeout (int): время ожидания в секундах

        Returns:
            List[WebElement]: список найденных элементов
        \"\"\"
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_all_elements_located(locator)
        )

    def click(self, locator: Tuple[str, str], timeout: int = 10) -> None:
        \"\"\"
        Клик по элементу

        Args:
            locator (Tuple[str, str]): кортеж (By, value)
            timeout (int): время ожидания в секундах
        \"\"\"
        self.find_element(locator, timeout).click()

    def send_keys(self, locator: Tuple[str, str], text: str, timeout: int = 10) -> None:
        \"\"\"
        Ввод текста в элемент

        Args:
            locator (Tuple[str, str]): кортеж (By, value)
            text (str): текст для ввода
            timeout (int): время ожидания в секундах
        \"\"\"
        self.find_element(locator, timeout).send_keys(text)

    def get_text(self, locator: Tuple[str, str], timeout: int = 10) -> str:
        \"\"\"
        Получение текста элемента

        Args:
            locator (Tuple[str, str]): кортеж (By, value)
            timeout (int): время ожидания в секундах

        Returns:
            str: текст элемента
        \"\"\"
        return self.find_element(locator, timeout).text

    def is_element_present(self, locator: Tuple[str, str], timeout: int = 5) -> bool:
        \"\"\"
        Проверка наличия элемента на странице

        Args:
            locator (Tuple[str, str]): кортеж (By, value)
            timeout (int): время ожидания в секундах

        Returns:
            bool: True если элемент найден, иначе False
        \"\"\"
        try:
            self.find_element(locator, timeout)
            return True
        except:
            return False
