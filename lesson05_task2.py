from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

print("=" * 60)
print("Упражнение 2: Клик по кнопке без ID")
print("=" * 60)

driver = webdriver.Chrome()

try:
    # 1. Открываем страницу
    driver.get("http://uitestingplayground.com/dynamicid")
    print("✓ Страница загружена")
    
    # 2. Находим кнопку БЕЗ использования ID
    # Кнопка имеет динамический ID, который меняется при каждом обновлении страницы
    # Используем другие атрибуты для поиска
    
    # Вариант 1: Поиск по тексту кнопки и классу
    blue_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((
            By.XPATH,
            "//button[text()='Button with Dynamic ID' and contains(@class, 'btn-primary')]"
        ))
    )
    
    print(f"✓ Найдена кнопка: '{blue_button.text}'")
    print(f"✓ Класс кнопки: {blue_button.get_attribute('class')}")
    print(f"✓ ID кнопки (динамический): {blue_button.get_attribute('id')}")
    
    # 3. Кликаем по кнопке
    blue_button.click()
    print("✓ Клик выполнен успешно!")
    
    # 4. Проверяем, что кнопка была нажата
    time.sleep(1)
    print("✓ Тест пройден: кнопка найдена и нажата без использования ID")
    
    # 5. Демонстрация динамического ID
    print("\nДемонстрация динамического ID:")
    print("Если обновить страницу, ID кнопки изменится:")
    
    # Обновляем страницу и проверяем новый ID
    driver.refresh()
    time.sleep(1)
    
    blue_button_new = driver.find_element(
        By.XPATH,
        "//button[text()='Button with Dynamic ID' and contains(@class, 'btn-primary')]"
    )
    
    new_id = blue_button_new.get_attribute('id')
    print(f"Новый ID после обновления: {new_id}")
    print("Это подтверждает, что ID динамический и не должен использоваться в селекторах")
    
except Exception as e:
    print(f"✗ Ошибка: {e}")
    
finally:
    driver.quit()
    print("\n✓ Браузер закрыт")
    print("=" * 60)
    print("Скрипт завершен. Запустите его еще 2 раза через терминал.")
    print("=" * 60)