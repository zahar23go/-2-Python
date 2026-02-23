from selenium.webdriver.common.by import By


class InventoryPage:
    """Page Object для главной страницы магазина"""

    def __init__(self, driver):
        self.driver = driver

    # Локаторы
    ADD_BACKPACK_BUTTON = (By.ID, "add-to-cart-sauce-labs-backpack")
    ADD_BOLT_TSHIRT_BUTTON = (By.ID, "add-to-cart-sauce-labs-bolt-t-shirt")
    ADD_ONESIE_BUTTON = (By.ID, "add-to-cart-sauce-labs-onesie")
    CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")
    CART_LINK = (By.CLASS_NAME, "shopping_cart_link")

    def add_backpack_to_cart(self):
        """Добавить рюкзак в корзину"""
        self.driver.find_element(*self.ADD_BACKPACK_BUTTON).click()

    def add_bolt_tshirt_to_cart(self):
        """Добавить футболку в корзину"""
        self.driver.find_element(*self.ADD_BOLT_TSHIRT_BUTTON).click()

    def add_onesie_to_cart(self):
        """Добавить Onesie в корзину"""
        self.driver.find_element(*self.ADD_ONESIE_BUTTON).click()

    def go_to_cart(self):
        """Перейти в корзину"""
        self.driver.find_element(*self.CART_LINK).click()

    def get_cart_count(self):
        """Получить количество товаров в корзине"""
        return self.driver.find_element(*self.CART_BADGE).text
