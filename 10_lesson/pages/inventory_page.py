from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .base_page import BasePage
from typing import Any
import time


class InventoryPage(BasePage):
    """Класс для страницы с товарами"""

    CART_LINK = (By.CLASS_NAME, "shopping_cart_link")
    CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")
    
    def __init__(self, driver: Any) -> None:
        """Инициализация страницы товаров"""
        super().__init__(driver)

    def add_to_cart(self, item_name: str) -> None:
        """
        Добавление товара в корзину
        """
        print(f"\n--- Добавляем товар: {item_name} ---")
        
        # Соответствие товаров их ID
        item_ids = {
            "Sauce Labs Backpack": "sauce-labs-backpack",
            "Sauce Labs Bike Light": "sauce-labs-bike-light",
        }
        
        if item_name not in item_ids:
            print(f" Неизвестный товар: {item_name}")
            return
            
        item_id = item_ids[item_name]
        add_button_id = f"add-to-cart-{item_id}"
        
        try:
            button = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, add_button_id))
            )
            
            print(f"Нашли кнопку: {add_button_id}")
            self.driver.execute_script("arguments[0].scrollIntoView(true);", button)
            time.sleep(1)
            self.driver.execute_script("arguments[0].click();", button)
            print(" JavaScript клик выполнен")
            time.sleep(2)
            
        except Exception as e:
            print(f" Ошибка: {e}")

    def go_to_cart(self) -> None:
        """Переход в корзину"""
        print("\n--- Переход в корзину ---")
        
        time.sleep(2)
        
        try:
            # Проверяем бейдж корзины
            badge = self.driver.find_element(*self.CART_BADGE)
            items_count = badge.text
            print(f"Товаров в корзине: {items_count}")
            
            # Несколько способов перехода в корзину
            print("Пробуем перейти в корзину...")
            
            # Способ 1: Прямой переход по URL
            self.driver.get("https://www.saucedemo.com/cart.html")
            time.sleep(2)
            
            if "cart" in self.driver.current_url.lower():
                print(" Успешно перешли в корзину через прямой URL!")
                return
                
        except Exception as e:
            print(f"Ошибка: {e}")
            
        # Если прямой URL не сработал, пробуем клик
        try:
            cart_link = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(self.CART_LINK)
            )
            
            print("Клик по ссылке корзины")
            cart_link.click()
            time.sleep(3)
            
            if "cart" in self.driver.current_url.lower():
                print(" Успешно перешли в корзину через клик!")
            else:
                print(" Не удалось перейти в корзину")
                
        except Exception as e:
            print(f"Ошибка при клике: {e}")
            # Последний шанс - прямой URL
            self.driver.get("https://www.saucedemo.com/cart.html")
            time.sleep(2)
            print(f"URL после прямого перехода: {self.driver.current_url}")
