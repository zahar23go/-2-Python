import allure
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage


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
        inventory_page.add_to_cart("Sauce Labs Backpack")
        inventory_page.add_to_cart("Sauce Labs Bike Light")

        with allure.step("Переход в корзину"):
            inventory_page.go_to_cart()

        assert "cart" in driver.current_url.lower(), "Не удалось перейти в корзину"

    with allure.step("Оформление заказа"):
        cart_page = CartPage(driver)
        cart_page.checkout()
