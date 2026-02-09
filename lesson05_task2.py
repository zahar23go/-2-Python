"""
Exercise 2. Click button without ID
URL: http://uitestingplayground.com/dynamicid
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

try:
    driver.get("http://uitestingplayground.com/dynamicid")
    time.sleep(2)

    xpath = ("//button[contains(@class, 'btn-primary') "
             "and text()='Button with Dynamic ID']")
    blue_button = driver.find_element(By.XPATH, xpath)
    blue_button.click()
    print("Click on blue button done")
    time.sleep(2)

    print("Task 2 completed successfully!")

except Exception as e:
    print(f"Error: {e}")

finally:
    driver.quit()
