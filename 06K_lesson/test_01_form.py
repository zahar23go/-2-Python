"""
Тест для проверки формы с валидацией полей
Используется браузер Microsoft Edge
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.edge.service import Service
import os


class TestForm:
    """Тест для проверки формы с подсветкой полей"""

    def setup_method(self):
        """Подготовка перед каждым тестом"""
        # Указываем путь к скачанному драйверу
        edge_driver_path = r"C:\WebDrivers\msedgedriver.exe"

        # Проверяем, существует ли файл драйвера
        if not os.path.exists(edge_driver_path):
            raise FileNotFoundError(
                f"EdgeDriver не найден по пути: {edge_driver_path}\n"
                "Скачайте его с:\n"
                "https://developer.microsoft.com/en-us/microsoft-edge/"
                "tools/webdriver/\n"
                "И поместите в C:\\WebDrivers\\msedgedriver.exe"
            )

        # Создаем сервис с указанием пути к драйверу
        service = Service(executable_path=edge_driver_path)
        self.driver = webdriver.Edge(service=service)
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 10)

    def teardown_method(self):
        """Очистка после каждого теста"""
        if self.driver:
            self.driver.quit()

    def test_form_validation(self):
        """Тест проверки валидации формы"""
        # Открываем страницу
        url = "https://bonigarcia.dev/selenium-webdriver-java/"
        self.driver.get(url + "data-types.html")

        # Заполняем форму значениями
        first_name = self.wait.until(
            EC.presence_of_element_located((By.NAME, "first-name")))
        first_name.clear()
        first_name.send_keys("Иван")

        last_name = self.driver.find_element(By.NAME, "last-name")
        last_name.clear()
        last_name.send_keys("Петров")

        address = self.driver.find_element(By.NAME, "address")
        address.clear()
        address.send_keys("Ленина, 55-3")

        email = self.driver.find_element(By.NAME, "e-mail")
        email.clear()
        email.send_keys("test@skypro.com")

        phone = self.driver.find_element(By.NAME, "phone")
        phone.clear()
        phone.send_keys("+7985899998787")

        zip_code = self.driver.find_element(By.NAME, "zip-code")
        zip_code.clear()

        city = self.driver.find_element(By.NAME, "city")
        city.clear()
        city.send_keys("Москва")

        country = self.driver.find_element(By.NAME, "country")
        country.clear()
        country.send_keys("Россия")

        job_position = self.driver.find_element(By.NAME, "job-position")
        job_position.clear()
        job_position.send_keys("QA")

        company = self.driver.find_element(By.NAME, "company")
        company.clear()
        company.send_keys("SkyPro")

        # Находим кнопку и кликаем через JavaScript
        submit_button = self.wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//button[@type='submit']")))

        self.driver.execute_script("arguments[0].click();", submit_button)

        # Ждем появления результатов
        self.wait.until(
            EC.presence_of_element_located(
                (By.CLASS_NAME, "alert-success")))

        # Проверяем поле Zip code (красное)
        zip_result = self.driver.find_element(By.ID, "zip-code")
        zip_class = zip_result.get_attribute("class")
        assert "danger" in zip_class, (
            f"Zip code должно быть красным, класс: {zip_class}")

        # Проверяем остальные поля (зеленые)
        green_fields = [
            "first-name", "last-name", "address", "e-mail",
            "phone", "city", "country", "job-position", "company"
        ]

        for field_id in green_fields:
            field = self.driver.find_element(By.ID, field_id)
            field_class = field.get_attribute("class")
            assert "success" in field_class, (
                f"Поле {field_id} должно быть зеленым, "
                f"класс: {field_class}")
