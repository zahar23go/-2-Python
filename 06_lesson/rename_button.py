"""
Задание 1.2: Переименовать кнопку
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def main():
    """Переименовываем кнопку на странице"""
    driver = webdriver.Chrome()

    try:
        # Шаг 1: Переходим на страницу
        print("1. Открываем страницу...")
        driver.get("http://uitestingplayground.com/textinput")

        # Шаг 2: Вводим текст в поле
        print("2. Вводим текст 'SkyPro'...")
        input_field = driver.find_element(By.ID, "newButtonName")
        input_field.send_keys("SkyPro")

        # Шаг 3: Нажимаем на синюю кнопку
        print("3. Нажимаем кнопку...")
        update_button = driver.find_element(By.ID, "updatingButton")
        update_button.click()

        # Шаг 4: Ждем обновления текста кнопки
        print("4. Ожидаем обновления текста...")
        WebDriverWait(driver, 10).until(
            EC.text_to_be_present_in_element(
                (By.ID, "updatingButton"), "SkyPro")
        )

        # Получаем текст кнопки
        button_text = driver.find_element(By.ID, "updatingButton").text
        print(f"5. Текст кнопки: '{button_text}'")

        # Проверка
        if button_text == "SkyPro":
            print("✅ Тест пройден!")
        else:
            print("❌ Тест не пройден")

    finally:
        input("Нажми Enter для закрытия...")
        driver.quit()


if __name__ == "__main__":
    main()
