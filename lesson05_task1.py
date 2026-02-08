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

        all_buttons = driver.find_elements(By.TAG_NAME, "button")
        target_button = None

        for btn in all_buttons:
            class_attr = btn.get_attribute("class") or ""
            if "btn-primary" in class_attr:
                target_button = btn
                break

        if target_button:
            target_button.click()
            time.sleep(1)
            alert = driver.switch_to.alert
            alert.accept()
            success_msg = f"Запуск {i+1}: Успех"
            print(success_msg)
        else:
            not_found_msg = f"Запуск {i+1}: Кнопка не найдена"
            print(not_found_msg)

    except Exception as e:
        error_msg = f"Запуск {i+1}: Ошибка - {e}"
        print(error_msg)

    finally:
        driver.quit()

message = "\nВсе 3 запуска завершены!"
print(message)
