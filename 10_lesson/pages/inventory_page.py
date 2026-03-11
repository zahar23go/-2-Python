
from selenium.webdriver.common.by import By
from typing import Any
from .base_page import BasePage
import time


class InventoryPage(BasePage):
    """Page Object для страницы инвентаря (списка товаров)"""

    # Локаторы
    INVENTORY_LIST = (By.CLASS_NAME, "inventory_list")
    INVENTORY_ITEM = (By.CLASS_NAME, "inventory_item")
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, "button.btn_inventory")
    CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")
    CART_LINK = (By.CLASS_NAME, "shopping_cart_link")
    SORT_CONTAINER = (By.CLASS_NAME, "product_sort_container")
    
    def __init__(self, driver: Any) -> None:
        """
        Инициализация страницы инвентаря

        Args:
            driver (Any): WebDriver instance
        """
        super().__init__(driver)
    
    def add_item_to_cart(self, item_name: str) -> None:
        """
        Добавить товар в корзину по его имени

        Args:
            item_name (str): название товара
        """
        # Формируем динамический локатор для кнопки добавления конкретного товара
        add_button = (By.XPATH, f"//div[text()='{item_name}']/ancestor::div[@class='inventory_item']//button")
        self.click(add_button)
        print(f"✓ Товар '{item_name}' добавлен в корзину")
        time.sleep(1)
    
    def get_cart_count(self) -> int:
        """
        Получить количество товаров в корзине

        Returns:
            int: количество товаров
        """
        if self.is_element_present(self.CART_BADGE):
            return int(self.get_text(self.CART_BADGE))
        return 0
    
    def go_to_cart(self) -> None:
        """Перейти в корзину"""
        time.sleep(1)
        
        # Находим ссылку на корзину
        cart_link = self.driver.find_element(By.CLASS_NAME, "shopping_cart_link")
        print("✓ Нашли иконку корзины")
        
        # Кликаем
        cart_link.click()
        time.sleep(2)
        
        # Проверяем результат
        current_url = self.driver.current_url
        print(f"URL после перехода: {current_url}")
        
        # Если не перешли, пробуем еще раз
        if "cart" not in current_url:
            print("⚠️ Первый клик не сработал, пробуем через JavaScript...")
            self.driver.execute_script("document.querySelector('.shopping_cart_link').click()")
            time.sleep(2)
            print(f"URL после JavaScript: {self.driver.current_url}")