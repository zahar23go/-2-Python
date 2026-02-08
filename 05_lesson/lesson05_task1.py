from selenium import webdriver
from selenium.webdriver.common.by import By
import time

for i in range(3):
    print(f"\n{'='*40}")
    print(f"ЗАПУСК {i+1}")
    print(f"{'='*40}")
    
    driver = webdriver.Chrome()
    
    try:
        driver.get("https://demoqa.com/alerts")
        
        target_button = driver.find_element(
            By.XPATH,
            "//button[contains(concat(' ', normalize-space(@class), ' '), ' btn-primary ')]"
        )
        
        target_button.click()
        time.sleep(1)
        alert = driver.switch_to.alert
        alert.accept()
        print(f"Запуск {i+1}: Успех")
            
    except Exception as e:
        print(f"Запуск {i+1}: Ошибка - {e}")
        
    finally:
        driver.quit()

print("\nВсе 3 запуска завершены!")