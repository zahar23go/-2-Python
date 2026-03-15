import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from typing import Generator, Any
import os

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
    
    # Автоматическое управление ChromeDriver через webdriver-manager
    driver_path = ChromeDriverManager().install()
    
    # Исправление для Windows - берем правильный путь к chromedriver.exe
    if "THIRD_PARTY_NOTICES" in driver_path:
        # Если скачался файл с уведомлениями, берем папку и ищем chromedriver.exe
        driver_dir = os.path.dirname(driver_path)
        driver_path = os.path.join(driver_dir, "chromedriver.exe")
        
        # Если файл не существует, пробуем другие варианты
        if not os.path.exists(driver_path):
            # Проверяем подпапку chromedriver-win32
            alternative_path = os.path.join(driver_dir, "chromedriver-win32", "chromedriver.exe")
            if os.path.exists(alternative_path):
                driver_path = alternative_path
    
    print(f"Используется драйвер: {driver_path}")  # Для отладки
    
    service = Service(driver_path)
    driver = webdriver.Chrome(service=service, options=chrome_options)
    
    driver.maximize_window()
    driver.implicitly_wait(10)
    
    yield driver
    
    # Закрытие драйвера после теста
    driver.quit()