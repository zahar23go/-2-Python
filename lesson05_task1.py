"""
Exercise 1. Click button with CSS-class
URL: http://uitestingplayground.com/classattr
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

try:
    driver.get("http://uitestingplayground.com/classattr")
    time.sleep(2)

    blue_button = driver.find_element(By.CLASS_NAME, "btn-primary")
    blue_button.click()
    print("Click on blue button done")
    time.sleep(2)

    driver.switch_to.alert.accept()
    print("Popup closed")

    print("Task 1 completed successfully!")

except Exception as e:
    print(f"Error: {e}")

finally:
    driver.quit()
