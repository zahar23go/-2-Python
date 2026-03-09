from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .base_page import BasePage
from typing import Any


class CartPage(BasePage):
    """Класс для страницы корзины"""

    CHECKOUT_BUTTON_ID = (By.ID, "checkout")
    CHECKOUT_BUTTON_DATA_TEST = (By.CSS_SELECTOR, "[data-test='checkout']")
    CHECKOUT_BUTTON_CLASS = (By.CLASS_NAME, "btn_action")
    CHECKOUT_BUTTON_XPATH = (By.XPATH, "//button[contains(text(), 'Checkout')]")
    CHECKOUT_BUTTON_NAME = (By.NAME, "checkout")

    CART_ITEMS = (By.CLASS_NAME, "cart_item")
    CONTINUE_SHOPPING = (By.ID, "continue-shopping")
    CART_LIST = (By.CLASS_NAME, "cart_list")

    def __init__(self, driver: Any) -> None:
        """Инициализация страницы корзины"""
        super().__init__(driver)

    def debug_page(self) -> None:
        """Отладка страницы - вывод всей информации"""
        print("\n=== ОТЛАДКА СТРАНИЦЫ КОРЗИНЫ ===")
        print(f"URL: {self.driver.current_url}")
        print(f"Заголовок: {self.driver.title}")

        self.driver.save_screenshot("cart_page_debug.png")
        print("Скриншот сохранен как cart_page_debug.png")

        with open("cart_page.html", "w", encoding="utf-8") as f:
            f.write(self.driver.page_source)
        print("HTML сохранен как cart_page.html")

    def checkout(self) -> None:
        """Оформление заказа с ожиданием"""
        locators = [
            self.CHECKOUT_BUTTON_ID,
            self.CHECKOUT_BUTTON_DATA_TEST,
            self.CHECKOUT_BUTTON_CLASS,
            self.CHECKOUT_BUTTON_XPATH,
            self.CHECKOUT_BUTTON_NAME
        ]

        print("\n=== ПОИСК КНОПКИ CHECKOUT ===")
        for locator in locators:
            try:
                print(f"Пробуем локатор: {locator}")
                element = WebDriverWait(self.driver, 3).until(
                    EC.presence_of_element_located(locator)
                )
                print("   Элемент найден!")
                print(f"    Текст: '{element.text}'")
                print(f"    Отображается: {element.is_displayed()}")

                if element.is_displayed() and element.is_enabled():
                    print("   Элемент видим и доступен, кликаем")
                    element.click()
                    return
                else:
                    print("   Элемент не видим или не доступен")
            except Exception as e:
                print(f"   Не найден: {type(e).__name__}")
                continue

        raise Exception("Не удалось найти кнопку Checkout ни по одному локатору")

    def get_items_count(self) -> int:
        """
        Получение количества товаров в корзине

        Returns:
            int: количество товаров
        """
        return len(self.driver.find_elements(*self.CART_ITEMS))

    def continue_shopping(self) -> None:
        """Продолжить покупки"""
        self.click(self.CONTINUE_SHOPPING)
