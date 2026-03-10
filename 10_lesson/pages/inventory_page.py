from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webelement import WebElement
from typing import List, Tuple, Any, Optional
from .base_page import BasePage


class InventoryPage(BasePage):
    \"\"\"Page Object для страницы инвентаря (списка товаров)\"\"\"

    # Локаторы
    PRODUCT_ITEM = (By.CLASS_NAME, "inventory_item")
    PRODUCT_NAME = (By.CLASS_NAME, "inventory_item_name")
    PRODUCT_PRICE = (By.CLASS_NAME, "inventory_item_price")
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, "button.btn_inventory")
    CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")
    SORT_DROPDOWN = (By.CLASS_NAME, "product_sort_container")
    MENU_BUTTON = (By.ID, "react-burger-menu-btn")
    LOGOUT_LINK = (By.ID, "logout_sidebar_link")

    def __init__(self, driver: Any) -> None:
        \"\"\"
        Инициализация страницы инвентаря

        Args:
            driver (Any): WebDriver instance
        \"\"\"
        super().__init__(driver)
        self.wait = WebDriverWait(driver, 10)

    def get_all_products(self) -> List[WebElement]:
        \"\"\"
        Получение списка всех товаров на странице

        Returns:
            List[WebElement]: список элементов товаров
        \"\"\"
        return self.wait.until(
            EC.presence_of_all_elements_located(self.PRODUCT_ITEM)
        )

    def add_product_to_cart(self, product_name: str) -> None:
        \"\"\"
        Добавление товара в корзину по его названию

        Args:
            product_name (str): название товара
        \"\"\"
        products = self.get_all_products()
        for product in products:
            name_element = product.find_element(*self.PRODUCT_NAME)
            if name_element.text == product_name:
                add_button = WebDriverWait(product, 5).until(
                    EC.element_to_be_clickable(self.ADD_TO_CART_BUTTON)
                )
                add_button.click()
                self.wait.until(
                    EC.presence_of_element_located(self.CART_BADGE)
                )
                return
        raise AssertionError(f"Товар '{product_name}' не найден на странице")

    def get_cart_count(self) -> int:
        \"\"\"
        Получение количества товаров в корзине

        Returns:
            int: количество товаров
        \"\"\"
        try:
            badge = self.wait.until(
                EC.presence_of_element_located(self.CART_BADGE)
            )
            return int(badge.text)
        except:
            return 0

    def sort_products(self, sort_option: str) -> None:
        \"\"\"
        Сортировка товаров

        Args:
            sort_option (str): опция сортировки (az, za, lohi, hilo)
        \"\"\"
        sort_map = {
            "az": "Name (A to Z)",
            "za": "Name (Z to A)",
            "lohi": "Price (low to high)",
            "hilo": "Price (high to low)"
        }
        dropdown = self.wait.until(
            EC.element_to_be_clickable(self.SORT_DROPDOWN)
        )
        dropdown.click()
        option = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, f"//option[text()='{sort_map[sort_option]}']"))
        )
        option.click()
        self.wait.until(
            EC.staleness_of(self.get_all_products()[0])
        )

    def logout(self) -> None:
        \"\"\"Выход из системы\"\"\"
        menu_button = self.wait.until(
            EC.element_to_be_clickable(self.MENU_BUTTON)
        )
        menu_button.click()
        logout_link = self.wait.until(
            EC.element_to_be_clickable(self.LOGOUT_LINK)
        )
        logout_link.click()
        self.wait.until(
            EC.presence_of_element_located((By.ID, "login-button"))
        )
