import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import os
from typing import Generator, Any

@pytest.fixture
def driver() -> Generator[Any, None, None]:
    '''
    Фикстура для создания и закрытия драйвера браузера
    
    Returns:
        WebDriver: экземпляр драйвера
    '''
    # Настройка опций Chrome
    chrome_options = Options()
    chrome_options.add_argument('--headless')  # Для безголового режима
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    
    # Путь к ChromeDriver (укажите правильный путь)
    chrome_driver_path = r'C:\chromedriver\chromedriver.exe'
    
    # Проверяем, существует ли файл
    if os.path.exists(chrome_driver_path):
        service = Service(chrome_driver_path)
        driver = webdriver.Chrome(service=service, options=chrome_options)
    else:
        # Если файл не найден, пробуем без указания пути
        driver = webdriver.Chrome(options=chrome_options)
    
    driver.maximize_window()
    driver.implicitly_wait(10)
    
    yield driver
    
    # Закрытие драйвера после теста
    driver.quit()
