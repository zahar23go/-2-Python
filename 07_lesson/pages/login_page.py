from selenium.webdriver.common.by import By


class LoginPage:
    """Page Object для страницы авторизации"""

    def __init__(self, driver):
        self.driver = driver

    # Локаторы
    USERNAME_INPUT = (By.ID, "user-name")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")

    def open(self):
        """Открыть страницу авторизации"""
        self.driver.get("https://www.saucedemo.com/")

    def enter_username(self, username):
        """Ввести имя пользователя"""
        self.driver.find_element(*self.USERNAME_INPUT).send_keys(username)

    def enter_password(self, password):
        """Ввести пароль"""
        self.driver.find_element(*self.PASSWORD_INPUT).send_keys(password)

    def click_login(self):
        """Нажать кнопку входа"""
        self.driver.find_element(*self.LOGIN_BUTTON).click()

    def login(self, username, password):
        """Выполнить полный процесс авторизации"""
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()
