from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage


class TestShop:
    """Тесты для интернет-магазина"""

    def test_shop_purchase_total(self, firefox_browser):
        """Тест проверки итоговой суммы покупки"""
        # Создаем объекты страниц
        login_page = LoginPage(firefox_browser)
        inventory_page = InventoryPage(firefox_browser)
        cart_page = CartPage(firefox_browser)
        checkout_page = CheckoutPage(firefox_browser)

        # Открываем страницу авторизации и входим
        login_page.open()
        login_page.login("standard_user", "secret_sauce")

        # Добавляем товары в корзину
        inventory_page.add_backpack_to_cart()
        inventory_page.add_bolt_tshirt_to_cart()
        inventory_page.add_onesie_to_cart()

        # Переходим в корзину
        inventory_page.go_to_cart()

        # Нажимаем Checkout
        cart_page.click_checkout()

        # Заполняем форму
        checkout_page.fill_checkout_form(
            "Иван",
            "Петров",
            "123456"
        )

        # Получаем итоговую сумму
        total = checkout_page.get_total_amount()

        # Проверяем итоговую сумму
        assert total == "$58.29", f"Ожидалось $58.29, получено {total}"
