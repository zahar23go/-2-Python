"""
Задание 1.3: Дождаться загрузки всех картинок.
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def main():
    """Основная функция скрипта."""
    driver = webdriver.Chrome()
    try:
        driver.get(
            "https://bonigarcia.dev/selenium-webdriver-java/"
            "loading-images.html"
        )

        WebDriverWait(driver, 15).until(
            EC.presence_of_element_located(
                (By.XPATH, "//*[contains(text(), 'Done')]")
            )
        )

        WebDriverWait(driver, 10).until(
            lambda d: len(d.find_elements(By.TAG_NAME, "img")) >= 5
        )

        images = driver.find_elements(By.TAG_NAME, "img")
        print(images[2].get_attribute("src"))

    finally:
        driver.quit()


if __name__ == "__main__":
    main()
