import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions


@pytest.fixture(scope="function")
def chrome_browser():
    """Фикстура для Chrome браузера"""
    options = ChromeOptions()
    options.add_argument("--headless")  # Опционально: для запуска в фоне
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture(scope="function")
def firefox_browser():
    """Фикстура для Firefox браузера"""
    options = FirefoxOptions()
    options.add_argument("--headless")  # Опционально: для запуска в фоне
    driver = webdriver.Firefox(options=options)
    driver.maximize_window()
    yield driver
    driver.quit()
