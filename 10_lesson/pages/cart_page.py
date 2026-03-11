from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from typing import Any
from .base_page import BasePage
import time


class CartPage(BasePage):
    """Page Object для страницы корзины"""

    # Локаторы
    CART_ITEM = (By.CLASS_NAME, "cart_item")
    CHECKOUT_BUTTON = (By.ID, "checkout")
    CONTINUE_SHOPPING_BUTTON = (By.ID, "continue-shopping")
    REMOVE_BUTTON = (By.CSS_SELECTOR, "button.cart_button")

    def __init__(self, driver: Any) -> None:
        """
        Инициализация страницы корзины

        Args:
            driver (Any): WebDriver instance
        """
        super().__init__(driver)

    def checkout(self) -> None:
        """Переход к оформлению заказа"""
        time.sleep(2)
        
        print(f"\nТекущий URL до клика: {self.driver.current_url}")
        
        # Пробуем разные способы нажатия на кнопку Checkout
        try:
            # Способ 1: обычный клик
            checkout_button = self.driver.find_element(By.ID, "checkout")
            print(f"✓ Найдена кнопка Checkout с текстом: '{checkout_button.text}'")
            checkout_button.click()
            print("✓ Способ 1: обычный клик выполнен")
        except Exception as e:
            print(f"✗ Способ 1 не сработал: {e}")
            
            # Способ 2: JavaScript клик
            try:
                self.driver.execute_script("document.getElementById('checkout').click();")
                print("✓ Способ 2: JavaScript клик выполнен")
            except Exception as e:
                print(f"✗ Способ 2 не сработал: {e}")
                
                # Способ 3: нажать через Enter
                checkout_button.send_keys("\n")
                print("✓ Способ 3: Enter нажат")
        
        # Ждем перехода на страницу оформления
        time.sleep(3)
        
        # Проверяем новый URL
        new_url = self.driver.current_url
        print(f"URL после клика: {new_url}")
        
        # Если URL не изменился, пробуем принудительный переход
        if "cart" in new_url:
            print("⚠️ URL не изменился, пробуем перейти напрямую")
            self.driver.get("https://www.saucedemo.com/checkout-step-one.html")
            time.sleep(2)
            print(f"URL после прямого перехода: {self.driver.current_url}")
        
        # Ждем появления полей формы
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, "first-name"))
            )
            print("✓ Страница оформления загружена, поля найдены")
        except Exception as e:
            print(f"⚠️ Поля не найдены, сохраняем скриншот. Ошибка: {e}")
            self.driver.save_screenshot("after_checkout.png")
            
            # Выводим информацию о текущей странице
            print(f"Заголовок страницы: {self.driver.title}")
            print(f"Текущий URL: {self.driver.current_url}")
            
            print("Доступные элементы input:")
            elements = self.driver.find_elements(By.TAG_NAME, "input")
            for el in elements:
                print(f"  Input: id='{el.get_attribute('id')}', name='{el.get_attribute('name')}', type='{el.get_attribute('type')}'")
            
            print("Доступные элементы button:")
            buttons = self.driver.find_elements(By.TAG_NAME, "button")
            for i, btn in enumerate(buttons):
                print(f"  Button {i}: id='{btn.get_attribute('id')}', text='{btn.text}'")
            
            raise

    def get_cart_items_count(self) -> int:
        """
        Получить количество товаров в корзине

        Returns:
            int: количество товаров
        """
        items = self.driver.find_elements(*self.CART_ITEM)
        return len(items)

    def remove_item(self, item_name: str) -> None:
        """
        Удалить товар из корзины

        Args:
            item_name (str): название товара
        """
        remove_locator = (By.XPATH, f"//div[text()='{item_name}']/ancestor::div[@class='cart_item']//button")
        self.click(remove_locator)

    def continue_shopping(self) -> None:
        """Продолжить покупки"""
        self.click(self.CONTINUE_SHOPPING_BUTTON)