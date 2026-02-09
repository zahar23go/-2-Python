from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.firefox import GeckoDriverManager
import time

driver = webdriver.Firefox(
    executable_path=GeckoDriverManager().install()
)

try:
    driver.get("http://the-internet.herokuapp.com/inputs")
    time.sleep(2)

    input_field = driver.find_element(By.TAG_NAME, "input")
    input_field.send_keys("Sky")
    time.sleep(1)
    input_field.clear()
    time.sleep(1)
    input_field.send_keys("Pro")

    print("Задание 3 выполнено: текст 'Pro' введен в поле")

except Exception as e:
    print(f"Ошибка: {e}")

finally:
    driver.quit()
