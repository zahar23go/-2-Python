import allure
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage


@allure.title("Тест покупки в магазине")
@allure.description("Проверка полного цикла покупки")
@allure.feature("Магазин")
@allure.severity(allure.severity_level.BLOCKER)
def test_shop(driver):
    with allure.step("Авторизация"):
        login_page = LoginPage(driver)
        login_page.open()
        login_page.login("standard_user", "secret_sauce")

    with allure.step("Добавление товаров в корзину"):
        inventory_page = InventoryPage(driver)
        inventory_page.add_item_to_cart("Sauce Labs Backpack")
        inventory_page.add_item_to_cart("Sauce Labs Bolt T-Shirt")

    with allure.step("Переход в корзину"):
        inventory_page.go_to_cart()

    with allure.step("Оформление заказа"):
        cart_page = CartPage(driver)
        cart_page.checkout()

    with allure.step("Заполнение информации"):
        checkout_page = CheckoutPage(driver)
        checkout_page.fill_checkout_info("John", "Doe", "12345")

    with allure.step("Завершение покупки"):
        checkout_page.finish_checkout()

    with allure.step("Проверка успешной покупки"):
        assert "Thank you for your order" in checkout_page.get_complete_header()