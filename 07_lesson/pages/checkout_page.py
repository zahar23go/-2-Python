from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CheckoutPage:
    """Page Object для страницы оформления заказа"""

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    # Локаторы
    FIRST_NAME_INPUT = (By.ID, "first-name")
    LAST_NAME_INPUT = (By.ID, "last-name")
    POSTAL_CODE_INPUT = (By.ID, "postal-code")
    CONTINUE_BUTTON = (By.ID, "continue")
    TOTAL_LABEL = (By.CLASS_NAME, "summary_total_label")

    def enter_first_name(self, first_name):
        """Ввести имя"""
        self.driver.find_element(*self.FIRST_NAME_INPUT).send_keys(
            first_name
        )

    def enter_last_name(self, last_name):
        """Ввести фамилию"""
        self.driver.find_element(*self.LAST_NAME_INPUT).send_keys(
            last_name
        )

    def enter_postal_code(self, postal_code):
        """Ввести почтовый индекс"""
        self.driver.find_element(*self.POSTAL_CODE_INPUT).send_keys(
            postal_code
        )

    def click_continue(self):
        """Нажать кнопку Continue"""
        self.driver.find_element(*self.CONTINUE_BUTTON).click()

    def fill_checkout_form(self, first_name, last_name, postal_code):
        """Заполнить форму оформления заказа"""
        self.enter_first_name(first_name)
        self.enter_last_name(last_name)
        self.enter_postal_code(postal_code)
        self.click_continue()

    def get_total_amount(self):
        """Получить итоговую сумму"""
        self.wait.until(
            EC.presence_of_element_located(self.TOTAL_LABEL)
        )
        total_text = self.driver.find_element(*self.TOTAL_LABEL).text
        # Извлекаем число из строки вида "Total: $58.29"
        return total_text.replace("Total: ", "")
