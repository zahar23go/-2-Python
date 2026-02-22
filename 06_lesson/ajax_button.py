"""
Задание 1.1: Нажать на кнопку и получить текст из зеленой плашки.
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def main():
    """Основная функция скрипта."""
    driver = webdriver.Chrome()
    try:
        driver.get("http://uitestingplayground.com/ajax")

        button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "ajaxButton"))
        )
        button.click()

        green_badge = WebDriverWait(driver, 15).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "bg-success"))
        )
        print(green_badge.text)

    finally:
        driver.quit()


if __name__ == "__main__":
    main()
