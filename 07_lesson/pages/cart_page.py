from selenium.webdriver.common.by import By


class CartPage:
    """Page Object для страницы корзины"""

    def __init__(self, driver):
        self.driver = driver

    # Локаторы
    CHECKOUT_BUTTON = (By.ID, "checkout")
    CART_ITEM = (By.CLASS_NAME, "cart_item")

    def click_checkout(self):
        """Нажать кнопку Checkout"""
        self.driver.find_element(*self.CHECKOUT_BUTTON).click()

    def get_cart_items_count(self):
        """Получить количество товаров в корзине"""
        items = self.driver.find_elements(*self.CART_ITEM)
        return len(items)
