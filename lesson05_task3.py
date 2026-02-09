"""
Exercise 3. Input field
URL: http://the-internet.herokuapp.com/inputs
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
import time

service = Service(GeckoDriverManager().install())
driver = webdriver.Firefox(service=service)

try:
    driver.get("http://the-internet.herokuapp.com/inputs")
    time.sleep(2)

    input_field = driver.find_element(By.TAG_NAME, "input")
    input_field.send_keys("Sky")
    time.sleep(1)
    print("Text 'Sky' entered")

    input_field.clear()
    time.sleep(1)
    print("Field cleared")

    input_field.send_keys("Pro")
    time.sleep(1)
    print("Text 'Pro' entered")

    print("Task 3 completed successfully!")

except Exception as e:
    print(f"Error: {e}")

finally:
    driver.quit()
    print("Browser closed")
